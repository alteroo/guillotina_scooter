from guillotina import schema, configure, content, interfaces
from guillotina.api.service import Service
from guillotina.directives import index_field
from guillotina.api.content import DefaultPOST, DefaultPATCH
import uuid
import json


class IScooterTag(interfaces.IItem):
    date = schema.Date()
    description = schema.Text()
    index_field("tag_id", type="keyword")
    tag_id = schema.TextLine()


@configure.contenttype(type_name="ScooterTag",
                       schema=IScooterTag)
class ScooterTag(content.Item):
    pass
