# Slot: is_frameshift_variant_of


_holds between a sequence variant and a gene, such the sequence variant causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three._



URI: [bican:is_frameshift_variant_of](https://identifiers.org/brain-bican/vocab/is_frameshift_variant_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [is_sequence_variant_of](is_sequence_variant_of.md)
            * **is_frameshift_variant_of**








## Properties

* Range: [GenomicEntity](GenomicEntity.md)

* Multivalued: True



## Aliases


* frameshift variant
* start lost
* stop lost



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
name: is frameshift variant of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a sequence variant and a gene, such the sequence variant
  causes a disruption of the translational reading frame, because the number of nucleotides
  inserted or deleted is not a multiple of three.
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- frameshift variant
- start lost
- stop lost
exact_mappings:
- SO:0001589
rank: 1000
is_a: is sequence variant of
domain: sequence variant
multivalued: true
inherited: true
alias: is_frameshift_variant_of
range: genomic entity

```
</details>