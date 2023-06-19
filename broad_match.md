# Slot: broad_match


_a list of terms from different schemas or terminology systems that have a broader, more general meaning. Broader terms are typically shown as parents in a hierarchy or tree._



URI: [bican:broad_match](https://identifiers.org/brain-bican/vocab/broad_match)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **broad_match**





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
| canonical_predicate | True || opposite_of | narrow match |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: broad match
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: narrow match
description: a list of terms from different schemas or terminology systems that have
  a broader, more general meaning. Broader terms are typically shown as parents in
  a hierarchy or tree.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- skos:broadMatch
- WIKIDATA:Q39894595
rank: 1000
is_a: related to at concept level
domain: named thing
multivalued: true
inherited: true
alias: broad_match
domain_of:
- predicate mapping
range: named thing

```
</details>