# Class: ChemicalEntityOrProteinOrPolypeptide


_A union of chemical entities and children, and protein and polypeptide. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities._





URI: [bican:ChemicalEntityOrProteinOrPolypeptide](https://identifiers.org/brain-bican/vocab/ChemicalEntityOrProteinOrPolypeptide)



```mermaid
 classDiagram
    class ChemicalEntityOrProteinOrPolypeptide
      ChemicalEntityOrProteinOrPolypeptide <|-- ChemicalEntity
      ChemicalEntityOrProteinOrPolypeptide <|-- Polypeptide
      
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemi... |
| [Polypeptide](Polypeptide.md) | A polypeptide is a molecular entity characterized by availability in protein ... |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:ChemicalEntityOrProteinOrPolypeptide |
| native | bican:ChemicalEntityOrProteinOrPolypeptide |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: chemical entity or protein or polypeptide
description: A union of chemical entities and children, and protein and polypeptide.
  This mixin is helpful to use when searching across chemical entities that must include
  genes and their children as chemical entities.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true

```
</details>

### Induced

<details>
```yaml
name: chemical entity or protein or polypeptide
description: A union of chemical entities and children, and protein and polypeptide.
  This mixin is helpful to use when searching across chemical entities that must include
  genes and their children as chemical entities.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true

```
</details>