# Slot: same_as


_holds between two entities that are considered equivalent to each other_



URI: [bican:same_as](https://identifiers.org/brain-bican/vocab/same_as)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * [close_match](close_match.md)
            * [exact_match](exact_match.md)
                * **same_as**








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
name: same as
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between two entities that are considered equivalent to each other
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- owl:sameAs
- skos:exactMatch
- WIKIDATA_PROPERTY:P2888
- CHEMBL.MECHANISM:equivalent_to
- MONDO:equivalentTo
close_mappings:
- owl:equivalentClass
narrow_mappings:
- DRUGBANK:external-identifier
rank: 1000
is_a: exact match
domain: named thing
multivalued: true
inherited: true
alias: same_as
symmetric: true
range: named thing

```
</details>