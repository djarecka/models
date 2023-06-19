# Slot: homologous_to


_holds between two biological entities that have common evolutionary origin_



URI: [bican:homologous_to](https://identifiers.org/brain-bican/vocab/homologous_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [similar_to](similar_to.md)
            * **homologous_to**
                * [paralogous_to](paralogous_to.md)
                * [orthologous_to](orthologous_to.md)
                * [xenologous_to](xenologous_to.md)








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True



## Aliases


* in homology relationship with



## Comments

* typically used to describe homology relationships between genes or gene products

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
name: homologous to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two biological entities that have common evolutionary origin
comments:
- typically used to describe homology relationships between genes or gene products
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- in homology relationship with
exact_mappings:
- RO:HOM0000001
- SIO:010302
narrow_mappings:
- UBERON_CORE:sexually_homologous_to
rank: 1000
is_a: similar to
domain: named thing
multivalued: true
inherited: true
alias: homologous_to
symmetric: true
range: named thing

```
</details>