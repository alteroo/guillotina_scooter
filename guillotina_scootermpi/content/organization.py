import sys
from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina import content
from .address import IAddress
from .contact_point import IContactPoint
from .codeable_concept import ICodeableConcept


class IOrganization(interfaces.IItem):
    """ A grouping of people or organizations with a common purpose.
    A formally or informally recognized grouping of people or organizations
    formed for the purpose of achieving some form of collective action.
    Includes companies, institutions, corporations, departments, community
    groups, healthcare practice groups, payer/insurer, etc.
    """

    active = schema.Bool(default=True)

    address = schema.List(value_type=schema.Object(IAddress))

    # List of alternate names the organization is/was known as.
    alias = schema.List(required=False, value_type=schema.Text())

    # Organization Name
    name = schema.Text()

    # Contact details for the organization
    telecom = schema.List(value_type=schema.Object(IContactPoint))

    organization_type = schema.Text()


@configure.contenttype(type_name="Organization", schema=IOrganization)
class Organization(content.Item):
    """
    Organization
    """
