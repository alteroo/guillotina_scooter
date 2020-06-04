from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina import content
from .period import IPeriod
from zope.interface import Interface
import typing


class IContactPoint(Interface):
    """ Details of a Technology mediated contact point
    (phone, fax, email, etc.).
    Details for all kinds of technology mediated contact points for a person or
    organization, including telephone, email, etc.
    """
    period = schema.List(value_type=schema.Object(IPeriod), default=[],
                         required=False)

    # Specify preferred order of use (1 = highest)
    rank = schema.Int(default=1, required=False)

    # phone | fax | email | pager | url | sms | other.
    contact_type = schema.Text(required=False)

    # home | work | temp | old | mobile - purpose of this contact point.
    contact_use = schema.Text(required=False)

    # Contact Point Details
    name = schema.Text()

    # Contact Point details
    value = schema.Text()


@configure.contenttype(type_name="ContactPoint", schema=IContactPoint)
class ContactPoint(content.Item):
    """
    Contact Point
    """
    rank = 1
    period: typing.List[IPeriod] = []
    contact_type = "phone"
    contact_use = "mobile"
