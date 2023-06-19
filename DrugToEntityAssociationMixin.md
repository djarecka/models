# Class: DrugToEntityAssociationMixin


_An interaction between a drug and another entity_





URI: [bican:DrugToEntityAssociationMixin](https://identifiers.org/brain-bican/vocab/DrugToEntityAssociationMixin)



```mermaid
 classDiagram
    class DrugToEntityAssociationMixin
      ChemicalEntityToEntityAssociationMixin <|-- DrugToEntityAssociationMixin
      

      DrugToEntityAssociationMixin <|-- DrugToGeneAssociation
      
      
      
```





## Inheritance
* [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md)
    * **DrugToEntityAssociationMixin**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | An interaction between a drug and a gene or gene product |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:DrugToEntityAssociationMixin |
| native | bican:DrugToEntityAssociationMixin |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: drug to entity association mixin
description: An interaction between a drug and another entity
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: chemical entity to entity association mixin
mixin: true
slot_usage:
  subject:
    name: subject
    description: the drug that is an interactor
    domain_of:
    - association
    range: drug
defining_slots:
- subject

```
</details>

### Induced

<details>
```yaml
name: drug to entity association mixin
description: An interaction between a drug and another entity
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: chemical entity to entity association mixin
mixin: true
slot_usage:
  subject:
    name: subject
    description: the drug that is an interactor
    domain_of:
    - association
    range: drug
defining_slots:
- subject

```
</details>