# Slot: has_biological_sequence


_connects a genomic feature to its sequence_



URI: [bican:has_biological_sequence](https://identifiers.org/brain-bican/vocab/has_biological_sequence)




## Inheritance

* [node_property](node_property.md)
    * **has_biological_sequence**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomicEntity](GenomicEntity.md) |  |  no  |
[EpigenomicEntity](EpigenomicEntity.md) |  |  no  |
[GeneAnnotation](GeneAnnotation.md) | An annotation describing the location, boundaries, and functions of  individu... |  no  |
[GenomeAnnotation](GenomeAnnotation.md) | Location and nomenclature of genes and all of the coding regions in a genome ... |  no  |
[NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |  no  |
[RegulatoryRegion](RegulatoryRegion.md) | A region (or regions) of the genome that contains known or putative regulator... |  no  |
[AccessibleDnaRegion](AccessibleDnaRegion.md) | A region (or regions) of a chromatinized genome that has been measured to be ... |  no  |
[TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | A region (or regions) of the genome that contains a region of DNA known or pr... |  no  |
[Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |  no  |
[NucleosomeModification](NucleosomeModification.md) | A chemical modification of a histone protein within a nucleosome octomer or a... |  no  |
[Genome](Genome.md) | A genome is the sum of genetic material within a cell or virion |  no  |
[Exon](Exon.md) | A region of the transcript sequence within a gene which is not removed from t... |  no  |
[Transcript](Transcript.md) | An RNA synthesized on a DNA or RNA template by an RNA polymerase |  no  |
[CodingSequence](CodingSequence.md) |  |  no  |
[RNAProduct](RNAProduct.md) |  |  no  |
[RNAProductIsoform](RNAProductIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |  no  |
[NoncodingRNAProduct](NoncodingRNAProduct.md) |  |  no  |
[MicroRNA](MicroRNA.md) |  |  no  |
[SiRNA](SiRNA.md) | A small RNA molecule that is the product of a longer exogenous or endogenous ... |  no  |
[Genotype](Genotype.md) | An information content entity that describes a genome by specifying the total... |  no  |
[Haplotype](Haplotype.md) | A set of zero or more Alleles on a single instance of a Sequence[VMC] |  no  |
[SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibi... |  yes  |
[Snv](Snv.md) | SNVs are single nucleotide positions in genomic DNA at which different sequen... |  no  |
[ReagentTargetedGene](ReagentTargetedGene.md) | A gene altered in its expression level in the context of some experiment as a... |  no  |
[GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic backg... |  no  |







## Properties

* Range: [BiologicalSequence](BiologicalSequence.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has biological sequence
description: connects a genomic feature to its sequence
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: node property
domain: named thing
alias: has_biological_sequence
domain_of:
- genomic entity
- epigenomic entity
range: biological sequence

```
</details>