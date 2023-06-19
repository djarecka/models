# Class: GeneToEntityAssociationMixin



URI: [bican:GeneToEntityAssociationMixin](https://identifiers.org/brain-bican/vocab/GeneToEntityAssociationMixin)



```mermaid
 classDiagram
    class GeneToEntityAssociationMixin
      GeneToEntityAssociationMixin <|-- GeneToPathwayAssociation
      GeneToEntityAssociationMixin <|-- GeneToDiseaseOrPhenotypicFeatureAssociation
      GeneToEntityAssociationMixin <|-- GeneToPhenotypicFeatureAssociation
      GeneToEntityAssociationMixin <|-- GeneToDiseaseAssociation
      GeneToEntityAssociationMixin <|-- CausalGeneToDiseaseAssociation
      GeneToEntityAssociationMixin <|-- CorrelatedGeneToDiseaseAssociation
      GeneToEntityAssociationMixin <|-- DruggableGeneToDiseaseAssociation
      
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | An interaction between a gene or gene product and a biological process or pat... |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) |  |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) |  |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |  |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) |  |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) |  |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) |  |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:GeneToEntityAssociationMixin |
| native | bican:GeneToEntityAssociationMixin |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene to entity association mixin
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: gene that is the subject of the association
    range: gene or gene product
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: gene to entity association mixin
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  subject:
    name: subject
    description: gene that is the subject of the association
    range: gene or gene product
defining_slots:
- subject

```
</details>