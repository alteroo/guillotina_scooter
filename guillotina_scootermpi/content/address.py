from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina import content


class IAddress(interfaces.IItem):

    # Address Line (Street name, number, PO Box etc)
    address_line = schema.List(value_type=schema.Text())

    # Name of city/town
    city = schema.Text()

    # Country. Can be ISO 3166 2 or 3 letter code
    # https://www.iso.org/iso-3166-country-codes.html
    country = schema.Text()

    # Parish
    parish = schema.Text()
    # postal | physical | both
    address_type = schema.Text(required=False)

    # home | work | temp | old | billing - purpose of this address.
    use = schema.Text(required=False)


@configure.contenttype(type_name="Address", schema=IAddress)
class Address(content.Item):
    """
    Address
    """
