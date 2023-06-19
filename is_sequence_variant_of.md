# Slot: is_sequence_variant_of


_holds between a sequence variant and a nucleic acid entity_



URI: [bican:is_sequence_variant_of](https://identifiers.org/brain-bican/vocab/is_sequence_variant_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **is_sequence_variant_of**
            * [is_missense_variant_of](is_missense_variant_of.md)
            * [is_synonymous_variant_of](is_synonymous_variant_of.md)
            * [is_nonsense_variant_of](is_nonsense_variant_of.md)
            * [is_frameshift_variant_of](is_frameshift_variant_of.md)
            * [is_splice_site_variant_of](is_splice_site_variant_of.md)
            * [is_nearby_variant_of](is_nearby_variant_of.md)
            * [is_non_coding_variant_of](is_non_coding_variant_of.md)








## Properties

* Range: [GenomicEntity](GenomicEntity.md)

* Multivalued: True



## Aliases


* gene product sequence variation encoded by gene mutant
* allelic variant of
* gene product variant of gene product



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
name: is sequence variant of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a sequence variant and a nucleic acid entity
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- gene product sequence variation encoded by gene mutant
- allelic variant of
- gene product variant of gene product
narrow_mappings:
- WIKIDATA:P3433
rank: 1000
is_a: related to at instance level
domain: sequence variant
multivalued: true
inherited: true
alias: is_sequence_variant_of
range: genomic entity

```
</details>