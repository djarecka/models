# Slot: gene_fusion_with


_holds between two independent genes that have fused through  translocation, interstitial deletion, or chromosomal inversion to  form a new, hybrid gene. Fusion genes are often implicated in various neoplasms and cancers._



URI: [bican:gene_fusion_with](https://identifiers.org/brain-bican/vocab/gene_fusion_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * [genetically_interacts_with](genetically_interacts_with.md)
                * **gene_fusion_with**








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
name: gene_fusion_with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two independent genes that have fused through  translocation,
  interstitial deletion, or chromosomal inversion to  form a new, hybrid gene. Fusion
  genes are often implicated in various neoplasms and cancers.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: genetically interacts with
domain: gene
multivalued: true
inherited: true
alias: gene_fusion_with
symmetric: true
range: gene

```
</details>