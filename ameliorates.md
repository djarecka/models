# Slot: ameliorates


_A relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure, clinical intervention) and a condition (a phenotype or disease), where the presence of the entity reduces or eliminates some or all aspects of the condition._



URI: [bican:ameliorates](https://identifiers.org/brain-bican/vocab/ameliorates)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **ameliorates**
                * [treats](treats.md)








## Properties

* Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | exacerbates |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: ameliorates
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: exacerbates
description: A relationship between an entity (e.g. a genotype, genetic variation,
  chemical, or environmental exposure, clinical intervention) and a condition (a phenotype
  or disease), where the presence of the entity reduces or eliminates some or all
  aspects of the condition.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0003307
rank: 1000
is_a: affects
domain: named thing
multivalued: true
inherited: true
alias: ameliorates
range: disease or phenotypic feature

```
</details>