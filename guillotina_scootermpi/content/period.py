from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina import content


class IPeriod(interfaces.IItem):
    """ Time range defined by start and end date.
    A time period defined by a start and end date.
    """

    start_date = schema.Date()
    end_date = schema.Date()


@configure.contenttype(type_name="Period", schema=IPeriod)
class Period(content.Item):
    """
    """
