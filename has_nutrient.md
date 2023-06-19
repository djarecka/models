# Slot: has_nutrient


_one or more nutrients which are growth factors for a living organism_



URI: [bican:has_nutrient](https://identifiers.org/brain-bican/vocab/has_nutrient)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [has_part](has_part.md)
                * [has_food_component](has_food_component.md)
                    * **has_nutrient**








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
name: has nutrient
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: one or more nutrients which are growth factors for a living organism
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA:Q181394
rank: 1000
is_a: has food component
domain: chemical entity
multivalued: true
inherited: true
alias: has_nutrient
range: chemical entity

```
</details>