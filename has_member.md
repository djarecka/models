# Slot: has_member


_Defines a mereological relation between a collection and an item._



URI: [bican:has_member](https://identifiers.org/brain-bican/vocab/has_member)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **has_member**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mappings](Mappings.md) | A collection of mappings between identifiers |  no  |







## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has member
description: Defines a mereological relation between a collection and an item.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002351
- skos:member
rank: 1000
is_a: related to at concept level
domain: named thing
multivalued: true
inherited: true
alias: has_member
domain_of:
- mappings
range: named thing

```
</details>