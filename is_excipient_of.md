# Slot: is_excipient_of


_holds between a molecular entity and a drug in which the former is a part of the latter, and is a biologically inactive component_



URI: [bican:is_excipient_of](https://identifiers.org/brain-bican/vocab/is_excipient_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [overlaps](overlaps.md)
            * [part_of](part_of.md)
                * **is_excipient_of**








## Properties

* Range: [Drug](Drug.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: is excipient of
description: holds between a molecular entity and a drug in which the former is a
  part of the latter, and is a biologically inactive component
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
mappings:
- WIKIDATA:Q902638
rank: 1000
is_a: part of
domain: molecular entity
multivalued: true
inherited: true
alias: is_excipient_of
inverse: has excipient
range: drug

```
</details>