from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina.api.service import Service
from guillotina.directives import index_field
from guillotina import content
from guillotina.api import search
from guillotina.api.content import DefaultPOST
from guillotina.response import HTTPBadRequest
import re
import json


class IPatientIndex(interfaces.IItem):

    first_name = schema.Text()
    last_name = schema.Text()
    active = schema.Bool(default=True)
    middle_names = schema.List(value_type=schema.Text())
    date_of_birth = schema.Date()
    addresses = schema.List(
        value_type=schema.Dict(key_type=schema.Text(),
                               value_type=schema.Text())
    )
    activities = schema.List(
        value_type=schema.Dict(key_type=schema.Text(),
                               value_type=schema.Text()),
    )
    # Set primary_id as index_field to allow search
    index_field("primary_id", type="keyword")
    # Constraint validates ID is 9 digits to match TRN format
    primary_id = schema.Text(constraint=lambda val: re.match("\d{9}", val) != None)
    secondary_id = schema.Text(required=False)


@configure.contenttype(type_name="PatientIndex", schema=IPatientIndex)
class PatientIndex(content.Item):
    """
    Patient Index
    """


class BasePatient(Service):
    async def get_patient_exists(self) -> PatientIndex:
        data = await self.request.json()
        primary_id: str = data["primary_id"]
        search_request = self.request
        search_request.data = json.dumps({"type_name": "PatientIndex", "primary_id": f"{primary_id}"})
        search_result = await search.search_post(self.context, search_request)
        if search_result['items_count'] == 0:
            return False
        else:
            return True


@configure.service(
    context=interfaces.IResource,
    permission='guillotina.AccessContent',
    name="@create",
    method="POST",
    responses={
        "200": {
            "description": "Add patient",
            # TODO: add response content schema here
        },
        "404": {
            "description": "User exists"
        }

    },
    summary="Add new patient",
    allow_access=True,
)
class AddUser(BasePatient):
    async def __call__(self):
        patientExists: bool = await self.get_patient_exists()
        if (patientExists):
            raise HTTPBadRequest(content={
                "reason": "duplicateID",
                "details": "A user already exists with this primary_id"
            })
        else:
            view = DefaultPOST(self.context, self.request)
            return await view()
