# Slot: decreases_response_to


_holds between two chemical entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine mixin, biological or pathological process) to the other_



URI: [bican:decreases_response_to](https://identifiers.org/brain-bican/vocab/decreases_response_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * [affects_response_to](affects_response_to.md)
                * **decreases_response_to**








## Properties

* Range: [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | increases response to |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: decreases response to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: increases response to
description: holds between two chemical entities where the action or effect of one
  decreases the susceptibility of a biological entity or system (e.g. an organism,
  cell, cellular component, macromolecular machine mixin, biological or pathological
  process) to the other
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- CTD:decreases_response_to
narrow_mappings:
- CTD:decreases_response_to_substance
rank: 1000
is_a: affects response to
domain: chemical entity or gene or gene product
multivalued: true
inherited: true
alias: decreases_response_to
range: chemical entity or gene or gene product

```
</details>