# Subset: Samples


_Sample/biosample datamodel_



URI: [Samples](Samples)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## Classes in subset

| Class | Description |
| --- | --- |
| [Attribute](Attribute.md) | A property or characteristic of an entity |


### Attribute

A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [has_attribute](has_attribute.md) | 0..* <br/> [Attribute](Attribute.md)  | connects any entity to an attribute   |
| [has_attribute_type](has_attribute_type.md) | 1..1 <br/> [OntologyClass](OntologyClass.md)  | connects an attribute to a class that describes it   |
| [has_qualitative_value](has_qualitative_value.md) | 0..1 <br/> [NamedThing](NamedThing.md)  | connects an attribute to a value   |
| [has_quantitative_value](has_quantitative_value.md) | 0..* <br/> [QuantityValue](QuantityValue.md)  | connects an attribute to a value   |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md)  | The human-readable 'attribute name' can be set to a string which reflects its...   |




## Slots in subset

| Slot | Description |
| --- | --- |
| [derives_from](derives_from.md) | holds between two distinct material entities, the new entity and the old enti... |
| [has_attribute](has_attribute.md) | connects any entity to an attribute |
| [has_attribute_type](has_attribute_type.md) | connects an attribute to a class that describes it |
| [has_numeric_value](has_numeric_value.md) | connects a quantity value to a number |
| [has_qualitative_value](has_qualitative_value.md) | connects an attribute to a value |
| [has_quantitative_value](has_quantitative_value.md) | connects an attribute to a value |
| [has_unit](has_unit.md) | connects a quantity value to a unit |
| [iri](iri.md) | An IRI for an entity |
| [name](name.md) | A human-readable name for an attribute or entity |


## Enumerations in subset

| Enumeration | Description |
| --- | --- |

