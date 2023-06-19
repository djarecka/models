# Slot: enabled_by


_holds between a process and a physical entity, where the physical entity executes the process_



URI: [bican:enabled_by](https://identifiers.org/brain-bican/vocab/enabled_by)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [has_participant](has_participant.md)
            * **enabled_by**





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

* Range: [PhysicalEntity](PhysicalEntity.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| opposite_of | prevented by |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: enabled by
annotations:
  opposite_of:
    tag: opposite_of
    value: prevented by
description: holds between a process and a physical entity, where the physical entity
  executes the process
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002333
rank: 1000
is_a: has participant
domain: biological process or activity
multivalued: true
inherited: true
alias: enabled_by
domain_of:
- biological process or activity
inverse: enables
range: physical entity

```
</details>