# Slot: narrow_match


_a list of terms from different schemas or terminology systems that have a narrower, more specific meaning. Narrower terms are typically shown as children in a hierarchy or tree._



URI: [bican:narrow_match](https://identifiers.org/brain-bican/vocab/narrow_match)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **narrow_match**





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
| opposite_of | broad match |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: narrow match
annotations:
  opposite_of:
    tag: opposite_of
    value: broad match
description: a list of terms from different schemas or terminology systems that have
  a narrower, more specific meaning. Narrower terms are typically shown as children
  in a hierarchy or tree.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- skos:narrowMatch
- WIKIDATA:Q39893967
rank: 1000
is_a: related to at concept level
domain: named thing
multivalued: true
inherited: true
alias: narrow_match
domain_of:
- predicate mapping
inverse: broad match
range: named thing

```
</details>