# Slot: exacerbates


_A relationship between an entity (e.g. a chemical, environmental exposure, or some form of genetic variation) and a condition (a phenotype or disease), where the presence of the entity worsens some or all aspects of the condition._



URI: [bican:exacerbates](https://identifiers.org/brain-bican/vocab/exacerbates)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **exacerbates**








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
name: exacerbates
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: A relationship between an entity (e.g. a chemical, environmental exposure,
  or some form of genetic variation) and a condition (a phenotype or disease), where
  the presence of the entity worsens some or all aspects of the condition.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0003309
broad_mappings:
- SEMMEDDB:COMPLICATES
rank: 1000
is_a: affects
domain: biological entity
multivalued: true
inherited: true
alias: exacerbates
range: disease or phenotypic feature

```
</details>