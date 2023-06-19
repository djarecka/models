# Slot: has_plasma_membrane_part


_Holds between a cell c and a protein complex or protein p if and only if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane has p as part._



URI: [bican:has_plasma_membrane_part](https://identifiers.org/brain-bican/vocab/has_plasma_membrane_part)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_plasma_membrane_part**








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
name: has plasma membrane part
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: Holds between a cell c and a protein complex or protein p if and only
  if that cell has as part a plasma_membrane[GO:0005886], and that plasma membrane
  has p as part.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002104
rank: 1000
is_a: has part
domain: named thing
multivalued: true
inherited: true
alias: has_plasma_membrane_part
range: named thing

```
</details>