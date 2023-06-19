# Slot: exact_match


_holds between two entities that have strictly equivalent meanings, with a high degree of confidence_



URI: [bican:exact_match](https://identifiers.org/brain-bican/vocab/exact_match)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * [close_match](close_match.md)
            * **exact_match**
                * [same_as](same_as.md)





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |







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
name: exact match
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two entities that have strictly equivalent meanings, with
  a high degree of confidence
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- skos:exactMatch
- WIKIDATA:Q39893449
- WIKIDATA:P2888
rank: 1000
is_a: close match
domain: named thing
multivalued: true
inherited: true
alias: exact_match
domain_of:
- predicate mapping
symmetric: true
range: named thing

```
</details>