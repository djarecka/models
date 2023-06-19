# Slot: paralogous_to


_a homology relationship that holds between entities (typically genes) that diverged after a duplication event._



URI: [bican:paralogous_to](https://identifiers.org/brain-bican/vocab/paralogous_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [similar_to](similar_to.md)
            * [homologous_to](homologous_to.md)
                * **paralogous_to**








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
name: paralogous to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: a homology relationship that holds between entities (typically genes)
  that diverged after a duplication event.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:HOM0000011
rank: 1000
is_a: homologous to
domain: named thing
multivalued: true
inherited: true
alias: paralogous_to
symmetric: true
range: named thing

```
</details>