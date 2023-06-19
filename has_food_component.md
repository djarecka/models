# Slot: has_food_component


_holds between food and one or more chemical entities composing it, irrespective of nutritional value (i.e. could also be a contaminant or additive)_



URI: [bican:has_food_component](https://identifiers.org/brain-bican/vocab/has_food_component)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * **has_food_component**
                    * [has_nutrient](has_nutrient.md)








## Properties

* Range: [ChemicalEntity](ChemicalEntity.md)

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
name: has food component
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between food and one or more chemical entities composing it, irrespective
  of nutritional value (i.e. could also be a contaminant or additive)
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: has part
domain: chemical entity
multivalued: true
inherited: true
alias: has_food_component
range: chemical entity

```
</details>