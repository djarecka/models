# Slot: derives_from


_holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity_



URI: [bican:derives_from](https://identifiers.org/brain-bican/vocab/derives_from)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **derives_from**
            * [is_metabolite_of](is_metabolite_of.md)








## Properties

* Range: [NamedThing](NamedThing.md)

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
name: derives from
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two distinct material entities, the new entity and the
  old entity, in which the new entity begins to exist when the old entity ceases to
  exist, and the new entity inherits the significant portion of the matter of the
  old entity
in_subset:
- translator_minimal
- samples
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0001000
- FMA:derives_from
- DOID-PROPERTY:derives_from
narrow_mappings:
- CHEBI:has_functional_parent
- SNOMED:has_specimen_source_topography
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: derives_from
inverse: derives into
range: named thing

```
</details>