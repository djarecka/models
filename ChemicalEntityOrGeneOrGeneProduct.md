# Class: ChemicalEntityOrGeneOrGeneProduct


_A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities._





URI: [bican:ChemicalEntityOrGeneOrGeneProduct](https://identifiers.org/brain-bican/vocab/ChemicalEntityOrGeneOrGeneProduct)



```mermaid
 classDiagram
    class ChemicalEntityOrGeneOrGeneProduct
      ChemicalEntityOrGeneOrGeneProduct <|-- ChemicalEntity
      ChemicalEntityOrGeneOrGeneProduct <|-- RegulatoryRegion
      ChemicalEntityOrGeneOrGeneProduct <|-- AccessibleDnaRegion
      ChemicalEntityOrGeneOrGeneProduct <|-- TranscriptionFactorBindingSite
      ChemicalEntityOrGeneOrGeneProduct <|-- Gene
      ChemicalEntityOrGeneOrGeneProduct <|-- Polypeptide
      ChemicalEntityOrGeneOrGeneProduct <|-- ProteinDomain
      ChemicalEntityOrGeneOrGeneProduct <|-- ProteinFamily
      ChemicalEntityOrGeneOrGeneProduct <|-- GeneFamily
      
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemi... |
| [RegulatoryRegion](RegulatoryRegion.md) | A region (or regions) of the genome that contains known or putative regulator... |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | A region (or regions) of a chromatinized genome that has been measured to be ... |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | A region (or regions) of the genome that contains a region of DNA known or pr... |
| [Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |
| [Polypeptide](Polypeptide.md) | A polypeptide is a molecular entity characterized by availability in protein ... |
| [ProteinDomain](ProteinDomain.md) | A conserved part of protein sequence and (tertiary) structure that can evolve... |
| [ProteinFamily](ProteinFamily.md) |  |
| [GeneFamily](GeneFamily.md) | any grouping of multiple genes or gene products related by common descent |




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [subject](subject.md) | range | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | range | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | range | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | range | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject](subject.md) | range | [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:ChemicalEntityOrGeneOrGeneProduct |
| native | bican:ChemicalEntityOrGeneOrGeneProduct |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: chemical entity or gene or gene product
description: A union of chemical entities and children, and gene or gene product.
  This mixin is helpful to use when searching across chemical entities that must include
  genes and their children as chemical entities.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true

```
</details>

### Induced

<details>
```yaml
name: chemical entity or gene or gene product
description: A union of chemical entities and children, and gene or gene product.
  This mixin is helpful to use when searching across chemical entities that must include
  genes and their children as chemical entities.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true

```
</details>