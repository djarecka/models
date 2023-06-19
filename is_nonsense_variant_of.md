# Slot: is_nonsense_variant_of


_holds between a sequence variant and a gene, such the sequence variant results in a premature stop codon_



URI: [bican:is_nonsense_variant_of](https://identifiers.org/brain-bican/vocab/is_nonsense_variant_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [is_sequence_variant_of](is_sequence_variant_of.md)
            * **is_nonsense_variant_of**








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
name: is nonsense variant of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a sequence variant and a gene, such the sequence variant
  results in a premature stop codon
from_schema: https://identifiers.org/brain-bican/kb-model
broad_mappings:
- SO:0002054
rank: 1000
is_a: is sequence variant of
domain: sequence variant
multivalued: true
inherited: true
alias: is_nonsense_variant_of
range: genomic entity

```
</details>