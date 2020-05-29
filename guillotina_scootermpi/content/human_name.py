from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina import content


class IHumanName(interfaces.IItem):
    """ Interface defining Human name.
    """
    last_name = schema.Text()

    first_name = schema.Text()

    # Given names (not always 'first'). Includes middle names
    given_name = schema.List(value_type=schema.Text(), required=False)

    # Parts that come before the name.
    prefix = schema.List(value_type=schema.Text(), required=False)

    # Parts that come after the name.
    suffix = schema.List(value_type=schema.Text(), required=False)

    # Text representation of the full name.
    text = schema.Text(required=False)

    # usual | official | temp | nickname | anonymous | old | maiden.
    use = schema.Text(required=False)


@configure.contenttype(type_name="HumanName", schema=IHumanName)
class HumanName(content.Item):
    """
    Human Name
    """
