# Slot: has_mode_of_inheritance


_Relates a disease or phenotypic feature to its observed genetic segregation and assumed associated underlying DNA manifestation (i.e. autosomal, sex or mitochondrial chromosome)._



URI: [bican:has_mode_of_inheritance](https://identifiers.org/brain-bican/vocab/has_mode_of_inheritance)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_manifestation](has_manifestation.md)
            * **has_mode_of_inheritance**








## Properties

* Range: [GeneticInheritance](GeneticInheritance.md)

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
name: has mode of inheritance
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: Relates a disease or phenotypic feature to its observed genetic segregation
  and assumed associated underlying DNA manifestation (i.e. autosomal, sex or mitochondrial
  chromosome).
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: has manifestation
domain: disease or phenotypic feature
multivalued: true
inherited: true
alias: has_mode_of_inheritance
range: genetic inheritance

```
</details>