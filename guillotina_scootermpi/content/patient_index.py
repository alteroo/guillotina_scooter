from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina import content


class IPatientIndex(interfaces.IItem):
    text = schema.Text()
    first_name = schema.Text()
    last_name = schema.Text()
    middle_names = schema.List(
        value_type=schema.Dict(key_type=schema.Text(), value_type=schema.Text())
    )
    date_of_birth = schema.Date()
    addresses = schema.List(
        value_type=schema.Dict(key_type=schema.Text(), value_type=schema.Text())
    )
    activities = fields.BucketListField(
        value_type=schema.Dict(key_type=schema.Text(), value_type=schema.Text()),
        bucket_len=5000,
    )
    id_data = schema.List(
        value_type=schema.Dict(key_type=schema.Text(), value_type=schema.Text())
    )


@configure.contenttype(type_name="PatientIndex", schema=IPatientIndex)
class PatientIndex(content.Item):
    """
    Patient Index 
    """
