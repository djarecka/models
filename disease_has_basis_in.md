# Slot: disease_has_basis_in


_A relation that holds between a disease and an entity where the state of the entity has contribution to the disease._



URI: [bican:disease_has_basis_in](https://identifiers.org/brain-bican/vocab/disease_has_basis_in)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **disease_has_basis_in**








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
name: disease has basis in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: A relation that holds between a disease and an entity where the state
  of the entity has contribution to the disease.
from_schema: https://identifiers.org/brain-bican/kb-model
narrow_mappings:
- MONDO:disease_has_basis_in_development_of
- MONDO:disease_has_basis_in_accumulation_of
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: disease_has_basis_in
range: named thing

```
</details>