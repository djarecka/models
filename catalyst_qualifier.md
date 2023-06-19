# Slot: catalyst_qualifier


_a qualifier that connects an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change._



URI: [bican:catalyst_qualifier](https://identifiers.org/brain-bican/vocab/catalyst_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * **catalyst_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | A causal relationship between two chemical entities, where the subject repres... |  yes  |







## Properties

* Range: [MacromolecularMachineMixin](MacromolecularMachineMixin.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: catalyst qualifier
description: a qualifier that connects an association between two causally connected
  entities (for example, two chemical entities, or a chemical entity in that changes
  location) and the gene product, gene, or complex that enables or catalyzes the change.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: association slot
domain: association
multivalued: true
alias: catalyst_qualifier
domain_of:
- chemical to chemical derivation association
range: macromolecular machine mixin

```
</details>