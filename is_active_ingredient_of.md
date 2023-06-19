# Slot: is_active_ingredient_of


_holds between a molecular entity and a drug, in which the former is a part of the latter, and is a biologically active component_



URI: [bican:is_active_ingredient_of](https://identifiers.org/brain-bican/vocab/is_active_ingredient_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [part_of](part_of.md)
                * **is_active_ingredient_of**








## Properties

* Range: [Drug](Drug.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: is active ingredient of
description: holds between a molecular entity and a drug, in which the former is a
  part of the latter, and is a biologically active component
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
mappings:
- RO:0002249
rank: 1000
is_a: part of
domain: molecular entity
multivalued: true
inherited: true
alias: is_active_ingredient_of
inverse: has active ingredient
range: drug

```
</details>