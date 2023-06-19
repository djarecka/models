# Slot: similar_to


_holds between an entity and some other entity with similar features._



URI: [bican:similar_to](https://identifiers.org/brain-bican/vocab/similar_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **similar_to**
            * [homologous_to](homologous_to.md)
            * [chemically_similar_to](chemically_similar_to.md)








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
name: similar to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between an entity and some other entity with similar features.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:HOM0000000
- SO:similar_to
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: similar_to
symmetric: true
range: named thing

```
</details>