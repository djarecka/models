# Class: EntityToExposureEventAssociationMixin


_An association between some entity and an exposure event._





URI: [bican:EntityToExposureEventAssociationMixin](https://identifiers.org/brain-bican/vocab/EntityToExposureEventAssociationMixin)



```mermaid
 classDiagram
    class EntityToExposureEventAssociationMixin
      EntityToExposureEventAssociationMixin <|-- DiseaseToExposureEventAssociation
      
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | An association between an exposure event and a disease |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:EntityToExposureEventAssociationMixin |
| native | bican:EntityToExposureEventAssociationMixin |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: entity to exposure event association mixin
description: An association between some entity and an exposure event.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  object:
    name: object
    domain_of:
    - association
    range: exposure event
defining_slots:
- object

```
</details>

### Induced

<details>
```yaml
name: entity to exposure event association mixin
description: An association between some entity and an exposure event.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  object:
    name: object
    domain_of:
    - association
    range: exposure event
defining_slots:
- object

```
</details>