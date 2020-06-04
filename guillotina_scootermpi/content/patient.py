import json
import re
import uuid

from elasticsearch_dsl import Q, Search
from guillotina import (configure, content, fields, interfaces, schema,
                        task_vars, utils)
from guillotina.api import search
from guillotina.api.content import DefaultPOST
from guillotina.api.service import Service
from guillotina.component import get_utility
from guillotina.directives import index_field
from guillotina.interfaces import IContainer
from guillotina.response import HTTPBadRequest
from guillotina_elasticsearch.interfaces import IElasticSearchUtility
from guillotina_elasticsearch.queries import build_security_query
from guillotina_elasticsearch.utility import ElasticSearchUtility

from guillotina_scootermpi.content.address import IAddress
from guillotina_scootermpi.content.contact_point import IContactPoint
from guillotina_scootermpi.content.human_name import IHumanName
from guillotina_scootermpi.content.scooter_tag import ScooterTag


class IPatientFolder(interfaces.IFolder):
    """
    Patient Folder. Exists mostly for enabling custom Grange page rendering
    """


@configure.contenttype(schema=IPatientFolder, type_name="PatientFolder",
                       allowed_types=["Patient"])
class PatientFolder(content.Folder):
    """
    Patient Folder
    """


class IPatient(interfaces.IFolder):

    active = schema.Bool(default=True)

    addresses = schema.List(value_type=schema.Object(IAddress), required=False)

    date_of_birth = schema.Date()

    deceased = schema.Bool(default=False)

    # male | female | other | unknown.
    gender = schema.Text()

    maritalStatus = schema.Text(required=False)

    multipleBirthBool = schema.Bool(default=False)

    multipleBirthInt = schema.Int(required=False)

    name = schema.Object(IHumanName)

    # Set primary_id as index_field to allow search
    # Constraint validates ID is 9 digits to match TRN format
    index_field("primary_id", type="text")
    primary_id = schema.Text(constraint=lambda val: re.match("\d{9}", val) != None)

    secondary_id = schema.TextLine(required=False)
    secondary_id_description = schema.Text(required=False)

    telecom = schema.List(value_type=schema.Object(IContactPoint))

    managingOrganization = schema.Text(required=False)


@configure.contenttype(schema=IPatient, type_name="Patient",
                       allowed_types=["ScooterTag"])
class Patient(content.Folder):
    """
    Patient
    """


@configure.service(
    context=interfaces.IResource,
    permission='guillotina.AccessContent',
    name="@create",
    method="POST",
    responses={
        "200": {
            "description": "Add patient",
        },
        "404": {
            "description": "User exists"
        }
    },
    summary="Add new patient"
)
class AddUser(DefaultPOST):
    async def get_patient_exists(self) -> Patient:
        data = await self.request.json()
        primary_id: str = data["primary_id"]
        search_request = self.request
        musts = [{"match": {"type_name": "Patient"}}]
        el_query = {
            "query": {
                "query": {"bool": {"must": musts}},
            }
        }
        musts.append({"match": {"primary_id": f"{primary_id}"}})
        search_request.query = el_query

        print(el_query)
        # es = get_utility(IElasticSearchUtility)
        # search_result = await IElasticSearchUtility.search_raw(task_vars.container.get(), el_query)
        search_result = await search.search_get(task_vars.container.get(),
                                                search_request)
        print(search_result)
        if search_result['items_count'] == 0:
            return False
        else:
            return True

    async def get_data(self):
        patientExists: bool = await self.get_patient_exists()
        if (patientExists):
            raise HTTPBadRequest(content={
                "reason": "duplicateID",
                "details": "A user already exists with this primary_id"
            })
        else:
            data = await super().get_data()
            full_name = ('%s %s' % (data['name']['first_name'],
                                    data['name']['last_name']))
            data['title'] = full_name
            data['name']['text'] = full_name
            return data


# Service to intercept POST request and generate
# uuid & tag_id before saving the object.
@configure.service(
    context=IPatient,
    name="@generate-tag",
    permission='guillotina.AccessContent',
    method="POST",
    summary="""Save new Scooter Tag. Generates uuid & creates tag_id
    using last 4 digits of parent uuid & tag uuid"""
)
class AddScooterTag(DefaultPOST):
    # Override DefaultPOSTS's get_data to manually set uuid
    # and tag_id generated from parent uuid & tag uuid
    async def get_data(self):
        data = await super().get_data()
        tag_uuid = str(uuid.uuid1()).replace("-", "")
        patient_uid = self.context.__parent__.uuid
        data["title"] = data['description']
        data["id"] = tag_uuid
        data["tag_id"] = self.build_id(patient_uuid=patient_uid,
                                       tag_uuid=tag_uuid)
        return data

    # Build tag_id using last 4 digits of patient & tag uuids
    def build_id(self, patient_uuid, tag_uuid) -> ScooterTag:
        return ('%s-%s' % (patient_uuid[-4:], tag_uuid[-4:]))