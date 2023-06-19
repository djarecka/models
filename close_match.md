# Slot: close_match


_a list of terms from different schemas or terminology systems that have a semantically similar but not strictly equivalent, broader, or narrower meaning. Such terms often describe the same general concept from different ontological perspectives (e.g. drug as a type of chemical entity versus drug as a type of role borne by a chemical entity)._



URI: [bican:close_match](https://identifiers.org/brain-bican/vocab/close_match)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **close_match**
            * [exact_match](exact_match.md)








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
name: close match
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: a list of terms from different schemas or terminology systems that have
  a semantically similar but not strictly equivalent, broader, or narrower meaning.
  Such terms often describe the same general concept from different ontological perspectives
  (e.g. drug as a type of chemical entity versus drug as a type of role borne by a
  chemical entity).
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- skos:closeMatch
- SEMMEDDB:same_as
narrow_mappings:
- CHEBI:is_enantiomer_of
- CHEBI:is_tautomer_of
- MEDDRA:classified_as
- oboInOwl:hasDbXref
- RXNORM:has_quantified_form
- UMLS:SY
rank: 1000
is_a: related to at concept level
domain: named thing
multivalued: true
inherited: true
alias: close_match
symmetric: true
range: named thing

```
</details>