# Slot: subject_category_closure


_Used to hold the subject category closure of an association. This is a denormalized  field used primarily in the SQL serialization of a knowledge graph via KGX._



URI: [bican:subject_category_closure](https://identifiers.org/brain-bican/vocab/subject_category_closure)




## Inheritance

* [association_slot](association_slot.md)
    * **subject_category_closure**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Association](Association.md) | A typed association between two entities, supported by evidence |  no  |
[ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) |  |  no  |
[ContributorAssociation](ContributorAssociation.md) | Any association between an entity (such as a publication) and various agents ... |  no  |
[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | Any association between one genotype and a genotypic entity that is a sub-com... |  no  |
[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | Any association between a genotype and a gene |  no  |
[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | Any association between a genotype and a sequence variant |  no  |
[GeneToGeneAssociation](GeneToGeneAssociation.md) | abstract parent class for different kinds of gene-gene or gene product to gen... |  no  |
[GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | A homology association between two genes |  no  |
[GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | Set membership of a gene in a family of genes related by common evolutionary ... |  no  |
[GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  no  |
[PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | An interaction between two genes or two gene products |  no  |
[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |  no  |
[CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | An relationship between a cell line and a disease or a phenotype, where the c... |  no  |
[ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | A relationship between two chemical entities |  no  |
[ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) |  |  no  |
[ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) |  |  no  |
[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | A causal relationship between two chemical entities, where the subject repres... |  no  |
[ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | An interaction between a chemical entity and a phenotype or disease, where th... |  no  |
[ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
[ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  no  |
[GeneToPathwayAssociation](GeneToPathwayAssociation.md) | An interaction between a gene or gene product and a biological process or pat... |  no  |
[MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | Association that holds the relationship between a reaction and the pathway it... |  no  |
[ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | An interaction between a chemical entity and a biological process or pathway |  no  |
[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) |  |  no  |
[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes a physical interaction between a chemical entity and a gene or gene... |  no  |
[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  no  |
[DrugToGeneAssociation](DrugToGeneAssociation.md) | An interaction between a drug and a gene or gene product |  no  |
[MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | An association between a material sample and the material entity from which i... |  no  |
[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | An association between a material sample and a disease or phenotype |  no  |
[DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | An association between an exposure event and a disease |  no  |
[ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome |  no  |
[InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | association between a named thing and a information content entity where the ... |  no  |
[DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | An association between either a disease or a phenotypic feature and an anatom... |  no  |
[DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | An association between either a disease or a phenotypic feature and its mode ... |  no  |
[GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | Any association between one genotype and a phenotypic feature, where having t... |  no  |
[ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | Any association between an environment and a phenotypic feature, where being ... |  no  |
[DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenot... |  no  |
[CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e |  no  |
[BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | An association between an mixture behavior and a behavioral feature manifeste... |  no  |
[GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) |  |  no  |
[GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) |  |  no  |
[GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |  |  no  |
[CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) |  |  no  |
[CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) |  |  no  |
[DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) |  |  no  |
[VariantToGeneAssociation](VariantToGeneAssociation.md) | An association between a variant and a gene, where the variant has a genetic ... |  no  |
[VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  no  |
[VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |  no  |
[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | An association between a two populations |  no  |
[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) |  |  no  |
[VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) |  |  no  |
[GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) |  |  no  |
[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) |  |  no  |
[VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) |  |  no  |
[GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) |  |  no  |
[CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) |  |  no  |
[OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) |  |  no  |
[OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) |  |  no  |
[TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) |  |  no  |
[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) |  |  no  |
[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and a gene expression site, possibly qualified ... |  no  |
[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | An association between a sequence variant and a treatment or health intervent... |  no  |
[FunctionalAssociation](FunctionalAssociation.md) | An association between a macromolecular machine mixin (gene, gene product or ... |  no  |
[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |  no  |
[MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |  no  |
[MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | A functional association between a macromolecular machine (gene, gene product... |  no  |
[MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | Added in response to capturing relationship between microbiome activities as ... |  no  |
[MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | Added in response to capturing relationship between microbiome activities as ... |  no  |
[GeneToGoTermAssociation](GeneToGoTermAssociation.md) |  |  no  |
[EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) |  |  no  |
[EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) |  |  no  |
[SequenceAssociation](SequenceAssociation.md) | An association between a sequence feature and a nucleic acid entity it is loc... |  no  |
[GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |  no  |
[SequenceFeatureRelationship](SequenceFeatureRelationship.md) | For example, a particular exon is part of a particular transcript or gene |  no  |
[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | A gene is a collection of transcripts |  no  |
[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | A gene is transcribed and potentially translated to a gene product |  no  |
[ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | A transcript is formed from multiple exons |  no  |
[ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | A regulatory relationship between two genes |  no  |
[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) |  |  no  |
[AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | A relationship between two anatomical entities where the relationship is mere... |  no  |
[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | A relationship between two anatomical entities where the relationship is onto... |  no  |
[OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | A relationship between two organism taxon nodes |  no  |
[OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | A child-parent relationship between two taxa |  no  |
[OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | An interaction relationship between two taxa |  no  |
[OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) |  |  no  |







## Properties

* Range: [OntologyClass](OntologyClass.md)

* Multivalued: True






## Examples

| Value |
| --- |
| ['biolink:Gene", "biolink:NamedThing'] |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| denormalized | True |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: subject category closure
annotations:
  denormalized:
    tag: denormalized
    value: 'True'
description: Used to hold the subject category closure of an association. This is
  a denormalized  field used primarily in the SQL serialization of a knowledge graph
  via KGX.
examples:
- value: '[''biolink:Gene", "biolink:NamedThing'']'
  description: 'The subject category closure of the association between the gene ''BRCA1''
    and the disease ''breast cancer'' is the set of all biolink classes that are ancestors
    of ''biolink:Gene'' in the biolink model.  Note: typically the "subclass of" and
    "part of"  relations are used to construct the closure, but other relations may
    be used as well.'
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: association slot
domain: association
multivalued: true
alias: subject_category_closure
domain_of:
- association
range: ontology class

```
</details>