# Slot: location_of


_holds between material entity or site and a material entity that is located within it (but not considered a part of it)_



URI: [bican:location_of](https://identifiers.org/brain-bican/vocab/location_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **location_of**
            * [expresses](expresses.md)








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True



## Aliases


* site of



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: location of
description: holds between material entity or site and a material entity that is located
  within it (but not considered a part of it)
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- site of
exact_mappings:
- RO:0001015
- SEMMEDDB:LOCATION_OF
- WIKIDATA_PROPERTY:P276
- FMA:location_of
narrow_mappings:
- SNOMED:inherent_location_of
- NCIT:Anatomic_Structure_Has_Location_Role
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: location_of
inverse: located in
range: named thing

```
</details>