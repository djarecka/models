# Class: MacromolecularMachineMixin


_A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this._





URI: [bican:MacromolecularMachineMixin](https://identifiers.org/brain-bican/vocab/MacromolecularMachineMixin)



```mermaid
 classDiagram
    class MacromolecularMachineMixin
      MacromolecularMachineMixin <|-- GeneOrGeneProduct
      MacromolecularMachineMixin <|-- MacromolecularComplex
      
      MacromolecularMachineMixin : name
        
      
```





## Inheritance
* **MacromolecularMachineMixin**
    * [GeneOrGeneProduct](GeneOrGeneProduct.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 0..1 <br/> [SymbolType](SymbolType.md) | genes are typically designated by a short symbol and a full name | direct |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [MacromolecularComplex](MacromolecularComplex.md) | A stable assembly of two or more macromolecules, i |




## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MolecularActivity](MolecularActivity.md) | [enabled_by](enabled_by.md) | range | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [catalyst_qualifier](catalyst_qualifier.md) | range | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject](subject.md) | range | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject](subject.md) | domain | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject](subject.md) | range | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject](subject.md) | domain | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject](subject.md) | range | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject](subject.md) | domain | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject](subject.md) | range | [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:MacromolecularMachineMixin |
| native | bican:MacromolecularMachineMixin |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: macromolecular machine mixin
description: A union of gene locus, gene product, and macromolecular complex. These
  are the basic units of function in a cell. They either carry out individual biological
  activities, or they encode molecules which do this.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slots:
- name
slot_usage:
  name:
    name: name
    description: genes are typically designated by a short symbol and a full name.
      We map the symbol to the default display name and use an additional slot for
      full name
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: symbol type

```
</details>

### Induced

<details>
```yaml
name: macromolecular machine mixin
description: A union of gene locus, gene product, and macromolecular complex. These
  are the basic units of function in a cell. They either carry out individual biological
  activities, or they encode molecules which do this.
from_schema: https://identifiers.org/brain-bican/kb-model
mixin: true
slot_usage:
  name:
    name: name
    description: genes are typically designated by a short symbol and a full name.
      We map the symbol to the default display name and use an additional slot for
      full name
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: symbol type
attributes:
  name:
    name: name
    description: genes are typically designated by a short symbol and a full name.
      We map the symbol to the default display name and use an additional slot for
      full name
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    domain: entity
    slot_uri: rdfs:label
    alias: name
    owner: macromolecular machine mixin
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: symbol type

```
</details>