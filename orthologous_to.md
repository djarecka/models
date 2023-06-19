# Slot: orthologous_to


_a homology relationship between entities (typically genes) that diverged after a speciation event._



URI: [bican:orthologous_to](https://identifiers.org/brain-bican/vocab/orthologous_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [similar_to](similar_to.md)
            * [homologous_to](homologous_to.md)
                * **orthologous_to**








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
name: orthologous to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: a homology relationship between entities (typically genes) that diverged
  after a speciation event.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:HOM0000017
- WIKIDATA_PROPERTY:P684
rank: 1000
is_a: homologous to
domain: named thing
multivalued: true
inherited: true
alias: orthologous_to
symmetric: true
range: named thing

```
</details>