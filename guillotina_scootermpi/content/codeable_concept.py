from guillotina import schema, fields, configure
from guillotina import interfaces
from guillotina import content
from .coding import ICoding


class ICodeableConcept(interfaces.IItem):
    """ Concept - reference to a terminology or just  text.
    A concept that may be defined by a formal reference to a terminology or
    ontology or may be provided by text.
    eg.
    "valueCodeableConcept": {
                "coding": [
                        {
                                "system": "http://snomed.info/sct",
                                "code": "260385009",
                                "display": "Negative"
                        }, {
                                "system": "https://acme.lab/resultcodes",
                                "code": "NEG",
                                "display": "Negative"
                        }
                ],
                "text": "Negative for Chlamydia Trachomatis rRNA"
          }
    """

    # List of concept code definitions
    coding = schema.List(value_type=schema.Object(ICoding))

    # Description/Display text for the concept.
    # May contain free text in lieue of codings
    text = schema.Text()


@configure.contenttype(type_name="CodeableConcept", schema=ICodeableConcept)
class CodeableConcept(content.Item):
    """
    Codeable Concept
    """
