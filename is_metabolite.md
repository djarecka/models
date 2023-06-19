# Slot: is_metabolite


_indicates whether a molecular entity is a metabolite_



URI: [bican:is_metabolite](https://identifiers.org/brain-bican/vocab/is_metabolite)




## Inheritance

* [node_property](node_property.md)
    * **is_metabolite**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently ... |  no  |
[SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability i... |  no  |
[NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |  no  |
[Exon](Exon.md) | A region of the transcript sequence within a gene which is not removed from t... |  no  |
[Transcript](Transcript.md) | An RNA synthesized on a DNA or RNA template by an RNA polymerase |  no  |
[CodingSequence](CodingSequence.md) |  |  no  |
[RNAProduct](RNAProduct.md) |  |  no  |
[RNAProductIsoform](RNAProductIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |  no  |
[NoncodingRNAProduct](NoncodingRNAProduct.md) |  |  no  |
[MicroRNA](MicroRNA.md) |  |  no  |
[SiRNA](SiRNA.md) | A small RNA molecule that is the product of a longer exogenous or endogenous ... |  no  |







## Properties

* Range: [Boolean](Boolean.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: is metabolite
description: indicates whether a molecular entity is a metabolite
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- CHEBI:25212
rank: 1000
is_a: node property
domain: molecular entity
alias: is_metabolite
domain_of:
- molecular entity
range: boolean

```
</details>