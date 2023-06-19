# Slot: has_active_ingredient


_holds between a drug and a molecular entity in which the latter is a part of the former, and is a biologically active component_



URI: [bican:has_active_ingredient](https://identifiers.org/brain-bican/vocab/has_active_ingredient)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_active_ingredient**








## Properties

* Range: [MolecularEntity](MolecularEntity.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | is excipient of |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has active ingredient
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: is excipient of
description: holds between a drug and a molecular entity in which the latter is a
  part of the former, and is a biologically active component
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
mappings:
- RO:0002248
rank: 1000
is_a: has part
domain: drug
multivalued: true
inherited: true
alias: has_active_ingredient
inverse: is active ingredient of
range: molecular entity

```
</details>