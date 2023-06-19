# Slot: contraindicated_for


_Holds between a drug and a disease or phenotype, such that a person with that disease should not be treated with the drug._



URI: [bican:contraindicated_for](https://identifiers.org/brain-bican/vocab/contraindicated_for)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **contraindicated_for**








## Properties

* Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | treats |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: contraindicated for
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: treats
description: Holds between a drug and a disease or phenotype, such that a person with
  that disease should not be treated with the drug.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- NCIT:C37933
rank: 1000
is_a: related to at instance level
domain: drug
multivalued: true
inherited: true
alias: contraindicated_for
range: disease or phenotypic feature

```
</details>