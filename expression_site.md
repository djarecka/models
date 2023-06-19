# Slot: expression_site


_location in which gene or protein expression takes place. May be cell, tissue, or organ._



URI: [bican:expression_site](https://identifiers.org/brain-bican/vocab/expression_site)




## Inheritance

* [association_slot](association_slot.md)
    * **expression_site**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phen... |  no  |
[GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
[VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  no  |







## Properties

* Range: [AnatomicalEntity](AnatomicalEntity.md)






## Examples

| Value |
| --- |
| UBERON:0002037 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: expression site
description: location in which gene or protein expression takes place. May be cell,
  tissue, or organ.
examples:
- value: UBERON:0002037
  description: cerebellum
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: association slot
domain: association
alias: expression_site
domain_of:
- gene expression mixin
range: anatomical entity

```
</details>