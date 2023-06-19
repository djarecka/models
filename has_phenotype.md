# Slot: has_phenotype


_holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). In SNOMEDCT, disorders with keyword 'characterized by' should translate into this predicate._



URI: [bican:has_phenotype](https://identifiers.org/brain-bican/vocab/has_phenotype)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_phenotype**








## Properties

* Range: [PhenotypicFeature](PhenotypicFeature.md)

* Multivalued: True



## Aliases


* disease presents symptom



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
name: has phenotype
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a biological entity and a phenotype, where a phenotype
  is construed broadly as any kind of quality of an organism part, a collection of
  these qualities, or a change in quality or qualities (e.g. abnormally increased
  temperature). In SNOMEDCT, disorders with keyword 'characterized by' should translate
  into this predicate.
notes:
- check the range
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- disease presents symptom
exact_mappings:
- RO:0002200
narrow_mappings:
- NCIT:R89
- DOID-PROPERTY:has_symptom
- RO:0004022
broad_mappings:
- NCIT:R115
- NCIT:R108
rank: 1000
is_a: related to at instance level
domain: biological entity
multivalued: true
inherited: true
alias: has_phenotype
range: phenotypic feature

```
</details>