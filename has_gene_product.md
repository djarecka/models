# Slot: has_gene_product


_holds between a gene and a transcribed and/or translated product generated from it_



URI: [bican:has_gene_product](https://identifiers.org/brain-bican/vocab/has_gene_product)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_gene_product**








## Properties

* Range: [GeneProductMixin](GeneProductMixin.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has gene product
description: holds between a gene and a transcribed and/or translated product generated
  from it
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002205
- WIKIDATA_PROPERTY:P688
- NCIT:gene_encodes_gene_product
close_mappings:
- PR:has_gene_template
narrow_mappings:
- NCIT:R178
rank: 1000
is_a: related to at instance level
domain: gene
multivalued: true
inherited: true
alias: has_gene_product
inverse: gene product of
range: gene product mixin

```
</details>