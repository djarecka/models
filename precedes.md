# Slot: precedes


_holds between two processes, where one completes before the other begins_



URI: [bican:precedes](https://identifiers.org/brain-bican/vocab/precedes)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [temporally_related_to](temporally_related_to.md)
            * **precedes**








## Properties

* Range: [Occurrent](Occurrent.md)

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
name: precedes
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two processes, where one completes before the other begins
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- BFO:0000063
- SEMMEDDB:PRECEDES
- SNOMED:occurs_before
close_mappings:
- RO:0002263
- RO:0002264
narrow_mappings:
- FMA:transforms_into
- RO:0002090
- RO:0002411
- RO:0002412
broad_mappings:
- WIKIDATA_PROPERTY:P156
rank: 1000
is_a: temporally related to
domain: occurrent
multivalued: true
inherited: true
alias: precedes
inverse: preceded by
range: occurrent

```
</details>