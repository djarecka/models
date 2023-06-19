# Slot: food_component_of


_holds between a one or more chemical entities present in food, irrespective of nutritional value (i.e. could also be a contaminant or additive)_



URI: [bican:food_component_of](https://identifiers.org/brain-bican/vocab/food_component_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [part_of](part_of.md)
                * **food_component_of**
                    * [nutrient_of](nutrient_of.md)








## Properties

* Range: [ChemicalEntity](ChemicalEntity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: food component of
description: holds between a one or more chemical entities present in food, irrespective
  of nutritional value (i.e. could also be a contaminant or additive)
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: part of
domain: chemical entity
multivalued: true
inherited: true
alias: food_component_of
inverse: has food component
range: chemical entity

```
</details>