from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina import content
from .period import IPeriod
from .codeable_concept import ICodeableConcept


class IIdentifier(interfaces.IItem):
    """ An identifier intended for computation.
    An identifier - identifies some entity uniquely and unambiguously.
    Typically this is used for business identifiers.
    """

    # Time period when id is/was valid
    period = schema.Object(IPeriod)

    # Namespace for the identifier value
    system = schema.Text()

    # Description of identifier
    identifier_type = schema.Object(ICodeableConcept)

    # usual | official | temp | secondary | old (If known).
    use = schema.Text()

    # ID value (TRN number, NIS number etc)
    value = schema.Text()


@configure.contenttype(type_name="Identifer", schema=IIdentifier)
class Identifier(content.Item):
    """
    Identifier
    """
