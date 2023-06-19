# Slot: directly_physically_interacts_with


_A causal mechanism mediated by a direct contact between the effector and target entities (this contact may  be weak or strong, transient or stable)._



URI: [bican:directly_physically_interacts_with](https://identifiers.org/brain-bican/vocab/directly_physically_interacts_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * [physically_interacts_with](physically_interacts_with.md) [ [interacts_with](interacts_with.md)]
                * **directly_physically_interacts_with**
                    * [binds](binds.md)








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
name: directly physically interacts with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: A causal mechanism mediated by a direct contact between the effector
  and target entities (this contact may  be weak or strong, transient or stable).
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002436
narrow_mappings:
- PHAROS:drug_targets
- DRUGBANK:chelator
- CTD:affects_binding
- DGIdb:cofactor
broad_mappings:
- SIO:000203
- RO:0002578
rank: 1000
is_a: physically interacts with
domain: named thing
multivalued: true
inherited: true
alias: directly_physically_interacts_with
symmetric: true
range: named thing

```
</details>