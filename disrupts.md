# Slot: disrupts


_describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another._



URI: [bican:disrupts](https://identifiers.org/brain-bican/vocab/disrupts)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **disrupts**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True



## Aliases


* disease causes disruption of



## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | enables |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: disrupts
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: enables
description: describes a relationship where one entity degrades or interferes with
  the structure, function, or occurrence of another.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- disease causes disruption of
exact_mappings:
- SEMMEDDB:DISRUPTS
- CHEMBL.MECHANISM:disrupting_agent
narrow_mappings:
- RO:0004024
- RO:0004025
rank: 1000
is_a: affects
domain: named thing
multivalued: true
inherited: true
alias: disrupts
range: named thing

```
</details>