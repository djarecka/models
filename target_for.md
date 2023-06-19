# Slot: target_for


_A gene is a target of a disease when its products are druggable and when a drug interaction with the gene product could have a therapeutic effect_



URI: [bican:target_for](https://identifiers.org/brain-bican/vocab/target_for)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **target_for**








## Properties

* Range: [Disease](Disease.md)

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
name: target for
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: A gene is a target of a disease when its products are druggable and when
  a drug interaction with the gene product could have a therapeutic effect
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: related to at instance level
domain: gene
multivalued: true
inherited: true
alias: target_for
range: disease

```
</details>