# Slot: has_gene


_connects an entity associated with one or more genes_



URI: [bican:has_gene](https://identifiers.org/brain-bican/vocab/has_gene)




## Inheritance

* [node_property](node_property.md)
    * [has_gene_or_gene_product](has_gene_or_gene_product.md)
        * **has_gene**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibi... |  yes  |
[Snv](Snv.md) | SNVs are single nucleotide positions in genomic DNA at which different sequen... |  no  |







## Properties

* Range: [Gene](Gene.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has gene
description: connects an entity associated with one or more genes
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: has gene or gene product
domain: named thing
multivalued: true
alias: has_gene
domain_of:
- sequence variant
range: gene

```
</details>