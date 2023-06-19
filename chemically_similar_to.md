# Slot: chemically_similar_to


_holds between one small molecule entity and another that it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity._



URI: [bican:chemically_similar_to](https://identifiers.org/brain-bican/vocab/chemically_similar_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [similar_to](similar_to.md)
            * **chemically_similar_to**








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
name: chemically similar to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between one small molecule entity and another that it approximates
  for purposes of scientific study, in virtue of its exhibiting similar features of
  the studied entity.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
narrow_mappings:
- CHEBI:has_parent_hydride
- CHEBI:has_functional_parent
- CHEBI:is_conjugate_acid_of
- CHEBI:is_conjugate_base_of
- CHEBI:is_enantiomer_of
- CHEBI:is_tautomer_of
- NCIT:has_salt_form
rank: 1000
is_a: similar to
domain: named thing
multivalued: true
inherited: true
alias: chemically_similar_to
symmetric: true
range: named thing

```
</details>