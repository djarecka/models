# Slot: condition_associated_with_gene


_holds between a gene and a disease or phenotypic feature that may be influenced, contribute to, or be correlated with the gene or its alleles/products_



URI: [bican:condition_associated_with_gene](https://identifiers.org/brain-bican/vocab/condition_associated_with_gene)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [genetically_associated_with](genetically_associated_with.md)
                * **condition_associated_with_gene**








## Properties

* Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

* Multivalued: True



## Aliases


* disease associated with gene



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: condition associated with gene
description: holds between a gene and a disease or phenotypic feature that may be
  influenced, contribute to, or be correlated with the gene or its alleles/products
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- disease associated with gene
narrow_mappings:
- NCIT:R176
rank: 1000
is_a: genetically associated with
domain: gene
multivalued: true
inherited: true
alias: condition_associated_with_gene
inverse: gene associated with condition
range: disease or phenotypic feature

```
</details>