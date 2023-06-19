# Slot: highest_FDA_approval_status


_Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'_



URI: [bican:highest_FDA_approval_status](https://identifiers.org/brain-bican/vocab/highest_FDA_approval_status)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular ent... |  no  |
[MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular e... |  no  |
[ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more mol... |  no  |
[ProcessedMaterial](ProcessedMaterial.md) | A chemical entity (often a mixture) processed for consumption for nutritional... |  no  |
[Drug](Drug.md) | A substance intended for use in the diagnosis, cure, mitigation, treatment, o... |  no  |
[Food](Food.md) | A substance consumed by a living organism as a source of nutrition |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: highest FDA approval status
description: Should be the highest level of FDA approval this chemical entity or device
  has, regardless of which disease, condition or phenotype it is currently being reviewed
  to treat.  For specific levels of FDA approval for a specific condition, disease,
  phenotype, etc., see the association slot, 'FDA approval status.'
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
alias: highest_FDA_approval_status
domain_of:
- chemical mixture
range: string

```
</details>