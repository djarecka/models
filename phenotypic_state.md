# Slot: phenotypic_state


_in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX._



URI: [bican:phenotypic_state](https://identifiers.org/brain-bican/vocab/phenotypic_state)




## Inheritance

* [association_slot](association_slot.md)
    * **phenotypic_state**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phen... |  no  |
[GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
[VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  no  |







## Properties

* Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: phenotypic state
description: in experiments (e.g. gene expression) assaying diseased or unhealthy
  tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues,
  use XXX.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: association slot
domain: association
alias: phenotypic_state
domain_of:
- gene expression mixin
range: disease or phenotypic feature

```
</details>