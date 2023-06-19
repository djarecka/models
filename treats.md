# Slot: treats


_holds between a therapeutic procedure or chemical entity and a disease or phenotypic feature that it is used to treat_



URI: [bican:treats](https://identifiers.org/brain-bican/vocab/treats)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * [ameliorates](ameliorates.md)
                * **treats**








## Properties

* Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

* Multivalued: True



## Aliases


* is substance that treats
* indicated for



## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | contraindicated for |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: treats
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: contraindicated for
description: holds between a therapeutic procedure or chemical entity and a disease
  or phenotypic feature that it is used to treat
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- is substance that treats
- indicated for
exact_mappings:
- DRUGBANK:treats
- SEMMEDDB:TREATS
- WIKIDATA_PROPERTY:P2175
related_mappings:
- MONDO:disease_responds_to
narrow_mappings:
- RO:0002606
- NCIT:regimen_has_accepted_use_for_disease
- REPODB:clinically_tested_approved_unknown_phase
- REPODB:clinically_tested_suspended_phase_0
- REPODB:clinically_tested_suspended_phase_1
- REPODB:clinically_tested_suspended_phase_1_or_phase_2
- REPODB:clinically_tested_suspended_phase_2
- REPODB:clinically_tested_suspended_phase_2_or_phase_3
- REPODB:clinically_tested_suspended_phase_3
- REPODB:clinically_tested_terminated_phase_0
- REPODB:clinically_tested_terminated_phase_1
- REPODB:clinically_tested_terminated_phase_1_or_phase_2
- REPODB:clinically_tested_terminated_phase_2
- REPODB:clinically_tested_terminated_phase_2_or_phase_3
- REPODB:clinically_tested_terminated_phase_3
- REPODB:clinically_tested_withdrawn_phase_0
- REPODB:clinically_tested_withdrawn_phase_1
- REPODB:clinically_tested_withdrawn_phase_1_or_phase_2
- REPODB:clinically_tested_withdrawn_phase_2
- REPODB:clinically_tested_withdrawn_phase_2_or_phase_3
- REPODB:clinically_tested_withdrawn_phase_3
- SNOMED:plays_role
rank: 1000
is_a: ameliorates
domain: chemical or drug or treatment
multivalued: true
inherited: true
alias: treats
range: disease or phenotypic feature

```
</details>