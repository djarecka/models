# Slot: gene_product_of


_definition x has gene product of y if and only if y is a gene (SO:0000704) that participates in some gene expression process (GO:0010467) where the output of thatf process is either y or something that is ribosomally translated from x_



URI: [bican:gene_product_of](https://identifiers.org/brain-bican/vocab/gene_product_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **gene_product_of**








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
name: gene product of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: definition x has gene product of y if and only if y is a gene (SO:0000704)
  that participates in some gene expression process (GO:0010467) where the output
  of thatf process is either y or something that is ribosomally translated from x
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002204
rank: 1000
is_a: related to at instance level
domain: gene product mixin
multivalued: true
inherited: true
alias: gene_product_of
inverse: has gene product
range: gene

```
</details>