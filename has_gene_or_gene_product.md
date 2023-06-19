# Slot: has_gene_or_gene_product


_connects an entity with one or more gene or gene products_



URI: [bican:has_gene_or_gene_product](https://identifiers.org/brain-bican/vocab/has_gene_or_gene_product)




## Inheritance

* [node_property](node_property.md)
    * **has_gene_or_gene_product**
        * [has_gene](has_gene.md)





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GeneGroupingMixin](GeneGroupingMixin.md) | any grouping of multiple genes or gene products |  no  |
[ProteinDomain](ProteinDomain.md) | A conserved part of protein sequence and (tertiary) structure that can evolve... |  no  |
[ProteinFamily](ProteinFamily.md) |  |  no  |
[GeneFamily](GeneFamily.md) | any grouping of multiple genes or gene products related by common descent |  no  |
[GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic backg... |  no  |
[DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | drug to gene interaction exposure is a drug exposure is where the interaction... |  no  |







## Properties

* Range: [Gene](Gene.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has gene or gene product
description: connects an entity with one or more gene or gene products
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: node property
domain: named thing
multivalued: true
alias: has_gene_or_gene_product
domain_of:
- gene grouping mixin
range: gene

```
</details>