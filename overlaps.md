# Slot: overlaps


_holds between entities that overlap in their extents (materials or processes)_



URI: [bican:overlaps](https://identifiers.org/brain-bican/vocab/overlaps)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **overlaps**
            * [has_part](has_part.md)
            * [part_of](part_of.md)








## Properties

* Range: [NamedThing](NamedThing.md)

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
name: overlaps
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between entities that overlap in their extents (materials or processes)
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002131
narrow_mappings:
- BSPO:0005001
- CHEMBL.MECHANISM:overlaps_with
- RO:0002100
- RO:0002102
- RO:0002433
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: overlaps
symmetric: true
range: named thing

```
</details>