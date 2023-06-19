# Slot: affects


_describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be._



URI: [bican:affects](https://identifiers.org/brain-bican/vocab/affects)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **affects**
            * [affects_response_to](affects_response_to.md)
            * [regulates](regulates.md) [ [interacts_with](interacts_with.md)]
            * [disrupts](disrupts.md)
            * [ameliorates](ameliorates.md)
            * [exacerbates](exacerbates.md)
            * [has_adverse_event](has_adverse_event.md)
            * [has_side_effect](has_side_effect.md)








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
name: affects
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: describes an entity that has a direct affect on the state or quality
  of another existing entity. Use of the 'affects' predicate implies that the affected
  entity already exists, unlike predicates such as 'affects risk for' and 'prevents,
  where the outcome is something that may or may not come to be.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SEMMEDDB:AFFECTS
- DGIdb:affects
related_mappings:
- DRUGBANK:pathway
narrow_mappings:
- SEMMEDDB:ADMINISTERED_TO
- CTD:prediction_hypothesis
- GOREL:0001006
- CTD:inferred
- UPHENO:0000001
- RO:0002263
- RO:0002264
- NCIT:R158
- NCIT:R160
- NCIT:R30
- NCIT:R150
- NCIT:R72
- NCIT:R146
- NCIT:R124
- NCIT:R173
- NCIT:R100
- NCIT:R102
- NCIT:R101
- NCIT:R113
- NCIT:R23
- NCIT:R25
- NCIT:gene_mapped_to_disease
- NCIT:R133
- RO:0002343
- RO:0002355
- RO:0002591
- RO:0002592
- RO:0012003
- SNOMED:has_pathological_process
- UBERGRAPH:is_increase_of
- UBERGRAPH:is_decrease_of
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: affects
range: named thing

```
</details>