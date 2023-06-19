# Slot: in_complex_with


_holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex_



URI: [bican:in_complex_with](https://identifiers.org/brain-bican/vocab/in_complex_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [coexists_with](coexists_with.md)
            * **in_complex_with**








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
name: in complex with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two genes or gene products that are part of (or code for
  products that are part of) in the same macromolecular complex
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
related_mappings:
- SIO:010497
broad_mappings:
- SIO:010285
rank: 1000
is_a: coexists with
domain: gene or gene product
multivalued: true
inherited: true
alias: in_complex_with
symmetric: true
range: gene or gene product

```
</details>