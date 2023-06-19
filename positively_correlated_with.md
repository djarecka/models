# Slot: positively_correlated_with


_A relationship that holds between two concepts represented by variables for which a statistical correlation  is demonstrated, wherein variable values move together in the same direction (i.e. increased in one or  presence of one correlates with an increase or presence of the other)._



URI: [bican:positively_correlated_with](https://identifiers.org/brain-bican/vocab/positively_correlated_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **positively_correlated_with**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | negatively correlated with |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: positively correlated with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: negatively correlated with
description: A relationship that holds between two concepts represented by variables
  for which a statistical correlation  is demonstrated, wherein variable values move
  together in the same direction (i.e. increased in one or  presence of one correlates
  with an increase or presence of the other).
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- CTD:positive_correlation
rank: 1000
is_a: correlated with
domain: named thing
multivalued: true
inherited: true
alias: positively_correlated_with
symmetric: true
range: named thing

```
</details>