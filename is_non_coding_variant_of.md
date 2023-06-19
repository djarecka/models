# Slot: is_non_coding_variant_of


_holds between a sequence variant and a gene, where the variant does not affect the coding sequence_



URI: [bican:is_non_coding_variant_of](https://identifiers.org/brain-bican/vocab/is_non_coding_variant_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [is_sequence_variant_of](is_sequence_variant_of.md)
            * **is_non_coding_variant_of**








## Properties

* Range: [GenomicEntity](GenomicEntity.md)

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
name: is non coding variant of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a sequence variant and a gene, where the variant does not
  affect the coding sequence
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: is sequence variant of
domain: sequence variant
multivalued: true
inherited: true
alias: is_non_coding_variant_of
range: genomic entity

```
</details>