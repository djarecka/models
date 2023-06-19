# Slot: has_sequence_location


_holds between two nucleic acid entities when the subject can be localized in sequence coordinates on the object. For example, between an exon and a chromosome/contig._



URI: [bican:has_sequence_location](https://identifiers.org/brain-bican/vocab/has_sequence_location)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_sequence_location**








## Properties

* Range: [NucleicAcidEntity](NucleicAcidEntity.md)

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
name: has sequence location
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two nucleic acid entities when the subject can be localized
  in sequence coordinates on the object. For example, between an exon and a chromosome/contig.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- faldo:location
rank: 1000
is_a: related to at instance level
domain: nucleic acid entity
multivalued: true
inherited: true
alias: has_sequence_location
range: nucleic acid entity

```
</details>