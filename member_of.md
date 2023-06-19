# Slot: member_of


_Defines a mereological relation between a item and a collection._



URI: [bican:member_of](https://identifiers.org/brain-bican/vocab/member_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **member_of**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Mapping](Mapping.md) | text |  no  |







## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: member of
description: Defines a mereological relation between a item and a collection.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002350
close_mappings:
- skos:member
rank: 1000
is_a: related to at concept level
domain: named thing
multivalued: true
inherited: true
alias: member_of
domain_of:
- mapping
inverse: has member
range: named thing

```
</details>