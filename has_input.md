# Slot: has_input


_holds between a process and a continuant, where the continuant is an input into the process_



URI: [bican:has_input](https://identifiers.org/brain-bican/vocab/has_input)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_participant](has_participant.md)
            * **has_input**
                * [consumes](consumes.md)





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | Either an individual molecular activity, or a collection of causally connecte... |  no  |
[MolecularActivity](MolecularActivity.md) | An execution of a molecular function carried out by a gene product or macromo... |  yes  |
[BiologicalProcess](BiologicalProcess.md) | One or more causally connected executions of molecular functions |  no  |
[Pathway](Pathway.md) |  |  no  |
[PhysiologicalProcess](PhysiologicalProcess.md) |  |  no  |
[Behavior](Behavior.md) |  |  no  |
[PathologicalProcess](PathologicalProcess.md) | A biologic function or a process having an abnormal or deleterious effect at ... |  no  |







## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || opposite_of | has output |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has input
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: has output
description: holds between a process and a continuant, where the continuant is an
  input into the process
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002233
- SEMMEDDB:USES
narrow_mappings:
- LOINC:has_fragments_for_synonyms
- LOINC:has_system
- PathWhiz:has_left_element
- RO:0002590
- RO:0004009
- SNOMED:has_finding_method
- SNOMED:has_precondition
- SNOMED:has_specimen_source_identity
- SNOMED:has_specimen_substance
- SNOMED:uses_access_device
- SNOMED:uses_device
- SNOMED:uses_energy
- SNOMED:uses_substance
rank: 1000
is_a: has participant
domain: biological process or activity
multivalued: true
inherited: true
alias: has_input
domain_of:
- biological process or activity
range: named thing

```
</details>