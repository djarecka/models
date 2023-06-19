# Slot: genetic_neighborhood_of


_holds between two genes located nearby one another on a chromosome. _



URI: [bican:genetic_neighborhood_of](https://identifiers.org/brain-bican/vocab/genetic_neighborhood_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * [genetically_interacts_with](genetically_interacts_with.md)
                * **genetic_neighborhood_of**








## Properties

* Range: [Gene](Gene.md)

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
name: genetic_neighborhood_of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: 'holds between two genes located nearby one another on a chromosome. '
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: genetically interacts with
domain: gene
multivalued: true
inherited: true
alias: genetic_neighborhood_of
symmetric: true
range: gene

```
</details>