# Slot: predisposes


_holds between two entities where exposure to one entity increases the chance of developing the other_



URI: [bican:predisposes](https://identifiers.org/brain-bican/vocab/predisposes)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects_risk_for](affects_risk_for.md)
            * **predisposes**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | prevents |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: predisposes
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: prevents
description: holds between two entities where exposure to one entity increases the
  chance of developing the other
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SEMMEDDB:PREDISPOSES
rank: 1000
is_a: affects risk for
domain: named thing
multivalued: true
inherited: true
alias: predisposes
range: named thing

```
</details>