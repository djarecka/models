# Slot: stage_qualifier


_stage during which gene or protein expression of takes place._



URI: [bican:stage_qualifier](https://identifiers.org/brain-bican/vocab/stage_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * **stage_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phen... |  no  |
[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and a gene expression site, possibly qualified ... |  yes  |
[GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
[VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  no  |







## Properties

* Range: [LifeStage](LifeStage.md)






## Examples

| Value |
| --- |
| UBERON:0000069 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: stage qualifier
description: stage during which gene or protein expression of takes place.
examples:
- value: UBERON:0000069
  description: larval stage
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: association slot
domain: association
alias: stage_qualifier
domain_of:
- gene expression mixin
- gene to expression site association
range: life stage

```
</details>