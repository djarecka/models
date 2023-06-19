# Slot: coexpressed_with


_holds between any two genes or gene products, in which both are generally expressed within a single defined experimental context._



URI: [bican:coexpressed_with](https://identifiers.org/brain-bican/vocab/coexpressed_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **coexpressed_with**








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
name: coexpressed with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between any two genes or gene products, in which both are generally
  expressed within a single defined experimental context.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: correlated with
domain: gene or gene product
multivalued: true
inherited: true
alias: coexpressed_with
symmetric: true
range: gene or gene product

```
</details>