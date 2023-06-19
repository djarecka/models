# Slot: derives_into


_holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity_



URI: [bican:derives_into](https://identifiers.org/brain-bican/vocab/derives_into)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **derives_into**
            * [has_metabolite](has_metabolite.md)








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True



## Aliases


* is normal cell origin of disease
* may be normal cell origin of disease



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: derives into
description: holds between two distinct material entities, the old entity and the
  new entity, in which the new entity begins to exist when the old entity ceases to
  exist, and the new entity inherits the significant portion of the matter of the
  old entity
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- is normal cell origin of disease
- may be normal cell origin of disease
exact_mappings:
- RO:0001001
- SEMMEDDB:CONVERTS_TO
- FMA:derives
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: derives_into
inverse: derives from
range: named thing

```
</details>