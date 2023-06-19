# Slot: interacting_molecules_category

URI: [bican:interacting_molecules_category](https://identifiers.org/brain-bican/vocab/interacting_molecules_category)




## Inheritance

* [association_slot](association_slot.md)
    * **interacting_molecules_category**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |  no  |







## Properties

* Range: [OntologyClass](OntologyClass.md)






## Examples

| Value |
| --- |
| MI:1048 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: interacting molecules category
examples:
- value: MI:1048
  description: smallmolecule-protein
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- MI:1046
rank: 1000
is_a: association slot
values_from:
- MI
domain: association
alias: interacting_molecules_category
domain_of:
- pairwise molecular interaction
range: ontology class

```
</details>