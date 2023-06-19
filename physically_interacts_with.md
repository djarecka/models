# Slot: physically_interacts_with


_holds between two entities that make physical contact as part of some interaction.  does not imply a causal relationship._



URI: [bican:physically_interacts_with](https://identifiers.org/brain-bican/vocab/physically_interacts_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [interacts_with](interacts_with.md)
            * **physically_interacts_with** [ [interacts_with](interacts_with.md)]
                * [directly_physically_interacts_with](directly_physically_interacts_with.md)
                * [indirectly_physically_interacts_with](indirectly_physically_interacts_with.md)








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
name: physically interacts with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two entities that make physical contact as part of some
  interaction.  does not imply a causal relationship.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
close_mappings:
- CHEMBL.MECHANISM:binding_agent
- CHEMBL.MECHANISM:chelating_agent
- CHEMBL.MECHANISM:cross-linking_agent
- CHEMBL.MECHANISM:oxidative_enzyme
- CHEMBL.MECHANISM:sequestering_agent
- CHEMBL.MECHANISM:substrate
- DRUGBANK:target
narrow_mappings:
- DRUGBANK:drug-interaction
- FMA:adheres_to
- NCIT:A7
- PR:non-covalently_bound_to
broad_mappings:
- WIKIDATA_PROPERTY:P129
rank: 1000
is_a: interacts with
mixins:
- interacts with
domain: named thing
multivalued: true
inherited: true
alias: physically_interacts_with
symmetric: true
range: named thing

```
</details>