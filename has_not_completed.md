# Slot: has_not_completed


_holds between an entity and a process that the entity is capable of, but has not completed_



URI: [bican:has_not_completed](https://identifiers.org/brain-bican/vocab/has_not_completed)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_not_completed**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| opposite_of | has completed || canonical_predicate | True |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has not completed
annotations:
  opposite_of:
    tag: opposite_of
    value: has completed
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between an entity and a process that the entity is capable of,
  but has not completed
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- CL:has_not_completed
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: has_not_completed
range: named thing

```
</details>