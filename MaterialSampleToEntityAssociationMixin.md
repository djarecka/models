# Class: MaterialSampleToEntityAssociationMixin


_An association between a material sample and something._





URI: [bican:MaterialSampleToEntityAssociationMixin](https://identifiers.org/brain-bican/vocab/MaterialSampleToEntityAssociationMixin)



```mermaid
 classDiagram
    class MaterialSampleToEntityAssociationMixin
      MaterialSampleToEntityAssociationMixin <|-- MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
      
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | An association between a material sample and a disease or phenotype |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:MaterialSampleToEntityAssociationMixin |
| native | bican:MaterialSampleToEntityAssociationMixin |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: material sample to entity association mixin
description: An association between a material sample and something.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: the material sample being described
    domain_of:
    - association
    range: material sample
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: material sample to entity association mixin
description: An association between a material sample and something.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: the material sample being described
    domain_of:
    - association
    range: material sample
defining_slots:
- subject

```
</details>