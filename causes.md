# Slot: causes


_holds between two entities where the occurrence, existence, or activity of one causes the occurrence or generation of the other_



URI: [bican:causes](https://identifiers.org/brain-bican/vocab/causes)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contributes_to](contributes_to.md)
            * **causes**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | prevents |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: causes
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: prevents
description: holds between two entities where the occurrence, existence, or activity
  of one causes the occurrence or generation of the other
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SEMMEDDB:CAUSES
- WIKIDATA_PROPERTY:P1542
- SNOMED:cause_of
- RO:0003303
narrow_mappings:
- MONDO:disease_triggers
- GOREL:0000040
- MONDO:disease_causes_feature
- MONDO:disease_triggers
- NCIT:allele_has_abnormality
- NCIT:biological_process_has_result_biological_process
- NCIT:chemical_or_drug_has_physiologic_effect
- NCIT:chemical_or_drug_initiates_biological_process
- NCIT:process_initiates_biological_process
- NCIT:chromosome_mapped_to_disease
- NCIT:disease_has_normal_tissue_origin
- NBO-PROPERTY:in_response_to
- orphanet:317343
- orphanet:317344
- orphanet:317346
- orphanet:410295
- orphanet:410296
- RO:0002256
- RO:0002315
- RO:0002507
- RO:0002509
- RO:0004001
- SNOMED:causative_agent_of
- SNOMED:has_realization
- UMLS:has_physiologic_effect
broad_mappings:
- RO:0002410
- RO:0002506
rank: 1000
is_a: contributes to
domain: named thing
multivalued: true
inherited: true
alias: causes
range: named thing

```
</details>