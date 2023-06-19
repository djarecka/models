# Slot: diagnoses


_a relationship that identifies the nature of (an illness or other problem) by examination  of the symptoms._



URI: [bican:diagnoses](https://identifiers.org/brain-bican/vocab/diagnoses)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **diagnoses**








## Properties

* Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

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
name: diagnoses
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: a relationship that identifies the nature of (an illness or other problem)
  by examination  of the symptoms.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- DrugCentral:5271
- SEMMEDDB:DIAGNOSES
close_mappings:
- NCIT:C15220
- SIO:001331
rank: 1000
is_a: related to at instance level
domain: diagnostic aid
multivalued: true
inherited: true
alias: diagnoses
range: disease or phenotypic feature

```
</details>