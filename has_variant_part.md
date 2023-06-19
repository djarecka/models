# Slot: has_variant_part


_holds between a nucleic acid entity and a nucleic acid entity that is a sub-component of it_



URI: [bican:has_variant_part](https://identifiers.org/brain-bican/vocab/has_variant_part)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_variant_part**








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
name: has variant part
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a nucleic acid entity and a nucleic acid entity that is
  a sub-component of it
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- GENO:0000382
rank: 1000
is_a: has part
domain: named thing
multivalued: true
inherited: true
alias: has_variant_part
range: named thing

```
</details>