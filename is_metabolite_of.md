# Slot: is_metabolite_of


_holds between two molecular entities in which the first one is derived from the second one as a product of metabolism_



URI: [bican:is_metabolite_of](https://identifiers.org/brain-bican/vocab/is_metabolite_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [derives_from](derives_from.md)
            * **is_metabolite_of**








## Properties

* Range: [MolecularEntity](MolecularEntity.md)

* Multivalued: True





## Comments

* The CHEBI ID represents a role rather than a predicate

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: is metabolite of
description: holds between two molecular entities in which the first one is derived
  from the second one as a product of metabolism
comments:
- The CHEBI ID represents a role rather than a predicate
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- CHEBI:25212
rank: 1000
is_a: derives from
domain: molecular entity
multivalued: true
inherited: true
alias: is_metabolite_of
inverse: has metabolite
range: molecular entity

```
</details>