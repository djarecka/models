# Slot: binds


_A causal mechanism mediated by the direct contact between effector and target chemical or biomolecular entity,  which form a stable physical interaction._



URI: [bican:binds](https://identifiers.org/brain-bican/vocab/binds)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * [physically_interacts_with](physically_interacts_with.md) [ [interacts_with](interacts_with.md)]
                * [directly_physically_interacts_with](directly_physically_interacts_with.md)
                    * **binds**








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
name: binds
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: A causal mechanism mediated by the direct contact between effector and
  target chemical or biomolecular entity,  which form a stable physical interaction.
deprecated: 'True'
from_schema: https://identifiers.org/brain-bican/kb-model
close_mappings:
- DGIdb:binder
rank: 1000
is_a: directly physically interacts with
domain: named thing
multivalued: true
inherited: true
alias: binds
symmetric: true
range: named thing

```
</details>