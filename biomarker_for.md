# Slot: biomarker_for


_holds between a measurable chemical entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._



URI: [bican:biomarker_for](https://identifiers.org/brain-bican/vocab/biomarker_for)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **biomarker_for**








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
name: biomarker for
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a measurable chemical entity and a disease or phenotypic
  feature, where the entity is used as an indicator of the presence or state of the
  disease or feature.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- NCIT:R39
narrow_mappings:
- NCIT:R47
- NCIT:genetic_biomarker_related_to
- NCIT:is_molecular_abnormality_of_disease
- orphanet:465410
broad_mappings:
- RO:0002607
rank: 1000
is_a: correlated with
domain: chemical entity or gene or gene product
multivalued: true
inherited: true
alias: biomarker_for
range: disease or phenotypic feature

```
</details>