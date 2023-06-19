# Slot: has_side_effect


_An unintended, but predictable, secondary effect shown to be correlated with a therapeutic agent, drug or treatment. Side effects happen at normal, recommended doses or treatments, and are unrelated to the intended purpose of  the medication._



URI: [bican:has_side_effect](https://identifiers.org/brain-bican/vocab/has_side_effect)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **has_side_effect**








## Properties

* Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

* Multivalued: True



## Aliases


* adverse drug reaction



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
name: has side effect
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: An unintended, but predictable, secondary effect shown to be correlated
  with a therapeutic agent, drug or treatment. Side effects happen at normal, recommended
  doses or treatments, and are unrelated to the intended purpose of  the medication.
notes:
- Side effects are listed on drug labels. There can be positive side effects, while
  adverse events are always negative. Aeolus, Sider are both resources that provide
  side effects.
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- adverse drug reaction
exact_mappings:
- NCIT:C2861
rank: 1000
is_a: affects
domain: chemical or drug or treatment
multivalued: true
inherited: true
alias: has_side_effect
range: disease or phenotypic feature

```
</details>