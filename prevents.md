# Slot: prevents


_holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical entity, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature._



URI: [bican:prevents](https://identifiers.org/brain-bican/vocab/prevents)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects_risk_for](affects_risk_for.md)
            * **prevents**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | predisposes |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: prevents
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: predisposes
description: holds between an entity whose application or use reduces the likelihood
  of a potential outcome. Typically used to associate a chemical entity, exposure,
  activity, or medical intervention that can prevent the onset a disease or phenotypic
  feature.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SEMMEDDB:PREVENTS
narrow_mappings:
- RO:0002599
rank: 1000
is_a: affects risk for
domain: named thing
multivalued: true
inherited: true
alias: prevents
range: named thing

```
</details>