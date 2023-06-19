# Slot: gene_associated_with_condition


_holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with_



URI: [bican:gene_associated_with_condition](https://identifiers.org/brain-bican/vocab/gene_associated_with_condition)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [genetically_associated_with](genetically_associated_with.md)
                * **gene_associated_with_condition**








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
name: gene associated with condition
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a gene and a disease or phenotypic feature that the gene
  or its alleles/products may influence, contribute to, or correlate with
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
narrow_mappings:
- NCIT:R38
- NCIT:R175
- NCIT:R48
broad_mappings:
- GENO:0000840
- GENO:0000841
rank: 1000
is_a: genetically associated with
domain: disease or phenotypic feature
multivalued: true
inherited: true
alias: gene_associated_with_condition
range: gene

```
</details>