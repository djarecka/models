# Slot: in_pathway_with


_holds between two genes or gene products that are part of in the same biological pathway_



URI: [bican:in_pathway_with](https://identifiers.org/brain-bican/vocab/in_pathway_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [coexists_with](coexists_with.md)
            * **in_pathway_with**








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
name: in pathway with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two genes or gene products that are part of in the same
  biological pathway
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
related_mappings:
- SIO:010532
rank: 1000
is_a: coexists with
domain: gene or gene product
multivalued: true
inherited: true
alias: in_pathway_with
symmetric: true
range: gene or gene product

```
</details>