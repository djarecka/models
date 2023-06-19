# Slot: manifestation_of


_that part of a phenomenon which is directly observable or visibly expressed, or which gives evidence to the underlying process; used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome_



URI: [bican:manifestation_of](https://identifiers.org/brain-bican/vocab/manifestation_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **manifestation_of**
            * [mode_of_inheritance_of](mode_of_inheritance_of.md)








## Properties

* Range: [Disease](Disease.md)

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
name: manifestation of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: that part of a phenomenon which is directly observable or visibly expressed,
  or which gives evidence to the underlying process; used in SemMedDB for linking
  things like dysfunctions and processes to some disease or syndrome
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SEMMEDDB:MANIFESTATION_OF
- OMIM:manifestation_of
narrow_mappings:
- SNOMED:has_definitional_manifestation
broad_mappings:
- WIKIDATA_PROPERTY:P1557
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: manifestation_of
range: disease

```
</details>