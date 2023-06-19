# Class: CellLineToEntityAssociationMixin


_An relationship between a cell line and another entity_





URI: [bican:CellLineToEntityAssociationMixin](https://identifiers.org/brain-bican/vocab/CellLineToEntityAssociationMixin)



```mermaid
 classDiagram
    class CellLineToEntityAssociationMixin
      CellLineToEntityAssociationMixin <|-- CellLineToDiseaseOrPhenotypicFeatureAssociation
      
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | An relationship between a cell line and a disease or a phenotype, where the c... |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:CellLineToEntityAssociationMixin |
| native | bican:CellLineToEntityAssociationMixin |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: cell line to entity association mixin
description: An relationship between a cell line and another entity
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  subject:
    name: subject
    range: cell line
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: cell line to entity association mixin
description: An relationship between a cell line and another entity
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  subject:
    name: subject
    range: cell line
defining_slots:
- subject

```
</details>