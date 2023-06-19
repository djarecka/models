# Slot: temporally_related_to


_holds between two entities with a temporal relationship_



URI: [bican:temporally_related_to](https://identifiers.org/brain-bican/vocab/temporally_related_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **temporally_related_to**
            * [precedes](precedes.md)
            * [preceded_by](preceded_by.md)








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
name: temporally related to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two entities with a temporal relationship
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SNOMED:temporally_related_to
narrow_mappings:
- RO:0002082
- RO:0002083
- RO:0002092
- RO:0002093
- RO:0002223
- RO:0002224
- RO:0002229
- RO:0002230
- RO:0002488
- RO:0002489
- RO:0002492
- RO:0002493
- RO:0002496
- RO:0002497
rank: 1000
is_a: related to at instance level
domain: occurrent
multivalued: true
inherited: true
alias: temporally_related_to
symmetric: true
range: occurrent

```
</details>