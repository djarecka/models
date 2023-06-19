# Slot: quantifier_qualifier


_A measurable quantity for the object of the association_



URI: [bican:quantifier_qualifier](https://identifiers.org/brain-bican/vocab/quantifier_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * **quantifier_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phen... |  yes  |
[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and a gene expression site, possibly qualified ... |  yes  |
[GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
[VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  no  |







## Properties

* Range: [OntologyClass](OntologyClass.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: quantifier qualifier
description: A measurable quantity for the object of the association
from_schema: https://identifiers.org/brain-bican/kb-model
narrow_mappings:
- LOINC:analyzes
- LOINC:measured_by
- LOINC:property_of
- SEMMEDDB:MEASURES
- UMLS:measures
rank: 1000
is_a: association slot
domain: association
alias: quantifier_qualifier
domain_of:
- gene expression mixin
- gene to expression site association
range: ontology class

```
</details>