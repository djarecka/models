# Slot: genetically_interacts_with


_holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality._



URI: [bican:genetically_interacts_with](https://identifiers.org/brain-bican/vocab/genetically_interacts_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * **genetically_interacts_with**
                * [gene_fusion_with](gene_fusion_with.md)
                * [genetic_neighborhood_of](genetic_neighborhood_of.md)








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
name: genetically interacts with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two genes whose phenotypic effects are dependent on each
  other in some way - such that their combined phenotypic effects are the result of
  some interaction between the activity of their gene products. Examples include epistasis
  and synthetic lethality.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002435
rank: 1000
is_a: interacts with
domain: gene
multivalued: true
inherited: true
alias: genetically_interacts_with
symmetric: true
range: gene

```
</details>