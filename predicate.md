# Slot: predicate


_A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes._



URI: [rdf:predicate](rdf:predicate)




## Inheritance

* [association_slot](association_slot.md)
    * **predicate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
[Association](Association.md) | A typed association between two entities, supported by evidence |  no  |
[ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) |  |  yes  |
[ContributorAssociation](ContributorAssociation.md) | Any association between an entity (such as a publication) and various agents ... |  yes  |
[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | Any association between one genotype and a genotypic entity that is a sub-com... |  yes  |
[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | Any association between a genotype and a gene |  yes  |
[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | Any association between a genotype and a sequence variant |  yes  |
[GeneToGeneAssociation](GeneToGeneAssociation.md) | abstract parent class for different kinds of gene-gene or gene product to gen... |  no  |
[GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | A homology association between two genes |  yes  |
[GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | Set membership of a gene in a family of genes related by common evolutionary ... |  yes  |
[GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same condition... |  yes  |
[PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | An interaction between two genes or two gene products |  yes  |
[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |  yes  |
[CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | An relationship between a cell line and a disease or a phenotype, where the c... |  no  |
[ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | A relationship between two chemical entities |  no  |
[ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) |  |  no  |
[ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) |  |  no  |
[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | A causal relationship between two chemical entities, where the subject repres... |  yes  |
[ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | An interaction between a chemical entity and a phenotype or disease, where th... |  no  |
[ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  yes  |
[ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or p... |  yes  |
[GeneToPathwayAssociation](GeneToPathwayAssociation.md) | An interaction between a gene or gene product and a biological process or pat... |  no  |
[MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | Association that holds the relationship between a reaction and the pathway it... |  yes  |
[ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | An interaction between a chemical entity and a biological process or pathway |  no  |
[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) |  |  yes  |
[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes a physical interaction between a chemical entity and a gene or gene... |  yes  |
[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  yes  |
[DrugToGeneAssociation](DrugToGeneAssociation.md) | An interaction between a drug and a gene or gene product |  no  |
[MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | An association between a material sample and the material entity from which i... |  yes  |
[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | An association between a material sample and a disease or phenotype |  no  |
[DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | An association between an exposure event and a disease |  no  |
[ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome |  no  |
[InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | association between a named thing and a information content entity where the ... |  yes  |
[DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | An association between either a disease or a phenotypic feature and an anatom... |  no  |
[DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | An association between either a disease or a phenotypic feature and its mode ... |  yes  |
[GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | Any association between one genotype and a phenotypic feature, where having t... |  yes  |
[ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | Any association between an environment and a phenotypic feature, where being ... |  no  |
[DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenot... |  no  |
[CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e |  no  |
[BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | An association between an mixture behavior and a behavioral feature manifeste... |  no  |
[GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) |  |  yes  |
[GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) |  |  no  |
[GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |  |  no  |
[CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) |  |  no  |
[CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) |  |  no  |
[DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) |  |  yes  |
[VariantToGeneAssociation](VariantToGeneAssociation.md) | An association between a variant and a gene, where the variant has a genetic ... |  yes  |
[VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i |  yes  |
[VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |  no  |
[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | An association between a two populations |  yes  |
[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) |  |  no  |
[VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) |  |  yes  |
[GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) |  |  yes  |
[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) |  |  no  |
[VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) |  |  no  |
[GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) |  |  no  |
[CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) |  |  no  |
[OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) |  |  no  |
[OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) |  |  no  |
[TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) |  |  no  |
[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) |  |  yes  |
[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and a gene expression site, possibly qualified ... |  yes  |
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
[GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |  yes  |
[SequenceFeatureRelationship](SequenceFeatureRelationship.md) | For example, a particular exon is part of a particular transcript or gene |  no  |
[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | A gene is a collection of transcripts |  no  |
[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | A gene is transcribed and potentially translated to a gene product |  yes  |
[ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | A transcript is formed from multiple exons |  no  |
[ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | A regulatory relationship between two genes |  yes  |
[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) |  |  no  |
[AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | A relationship between two anatomical entities where the relationship is mere... |  yes  |
[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | A relationship between two anatomical entities where the relationship is onto... |  yes  |
[OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | A relationship between two organism taxon nodes |  no  |
[OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | A child-parent relationship between two taxa |  yes  |
[OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | An interaction relationship between two taxa |  yes  |
[OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) |  |  yes  |







## Properties

* Range: [PredicateType](PredicateType.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: predicate
local_names:
  ga4gh:
    local_name_source: ga4gh
    local_name_value: annotation predicate
  translator:
    local_name_source: translator
    local_name_value: predicate
description: A high-level grouping for the relationship type. AKA minimal predicate.
  This is analogous to category for nodes.
notes:
- Has a value from the Biolink related_to hierarchy. In RDF,  this corresponds to
  rdf:predicate and in Neo4j this corresponds to the relationship type. The convention
  is for an edge label in snake_case form. For example, biolink:related_to, biolink:causes,
  biolink:treats
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- owl:annotatedProperty
- OBAN:association_has_predicate
rank: 1000
is_a: association slot
domain: association
slot_uri: rdf:predicate
alias: predicate
domain_of:
- predicate mapping
- association
range: predicate type
required: true

```
</details>