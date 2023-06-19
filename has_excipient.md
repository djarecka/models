# Slot: has_excipient


_holds between a drug and a molecular entities in which the latter is a part of the former, and is a biologically inactive component_



URI: [bican:has_excipient](https://identifiers.org/brain-bican/vocab/has_excipient)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_excipient**








## Properties

* Range: [MolecularEntity](MolecularEntity.md)

* Multivalued: True





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
name: has excipient
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a drug and a molecular entities in which the latter is
  a part of the former, and is a biologically inactive component
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
mappings:
- WIKIDATA:Q902638
rank: 1000
is_a: has part
domain: drug
multivalued: true
inherited: true
alias: has_excipient
range: molecular entity

```
</details>