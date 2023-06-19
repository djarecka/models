# Class: EntityToDiseaseOrPhenotypicFeatureAssociationMixin



URI: [bican:EntityToDiseaseOrPhenotypicFeatureAssociationMixin](https://identifiers.org/brain-bican/vocab/EntityToDiseaseOrPhenotypicFeatureAssociationMixin)



```mermaid
 classDiagram
    class EntityToDiseaseOrPhenotypicFeatureAssociationMixin
      EntityToDiseaseOrPhenotypicFeatureAssociationMixin <|-- CellLineToDiseaseOrPhenotypicFeatureAssociation
      EntityToDiseaseOrPhenotypicFeatureAssociationMixin <|-- ChemicalToDiseaseOrPhenotypicFeatureAssociation
      EntityToDiseaseOrPhenotypicFeatureAssociationMixin <|-- ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation
      EntityToDiseaseOrPhenotypicFeatureAssociationMixin <|-- ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation
      EntityToDiseaseOrPhenotypicFeatureAssociationMixin <|-- MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
      
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | An relationship between a cell line and a disease or a phenotype, where the c... |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | An interaction between a chemical entity and a phenotype or disease, where th... |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | An association between a material sample and a disease or phenotype |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:EntityToDiseaseOrPhenotypicFeatureAssociationMixin |
| native | bican:EntityToDiseaseOrPhenotypicFeatureAssociationMixin |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: entity to disease or phenotypic feature association mixin
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  object:
    name: object
    description: disease or phenotype
    examples:
    - value: MONDO:0017314
      description: Ehlers-Danlos syndrome, vascular type
    - value: MP:0013229
      description: abnormal brain ventricle size
    domain_of:
    - association
    range: disease or phenotypic feature
defining_slots:
- object

```
</details>

### Induced

<details>
```yaml
name: entity to disease or phenotypic feature association mixin
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  object:
    name: object
    description: disease or phenotype
    examples:
    - value: MONDO:0017314
      description: Ehlers-Danlos syndrome, vascular type
    - value: MP:0013229
      description: abnormal brain ventricle size
    domain_of:
    - association
    range: disease or phenotypic feature
defining_slots:
- object

```
</details>