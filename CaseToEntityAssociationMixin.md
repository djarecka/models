# Class: CaseToEntityAssociationMixin


_An abstract association for use where the case is the subject_





URI: [bican:CaseToEntityAssociationMixin](https://identifiers.org/brain-bican/vocab/CaseToEntityAssociationMixin)



```mermaid
 classDiagram
    class CaseToEntityAssociationMixin
      CaseToEntityAssociationMixin <|-- CaseToPhenotypicFeatureAssociation
      
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:CaseToEntityAssociationMixin |
| native | bican:CaseToEntityAssociationMixin |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: case to entity association mixin
description: An abstract association for use where the case is the subject
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: the case (e.g. patient) that has the property
    domain_of:
    - association
    range: case
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: case to entity association mixin
description: An abstract association for use where the case is the subject
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: the case (e.g. patient) that has the property
    domain_of:
    - association
    range: case
defining_slots:
- subject

```
</details>