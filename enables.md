# Slot: enables


_holds between a physical entity and a process, where the physical entity executes the process_



URI: [bican:enables](https://identifiers.org/brain-bican/vocab/enables)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [participates_in](participates_in.md)
            * **enables**








## Properties

* Range: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | prevents |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: enables
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: prevents
description: holds between a physical entity and a process, where the physical entity
  executes the process
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002327
rank: 1000
is_a: participates in
domain: physical entity
multivalued: true
inherited: true
alias: enables
inverse: enabled by
range: biological process or activity

```
</details>