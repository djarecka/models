# Slot: interacts_with


_holds between any two entities that directly or indirectly interact with each other_



URI: [bican:interacts_with](https://identifiers.org/brain-bican/vocab/interacts_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **interacts_with**
            * [physically_interacts_with](physically_interacts_with.md) [ [interacts_with](interacts_with.md)]
            * [genetically_interacts_with](genetically_interacts_with.md)







## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |
| [physically_interacts_with](physically_interacts_with.md) | holds between two entities that make physical contact as part of some interac... | None |  |
| [regulates](regulates.md) | A more specific form of affects, that implies the effect results from a biolo... | physical essence or occurrent |  |



## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True

* Mixin: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: interacts with
description: holds between any two entities that directly or indirectly interact with
  each other
notes:
- 'please use a more specific child predicate of interacts with, either physically
  interacts with or genetically interacts with. '
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SEMMEDDB:INTERACTS_WITH
rank: 1000
is_a: related to at instance level
mixin: true
domain: named thing
multivalued: true
inherited: true
alias: interacts_with
symmetric: true
range: named thing

```
</details>