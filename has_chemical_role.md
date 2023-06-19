# Slot: has_chemical_role


_A role is particular behaviour which a chemical entity may exhibit._



URI: [bican:has_chemical_role](https://identifiers.org/brain-bican/vocab/has_chemical_role)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **has_chemical_role**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemi... |  no  |
[MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently ... |  no  |
[SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability i... |  no  |
[ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular ent... |  no  |
[NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |  no  |
[MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular e... |  no  |
[ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more mol... |  no  |
[ProcessedMaterial](ProcessedMaterial.md) | A chemical entity (often a mixture) processed for consumption for nutritional... |  no  |
[Drug](Drug.md) | A substance intended for use in the diagnosis, cure, mitigation, treatment, o... |  no  |
[EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) |  |  no  |
[FoodAdditive](FoodAdditive.md) |  |  no  |
[Food](Food.md) | A substance consumed by a living organism as a source of nutrition |  no  |
[Exon](Exon.md) | A region of the transcript sequence within a gene which is not removed from t... |  no  |
[Transcript](Transcript.md) | An RNA synthesized on a DNA or RNA template by an RNA polymerase |  no  |
[CodingSequence](CodingSequence.md) |  |  no  |
[RNAProduct](RNAProduct.md) |  |  no  |
[RNAProductIsoform](RNAProductIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |  no  |
[NoncodingRNAProduct](NoncodingRNAProduct.md) |  |  no  |
[MicroRNA](MicroRNA.md) |  |  no  |
[SiRNA](SiRNA.md) | A small RNA molecule that is the product of a longer exogenous or endogenous ... |  no  |







## Properties

* Range: [ChemicalRole](ChemicalRole.md)

* Multivalued: True





## Comments

* We expect primarily to use CHEBI chemical roles here; however, we are looking for a mapping between CHEBI And ATC codes to support this slot.

## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CHEBI








### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has chemical role
id_prefixes:
- CHEBI
description: A role is particular behaviour which a chemical entity may exhibit.
comments:
- We expect primarily to use CHEBI chemical roles here; however, we are looking for
  a mapping between CHEBI And ATC codes to support this slot.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: related to at concept level
domain: named thing
multivalued: true
inherited: true
alias: has_chemical_role
domain_of:
- chemical entity
range: chemical role

```
</details>