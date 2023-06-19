# Slot: contributes_to


_holds between two entities where the occurrence, existence, or activity of one contributes to the occurrence or generation of the other_



URI: [bican:contributes_to](https://identifiers.org/brain-bican/vocab/contributes_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **contributes_to**
            * [causes](causes.md)








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
name: contributes to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two entities where the occurrence, existence, or activity
  of one contributes to the occurrence or generation of the other
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002326
close_mappings:
- IDO:0000664
narrow_mappings:
- CTD:marker_mechanism
- MONDO:predisposes_towards
- RO:0002255
- RO:0003304
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: contributes_to
range: named thing

```
</details>