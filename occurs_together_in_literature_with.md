# Slot: occurs_together_in_literature_with


_holds between two entities where their co-occurrence is correlated by counts of publications in which both occur, using some threshold of occurrence as defined by the edge provider._



URI: [bican:occurs_together_in_literature_with](https://identifiers.org/brain-bican/vocab/occurs_together_in_literature_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **occurs_together_in_literature_with**








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
name: occurs together in literature with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two entities where their co-occurrence is correlated by
  counts of publications in which both occur, using some threshold of occurrence as
  defined by the edge provider.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: correlated with
domain: named thing
multivalued: true
inherited: true
alias: occurs_together_in_literature_with
symmetric: true
range: named thing

```
</details>