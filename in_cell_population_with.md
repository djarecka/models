# Slot: in_cell_population_with


_holds between two genes or gene products that are expressed in the same cell type or population_



URI: [bican:in_cell_population_with](https://identifiers.org/brain-bican/vocab/in_cell_population_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [coexists_with](coexists_with.md)
            * **in_cell_population_with**








## Properties

* Range: [GeneOrGeneProduct](GeneOrGeneProduct.md)

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
name: in cell population with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two genes or gene products that are expressed in the same
  cell type or population
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: coexists with
domain: gene or gene product
multivalued: true
inherited: true
alias: in_cell_population_with
symmetric: true
range: gene or gene product

```
</details>