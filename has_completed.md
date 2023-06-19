# Slot: has_completed


_holds between an entity and a process that the entity is capable of and has completed_



URI: [bican:has_completed](https://identifiers.org/brain-bican/vocab/has_completed)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_completed**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | has not completed |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has completed
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: has not completed
description: holds between an entity and a process that the entity is capable of and
  has completed
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- CL:has_completed
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: has_completed
range: named thing

```
</details>