# Slot: has_output


_holds between a process and a continuant, where the continuant is an output of the process_



URI: [bican:has_output](https://identifiers.org/brain-bican/vocab/has_output)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_participant](has_participant.md)
            * **has_output**





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
| canonical_predicate | True || opposite_of | has input |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has output
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  opposite_of:
    tag: opposite_of
    value: has input
description: holds between a process and a continuant, where the continuant is an
  output of the process
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002234
narrow_mappings:
- NCIT:R31
- OBI:0000299
- PathWhiz:has_right_element
- RO:0002296
- RO:0002297
- RO:0002298
- RO:0002299
- RO:0002588
- RO:0004008
rank: 1000
is_a: has participant
domain: biological process or activity
multivalued: true
inherited: true
alias: has_output
domain_of:
- biological process or activity
range: named thing

```
</details>