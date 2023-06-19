# Slot: participates_in


_holds between a continuant and a process, where the continuant is somehow involved in the process_



URI: [bican:participates_in](https://identifiers.org/brain-bican/vocab/participates_in)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **participates_in**
            * [is_input_of](is_input_of.md)
            * [is_output_of](is_output_of.md)
            * [catalyzes](catalyzes.md)
            * [is_substrate_of](is_substrate_of.md)
            * [actively_involved_in](actively_involved_in.md)
            * [enables](enables.md)








## Properties

* Range: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: participates in
description: holds between a continuant and a process, where the continuant is somehow
  involved in the process
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0000056
- BFO:0000056
narrow_mappings:
- DRUGBANK:pathway
- HMDB:in_pathway
- LOINC:is_given_pharmaceutical_substance_for
- NCIT:R130
- NCIT:R37
- NCIT:R131
- NCIT:R51
- NCIT:R53
- OBI:0000295
- RO:0002216
- RO:0002505
- SNOMED:has_direct_device
rank: 1000
is_a: related to at instance level
domain: occurrent
multivalued: true
inherited: true
alias: participates_in
inverse: has participant
range: biological process or activity

```
</details>