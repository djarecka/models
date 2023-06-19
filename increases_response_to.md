# Slot: increases_response_to


_holds between two chemical entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other_



URI: [bican:increases_response_to](https://identifiers.org/brain-bican/vocab/increases_response_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * [affects_response_to](affects_response_to.md)
                * **increases_response_to**








## Properties

* Range: [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | decreases response to |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: increases response to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: decreases response to
description: holds between two chemical entities where the action or effect of one
  increases the susceptibility of a biological entity or system (e.g. an organism,
  cell, cellular component, macromolecular machine mixin, biological or pathological
  process) to the other
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- CTD:increases_response_to
rank: 1000
is_a: affects response to
domain: chemical entity or gene or gene product
multivalued: true
inherited: true
alias: increases_response_to
range: chemical entity or gene or gene product

```
</details>