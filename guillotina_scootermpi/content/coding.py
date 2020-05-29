from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina import content


class ICoding(interfaces.IItem):
    """ A reference to a code defined by a terminology system.
      """
    # Symbol as defined by the system
    code = schema.Text()

    # Representation of code by the system
    display = schema.Text()

    # Was the code chosen directly by the user?
    user_selected = schema.Bool()

    # The system in which this code is defined.
    system = schema.Text()

    # Version of the system - if applicable
    version = schema.Text()


@configure.contenttype(type_name="Coding", schema=ICoding)
class Coding(content.Item):
    """
    Coding
    """
