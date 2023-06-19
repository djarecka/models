# Slot: has_metabolite


_holds between two molecular entities in which the second one is derived from the first one as a product of metabolism_



URI: [bican:has_metabolite](https://identifiers.org/brain-bican/vocab/has_metabolite)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [derives_into](derives_into.md)
            * **has_metabolite**








## Properties

* Range: [MolecularEntity](MolecularEntity.md)

* Multivalued: True





## Comments

* The CHEBI ID represents a role rather than a predicate

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has metabolite
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two molecular entities in which the second one is derived
  from the first one as a product of metabolism
comments:
- The CHEBI ID represents a role rather than a predicate
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- CHEBI:25212
rank: 1000
is_a: derives into
domain: molecular entity
multivalued: true
inherited: true
alias: has_metabolite
range: molecular entity

```
</details>