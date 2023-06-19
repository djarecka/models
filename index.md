# kb-model



URI: https://identifiers.org/brain-bican/kb-model

Name: kb-model



## Classes

| Class | Description |
| --- | --- |
| [Annotation](Annotation.md) | Biolink Model root class for entity annotations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QuantityValue](QuantityValue.md) | A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value |
| [AnnotationCollection](AnnotationCollection.md) | None |
| [BehavioralOutcome](BehavioralOutcome.md) | An outcome resulting from an exposure event which is the manifestation of human behavior. |
| [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md) | An abstract association for use where the case is the subject |
| [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) | An relationship between a cell line and another entity |
| [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) | A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities. |
| [ChemicalEntityOrProteinOrPolypeptide](ChemicalEntityOrProteinOrPolypeptide.md) | A union of chemical entities and children, and protein and polypeptide. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities. |
| [ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md) | An interaction between a chemical entity and another entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md) | An interaction between a chemical entity and another entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md) | An interaction between a drug and another entity |
| [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md) | None |
| [DiseaseOrPhenotypicFeatureOutcome](DiseaseOrPhenotypicFeatureOutcome.md) | Physiological outcomes resulting from an exposure event which is the manifestation of a disease or other characteristic phenotype. |
| [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md) | None |
| [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) | None |
| [Entity](Entity.md) | Root Biolink Model class for all things and informational relationships, real or imagined. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Association](Association.md) | A typed association between two entities, supported by evidence |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | A relationship between two anatomical entities where the relationship is ontogenic, i.e. the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | An association between an mixture behavior and a behavioral feature manifested by the individual exhibited or has exhibited the behavior. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e.g. an impact of on its abundance, activity, localization, processing, expression, etc.) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | A regulatory relationship between two genes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes a physical interaction between a chemical entity and a gene or gene product. Any biological or chemical effect resulting from such an interaction are out of scope, and covered by the ChemicalAffectsGeneAssociation type (e.g. impact of a chemical on the abundance, activity, structure, etc, of either participant in the interaction) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic feature where the disesae or phenotypic feature is a secondary undesirable effect. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | This association defines a relationship between a chemical or treatment (or procedure) and a disease or phenotypic feature where the disesae or phenotypic feature is a secondary, typically (but not always) undesirable effect. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
  IF
  R has-input C1 AND
  R has-output C2 AND
  R enabled-by P AND
  R type Reaction
  THEN
  C1 derives-into C2 <<catalyst qualifier P>> |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | An interaction between a chemical entity and a biological process or pathway. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContributorAssociation](ContributorAssociation.md) | Any association between an entity (such as a publication) and various agents that contribute to its realisation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | An association between either a disease or a phenotypic feature and its mode of (genetic) inheritance. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | An association between an exposure event and a disease. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugToGeneAssociation](DrugToGeneAssociation.md) | An interaction between a drug and a gene or gene product. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FunctionalAssociation](FunctionalAssociation.md) | An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGoTermAssociation](GeneToGoTermAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | An association between a gene and a gene expression site, possibly qualified by stage/timing info. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneAssociation](GeneToGeneAssociation.md) | abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | Indicates that two genes are co-expressed, generally under the same conditions. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | An interaction at the molecular level between two physical entities |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | Set membership of a gene in a family of genes related by common evolutionary ancestry usually inferred by sequence comparisons. The genes in a given family generally share common sequence motifs which generally map onto shared gene product structure-function relationships. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToPathwayAssociation](GeneToPathwayAssociation.md) | An interaction between a gene or gene product and a biological process or pathway. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | Any association between one genotype and a genotypic entity that is a sub-component of it |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | Any association between a genotype and a sequence variant. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | association between a named thing and a information content entity where the specific context of the relationship between that named thing and the publication is unknown. For example, model organisms databases often capture the knowledge that a gene is found in a journal article, but not specifically the context in which that gene was documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be used. Conversely, for more specific associations (like 'gene to disease association', the publication should be captured as an edge property). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | An association between a material sample and the material entity from which it is derived. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | An association between a material sample and a disease or phenotype. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | Added in response to capturing relationship between microbiome activities as measured via measurements of blood analytes as collected via blood and stool samples |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | Association that holds the relationship between a reaction and the pathway it participates in. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | A relationship between two organism taxon nodes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | An interaction relationship between two taxa. This may be a symbiotic relationship (encompassing mutualism and parasitism), or it may be non-symbiotic. Example: plague transmitted_by flea; cattle domesticated_by Homo sapiens; plague infects Homo sapiens |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | A child-parent relationship between two taxa. For example: Homo sapiens subclass_of Homo |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | An association between a two populations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceAssociation](SequenceAssociation.md) | An association between a sequence feature and a nucleic acid entity it is localized to. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceFeatureRelationship](SequenceFeatureRelationship.md) | For example, a particular exon is part of a particular transcript or gene |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | A transcript is formed from multiple exons |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | A gene is transcribed and potentially translated to a gene product |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | A gene is a collection of transcripts |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToGeneAssociation](VariantToGeneAssociation.md) | An association between a variant and a gene, where the variant has a genetic association with the gene (i.e. is in linkage disequilibrium) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | An association between a variant and expression of a gene (i.e. e-QTL) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has particular frequency in the population |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Checksum](Checksum.md) | Checksum values associated with digital entities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NamedThing](NamedThing.md) | a databased entity or concept/class |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Activity](Activity.md) | An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Study](Study.md) | a detailed investigation and/or analysis |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AdministrativeEntity](AdministrativeEntity.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Agent](Agent.md) | person, group, organization or project that provides a piece of information (i.e. a knowledge association) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Attribute](Attribute.md) | A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BehavioralExposure](BehavioralExposure.md) | A behavioral exposure is a factor relating to behavior impacting an individual. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalSex](BiologicalSex.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenotypicSex](GenotypicSex.md) | An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypicSex](PhenotypicSex.md) | An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BioticExposure](BioticExposure.md) | An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalExposure](ChemicalExposure.md) | A chemical exposure is an intake of a particular chemical entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugExposure](DrugExposure.md) | A drug exposure is an intake of a particular drug. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | drug to gene interaction exposure is a drug exposure is where the interactions of the drug with specific genes are known to constitute an 'exposure' to the organism, leading to or influencing an outcome. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalRole](ChemicalRole.md) | 	A role played by the molecular entity or part thereof within a chemical context. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalAttribute](ClinicalAttribute.md) | Attributes relating to a clinical manifestation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalCourse](ClinicalCourse.md) | The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Onset](Onset.md) | The age group in which (disease) symptom manifestations appear |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalMeasurement](ClinicalMeasurement.md) | A clinical measurement is a special kind of attribute which results from a laboratory observation from a subject individual or sample. Measurements can be connected to their subject by the 'has attribute' slot. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalModifier](ClinicalModifier.md) | Used to characterize and specify the phenotypic abnormalities defined in the phenotypic abnormality sub-ontology, with respect to severity, laterality, and other aspects |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComplexChemicalExposure](ComplexChemicalExposure.md) | A complex chemical exposure is an intake of a chemical mixture (e.g. gasoline), other than a drug. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | A disease or phenotypic feature state, when viewed as an exposure, represents an precondition, leading to or influencing an outcome, e.g. HIV predisposing an individual to infections; a relative deficiency of skin pigmentation predisposing an individual to skin cancer. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentalExposure](EnvironmentalExposure.md) | A environmental exposure is a factor relating to abiotic processes in the environment including sunlight (UV-B), atmospheric (heat, cold, general pollution) and water-born contaminants. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeographicExposure](GeographicExposure.md) | A geographic exposure is a factor relating to geographic proximity to some impactful entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismAttribute](OrganismAttribute.md) | describes a characteristic of an organismal entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypicQuality](PhenotypicQuality.md) | A property of a phenotype |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | An abnormal anatomical structure, when viewed as an exposure, representing an precondition, leading to or influencing an outcome, e.g. thrombosis leading to an ischemic disease outcome. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathologicalProcessExposure](PathologicalProcessExposure.md) | A pathological process, when viewed as an exposure, representing a precondition, leading to or influencing an outcome, e.g. autoimmunity leading to disease. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SeverityValue](SeverityValue.md) | describes the severity of a phenotypic feature or disease |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SocioeconomicAttribute](SocioeconomicAttribute.md) | Attributes relating to a socioeconomic manifestation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SocioeconomicExposure](SocioeconomicExposure.md) | A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Zygosity](Zygosity.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalEntity](BiologicalEntity.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiologicalProcess](BiologicalProcess.md) | One or more causally connected executions of molecular functions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Behavior](Behavior.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathologicalProcess](PathologicalProcess.md) | A biologic function or a process having an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pathway](Pathway.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhysiologicalProcess](PhysiologicalProcess.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularActivity](MolecularActivity.md) | An execution of a molecular function carried out by a gene product or macromolecular complex. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.  Please see definitions of phenotypic feature and disease in this model for their independent descriptions.  This class is helpful to enforce domains and ranges   that may involve either a disease or a phenotypic feature. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Disease](Disease.md) | A disorder of structure or function, especially one that produces specific  signs, phenotypes or symptoms or that affects a specific location and is not simply a  direct result of physical injury.  A disposition to undergo pathological processes that exists in an  organism because of one or more disorders in that organism. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhenotypicFeature](PhenotypicFeature.md) | A combination of entity and quality that makes up a phenotyping statement. An observable characteristic of an  individual resulting from the interaction of its genotype with its molecular and physical environment. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BehavioralFeature](BehavioralFeature.md) | A phenotypic feature which is behavioral in nature. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalFinding](ClinicalFinding.md) | this category is currently considered broad enough to tag clinical lab measurements and other biological attributes taken as 'clinical traits' with some statistical score, for example, a p value in genetic associations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneAnnotation](GeneAnnotation.md) | An annotation describing the location, boundaries, and functions of  individual genes within a genome annotation. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneFamily](GeneFamily.md) | any grouping of multiple genes or gene products related by common descent |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneticInheritance](GeneticInheritance.md) | The pattern or 'mode' in which a particular genetic trait or disorder is passed from one generation to the next, e.g. autosomal dominant, autosomal recessive, etc. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Genome](Genome.md) | A genome is the sum of genetic material within a cell or virion. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GenomeAnnotation](GenomeAnnotation.md) | Location and nomenclature of genes and all of the coding regions in a genome assembly  and the classification of genes and transcripts into types. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Genotype](Genotype.md) | An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Haplotype](Haplotype.md) | A set of zero or more Alleles on a single instance of a Sequence[VMC] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MacromolecularComplex](MacromolecularComplex.md) | A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | A linear nucleotide sequence pattern that is widespread and has, or is conjectured to have, a biological significance. e.g. the TATA box promoter motif, transcription factor binding consensus sequences. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleosomeModification](NucleosomeModification.md) | A chemical modification of a histone protein within a nucleosome octomer or a substitution of a histone with a variant histone isoform. e.g. Histone 4 Lysine 20 methylation (H4K20me), histone variant H2AZ substituting H2A. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismalEntity](OrganismalEntity.md) | A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding chemical entities |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AnatomicalEntity](AnatomicalEntity.md) | A subcellular location, cell type or gross anatomical part |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Cell](Cell.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellularComponent](CellularComponent.md) | A location in or around a cell |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GrossAnatomicalStructure](GrossAnatomicalStructure.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | An anatomical structure with the potential of have an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bacterium](Bacterium.md) | A member of a group of unicellular microorganisms lacking a nuclear membrane, that reproduce by binary fission and are often motile. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellLine](CellLine.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellularOrganism](CellularOrganism.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fungus](Fungus.md) | A kingdom of eukaryotic, heterotrophic organisms that live as saprobes or parasites,  including mushrooms, yeasts, smuts, molds, etc. They reproduce either sexually or asexually, and have life cycles that range from simple to complex. Filamentous  fungi refer to those that grow as multicellular colonies (mushrooms and molds). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Invertebrate](Invertebrate.md) | An animal lacking a vertebral column. This group consists of 98% of all animal species. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Mammal](Mammal.md) | A member of the class Mammalia, a clade of endothermic amniotes distinguished from reptiles and birds by the possession of hair, three middle ear bones, mammary glands, and a neocortex |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Human](Human.md) | A member of the the species Homo sapiens. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Plant](Plant.md) |  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Vertebrate](Vertebrate.md) | A sub-phylum of animals consisting of those having a bony or cartilaginous vertebral column. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IndividualOrganism](IndividualOrganism.md) | An instance of an organism. For example, Richard Nixon, Charles Darwin, my pet cat. Example ID: ORCID:0000-0002-5355-2576 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Case](Case.md) | An individual (human) organism that has a patient role in some clinical context. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LifeStage](LifeStage.md) | A stage of development or growth of an organism, including post-natal adult stages |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StudyPopulation](StudyPopulation.md) | A group of people banded together or treated as a group as participants in a research study. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Cohort](Cohort.md) | A group of people banded together or treated as a group who share common characteristics. A cohort 'study' is a particular form of longitudinal study that samples a cohort, performing a cross-section at intervals through time. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Virus](Virus.md) | A virus is a microorganism that replicates itself as a microRNA and infects the host cell. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Polypeptide](Polypeptide.md) | A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Protein](Protein.md) | A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinIsoform](ProteinIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/ |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PosttranslationalModification](PosttranslationalModification.md) | A chemical modification of a polypeptide or protein that occurs after translation.  e.g. polypeptide cleavage to form separate proteins, methylation or acetylation of histone tail amino acids,  protein ubiquitination. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinDomain](ProteinDomain.md) | A conserved part of protein sequence and (tertiary) structure that can evolve, function, and exist independently of the rest of the protein chain. Protein domains maintain their structure and function independently of the proteins in which they are found. e.g. an SH3 domain. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinFamily](ProteinFamily.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ReagentTargetedGene](ReagentTargetedGene.md) | A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RegulatoryRegion](RegulatoryRegion.md) | A region (or regions) of the genome that contains known or putative regulatory elements that act in cis- or trans- to affect the transcription of gene |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AccessibleDnaRegion](AccessibleDnaRegion.md) | A region (or regions) of a chromatinized genome that has been measured to be more accessible to an enzyme such as DNase-I or Tn5 Transpose |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | A region (or regions) of the genome that contains a region of DNA known or predicted to bind a protein that modulates gene transcription |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibiting one or more sequence_alteration. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Snv](Snv.md) | SNVs are single nucleotide positions in genomic DNA at which different sequence alternatives exist |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemistry. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular entities. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more molecular entities with unknown concentration and stoichiometry. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Food](Food.md) | A substance consumed by a living organism as a source of nutrition |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular entities with known concentration and stoichiometry. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Drug](Drug.md) | A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessedMaterial](ProcessedMaterial.md) | A chemical entity (often a mixture) processed for consumption for nutritional, medical or technical use. Is a material entity that is created or changed during material processing. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FoodAdditive](FoodAdditive.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently bonded atoms. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CodingSequence](CodingSequence.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Exon](Exon.md) | A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Transcript](Transcript.md) | An RNA synthesized on a DNA or RNA template by an RNA polymerase. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RNAProduct](RNAProduct.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NoncodingRNAProduct](NoncodingRNAProduct.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MicroRNA](MicroRNA.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SiRNA](SiRNA.md) | A small RNA molecule that is the product of a longer exogenous or endogenous dsRNA, which is either a bimolecular duplex or very long hairpin, processed (via the Dicer pathway) such that numerous siRNAs accumulate from both strands of the dsRNA. SRNAs trigger the cleavage of their target molecules. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RNAProductIsoform](RNAProductIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference RNA |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalEntity](ClinicalEntity.md) | Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalIntervention](ClinicalIntervention.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Hospitalization](Hospitalization.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ClinicalTrial](ClinicalTrial.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Device](Device.md) | A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiagnosticAid](DiagnosticAid.md) | A device or substance used to help diagnose disease or injury |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Event](Event.md) | Something that happens at a given place and time. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InformationContentEntity](InformationContentEntity.md) | a piece of information that typically describes some topic of discourse or is used as support. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CommonDataElement](CommonDataElement.md) | A Common Data Element (CDE) is a standardized, precisely defined question, paired with a set of allowable  responses, used systematically across different sites, studies, or clinical trials to ensure consistent  data collection. Multiple CDEs (from one or more Collections) can be curated into Forms.  (https://cde.nlm.nih.gov/home) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConfidenceLevel](ConfidenceLevel.md) | Level of confidence in a statement |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dataset](Dataset.md) | an item that refers to a collection of data from a data source. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DatasetDistribution](DatasetDistribution.md) | an item that holds distribution level information about a dataset. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DatasetSummary](DatasetSummary.md) | an item that holds summary level information about a dataset. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DatasetVersion](DatasetVersion.md) | an item that holds version level information about a dataset. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EvidenceType](EvidenceType.md) | Class of evidence that supports an association |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Publication](Publication.md) | Any ‘published’ piece of information. Publications are considered broadly  to include any document or document part made available in print or on the  web - which may include scientific journal issues, individual articles, and  books - as well as things like pre-prints, white papers, patents, drug  labels, web pages, protocol documents,  and even a part of a publication if  of significant knowledge scope (e.g. a figure, figure legend, or section  highlighted by NLP).  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone  section of a larger publication	   |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published  in an issue of a scientific journal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Book](Book.md) | This class may rarely be instantiated except if use cases of a given knowledge graph support its utility. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BookChapter](BookChapter.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DrugLabel](DrugLabel.md) | a document accompanying a drug or its container that provides written, printed or graphic information about the drug, including drug contents, specific instructions  or warnings for administration, storage and disposal instructions, etc.  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Patent](Patent.md) | a legal document granted by a patent issuing authority which confers upon  the patenter the sole right to make, use and sell an invention for a set period of time.  |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PreprintPublication](PreprintPublication.md) | a document reresenting an early version of an author's original scholarly work,  such as a research paper or a review, prior to formal peer review and publication  in a peer-reviewed scholarly or scientific journal. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledge graph support its utility. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WebPage](WebPage.md) | a document that is published according to World Wide Web standards, which  may incorporate text, graphics, sound, and/or other features. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RetrievalSource](RetrievalSource.md) | Provides information about how a particular InformationResource served as a source from which knowledge expressed in an Edge, or data used to generate this knowledge, was retrieved. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StudyResult](StudyResult.md) | A collection of data items from a study that are about a particular study subject or experimental unit (the  'focus' of the Result) - optionally with context/provenance metadata that may be relevant to the interpretation of this data as evidence. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) | A result of a chi squared analysis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) | A result of a concept count analysis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LogOddsAnalysisResult](LogOddsAnalysisResult.md) | A result of a log odds ratio analysis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) | A result of a observed expected frequency analysis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) | A result of a relative frequency analysis. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TextMiningResult](TextMiningResult.md) | A result of text mining. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StudyVariable](StudyVariable.md) | a variable that is used as a measure in the investigation of a study |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OrganismTaxon](OrganismTaxon.md) | A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Phenomenon](Phenomenon.md) | a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhysicalEntity](PhysicalEntity.md) | An entity that has material reality (a.k.a. physical essence). |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MaterialSample](MaterialSample.md) | A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO] |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PlanetaryEntity](PlanetaryEntity.md) | Any entity or process that exists at the level of the whole planet |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentalFeature](EnvironmentalFeature.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EnvironmentalProcess](EnvironmentalProcess.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeographicLocation](GeographicLocation.md) | a location that can be described in lat/long coordinates |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeographicLocationAtTime](GeographicLocationAtTime.md) | a location that can be described in lat/long coordinates, for a particular time |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Procedure](Procedure.md) | A series of actions conducted in a certain order or manner |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures', medical devices and/or procedures |
| [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md) | None |
| [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md) | An association between some entity and an exposure event. |
| [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md) | An association between some entity and an outcome |
| [EpidemiologicalOutcome](EpidemiologicalOutcome.md) | An epidemiological outcome, such as societal disease burden, resulting from an exposure event. |
| [EpigenomicEntity](EpigenomicEntity.md) | None |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | Qualifier for frequency type associations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | Qualifiers for entity to disease or phenotype associations. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | mixin class for any association whose object (target node) is a disease |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | None |
| [GeneExpressionMixin](GeneExpressionMixin.md) | Observed gene expression intensity, context (site, stage) and associated phenotypic status within which the expression occurs. |
| [GeneGroupingMixin](GeneGroupingMixin.md) | any grouping of multiple genes or gene products |
| [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md) | None |
| [GenomeAssembly](GenomeAssembly.md) | Genome assembly to contain version and label information |
| [GenomicEntity](GenomicEntity.md) | None |
| [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md) | None |
| [HospitalizationOutcome](HospitalizationOutcome.md) | An outcome resulting from an exposure event which is the increased manifestation of acute (e.g. emergency room visit) or chronic (inpatient) hospitalization. |
| [MacromolecularMachineMixin](MacromolecularMachineMixin.md) | A union of gene locus, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneOrGeneProduct](GeneOrGeneProduct.md) | A union of gene loci or gene products. Frequently an identifier for one will be used as proxy for another |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneProductMixin](GeneProductMixin.md) | The functional molecular product of a single gene locus. Gene products are either proteins or functional RNA molecules. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneProductIsoformMixin](GeneProductIsoformMixin.md) | This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms. |
| [MacromolecularMachineToEntityAssociationMixin](MacromolecularMachineToEntityAssociationMixin.md) | an association which has a macromolecular machine mixin as a subject |
| [Mapping](Mapping.md) | text |
| [MappingCollection](MappingCollection.md) | A collection of deprecated mappings. |
| [Mappings](Mappings.md) | A collection of mappings between identifiers
 |
| [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) | An association between a material sample and something. |
| [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) | This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease |
| [MortalityOutcome](MortalityOutcome.md) | An outcome of death from resulting from an exposure event. |
| [OntologyClass](OntologyClass.md) | a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExposureEvent](ExposureEvent.md) | A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelationshipType](RelationshipType.md) | An OWL property used as an edge label |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TaxonomicRank](TaxonomicRank.md) | A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom) |
| [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md) | An association between an organism taxon and another entity |
| [Outcome](Outcome.md) | An entity that has the role of being the consequence of an exposure event. This is an abstract mixin grouping of various categories of possible biological or non-biological (e.g. clinical) outcomes. |
| [PathologicalAnatomicalOutcome](PathologicalAnatomicalOutcome.md) | An outcome resulting from an exposure event which is the manifestation of an abnormal anatomical structure. |
| [PathologicalEntityMixin](PathologicalEntityMixin.md) | A pathological (abnormal) structure or process. |
| [PathologicalProcessOutcome](PathologicalProcessOutcome.md) | An outcome resulting from an exposure event which is the manifestation of a pathological process. |
| [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md) | Either a physical or processual entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Occurrent](Occurrent.md) | A processual entity. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ActivityAndBehavior](ActivityAndBehavior.md) | Activity or behavior of any independent integral living, organization or mechanical actor in the world |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PhysicalEssence](PhysicalEssence.md) | Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge. |
| [PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and an example of the rewiring that should be done to use a qualified statement in its place. |
| [RelationshipQuantifier](RelationshipQuantifier.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FrequencyQuantifier](FrequencyQuantifier.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SensitivityQuantifier](SensitivityQuantifier.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SpecificityQuantifier](SpecificityQuantifier.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PathognomonicityQuantifier](PathognomonicityQuantifier.md) | A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease |
| [SocioeconomicOutcome](SocioeconomicOutcome.md) | An general social or economic outcome, such as healthcare costs, utilization, etc., resulting from an exposure event |
| [SubjectOfInvestigation](SubjectOfInvestigation.md) | An entity that has the role of being studied in an investigation, study, or experiment |
| [ThingWithTaxon](ThingWithTaxon.md) | A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes |
| [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) | None |



## Slots

| Slot | Description |
| --- | --- |
| [access_date](access_date.md) |  |
| [active_in](active_in.md) |  |
| [actively_involved_in](actively_involved_in.md) | holds between a continuant and a process or function, where the continuant ac... |
| [actively_involves](actively_involves.md) |  |
| [acts_upstream_of](acts_upstream_of.md) |  |
| [acts_upstream_of_negative_effect](acts_upstream_of_negative_effect.md) |  |
| [acts_upstream_of_or_within](acts_upstream_of_or_within.md) |  |
| [acts_upstream_of_or_within_negative_effect](acts_upstream_of_or_within_negative_effect.md) |  |
| [acts_upstream_of_or_within_positive_effect](acts_upstream_of_or_within_positive_effect.md) |  |
| [acts_upstream_of_positive_effect](acts_upstream_of_positive_effect.md) |  |
| [address](address.md) | the particulars of the place where someone or an organization is situated |
| [adjusted_p_value](adjusted_p_value.md) | The adjusted p-value is the probability of obtaining test results at least as... |
| [adverse_event_of](adverse_event_of.md) |  |
| [affected_by](affected_by.md) | describes an entity of which the state or quality is affected by another exis... |
| [affects](affects.md) | describes an entity that has a direct affect on the state or quality of anoth... |
| [affects_response_to](affects_response_to.md) |  |
| [affects_risk_for](affects_risk_for.md) | holds between two entities where exposure to one entity alters the chance of ... |
| [affiliation](affiliation.md) | a professional relationship between one provider (often a person) within anot... |
| [aggregate_statistic](aggregate_statistic.md) |  |
| [aggregator_knowledge_source](aggregator_knowledge_source.md) | An intermediate aggregator resource from which knowledge expressed in an Asso... |
| [ameliorates](ameliorates.md) | A relationship between an entity (e |
| [amount_or_activity_decreased_by](amount_or_activity_decreased_by.md) |  |
| [amount_or_activity_increased_by](amount_or_activity_increased_by.md) |  |
| [anatomical_context_qualifier](anatomical_context_qualifier.md) | A statement qualifier representing an anatomical location where an relationsh... |
| [animal_model_available_from](animal_model_available_from.md) |  |
| [annotations](annotations.md) |  |
| [aspect_qualifier](aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [assesses](assesses.md) | The effect of a thing on a target was interrogated in some assay |
| [associated_environmental_context](associated_environmental_context.md) | An attribute that can be applied to an association where the association hold... |
| [associated_with](associated_with.md) | Expresses a relationship between two named things where the relationship is t... |
| [associated_with_decreased_likelihood_of](associated_with_decreased_likelihood_of.md) | Expresses a relationship between two named things where the relationship is t... |
| [associated_with_increased_likelihood_of](associated_with_increased_likelihood_of.md) | Expresses a relationship between two named things where the relationship is t... |
| [associated_with_likelihood_of](associated_with_likelihood_of.md) | A a relationship that holds between two concepts represented by variables for... |
| [associated_with_resistance_to](associated_with_resistance_to.md) | A relation that holds between a named thing and a chemical that specifies tha... |
| [associated_with_sensitivity_to](associated_with_sensitivity_to.md) | A relation that holds between a named thing and a chemical that specifies tha... |
| [association_slot](association_slot.md) | any slot that relates an association to another entity |
| [author](author.md) | an instance of one (co-)creator primarily responsible for a written work |
| [authority](authority.md) |  |
| [authors](authors.md) | connects an publication to the list of authors who contributed to the publica... |
| [available_from](available_from.md) |  |
| [base_coordinate](base_coordinate.md) | A position in the base coordinate system |
| [binds](binds.md) | A causal mechanism mediated by the direct contact between effector and target... |
| [biological_role_mixin](biological_role_mixin.md) | A role played by the chemical entity or part thereof within a biological cont... |
| [biomarker_for](biomarker_for.md) | holds between a measurable chemical entity and a disease or phenotypic featur... |
| [bonferonni_adjusted_p_value](bonferonni_adjusted_p_value.md) | The Bonferroni correction is an adjustment made to P values when several depe... |
| [broad_match](broad_match.md) | a list of terms from different schemas or terminology systems that have a bro... |
| [broad_matches](broad_matches.md) | A list of terms from different schemas or terminology systems that have a bro... |
| [broad_synonym](broad_synonym.md) |  |
| [can_be_carried_out_by](can_be_carried_out_by.md) |  |
| [capable_of](capable_of.md) | holds between a physical entity and process or function, where the continuant... |
| [catalyst_qualifier](catalyst_qualifier.md) | a qualifier that connects an association between two causally connected entit... |
| [catalyzes](catalyzes.md) |  |
| [category](category.md) | Name of the high level ontology class in which this entity is categorized |
| [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | A statement qualifier representing a type of molecular control mechanism thro... |
| [caused_by](caused_by.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [causes](causes.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [chapter](chapter.md) | chapter of a book |
| [checksum_algorithm](checksum_algorithm.md) |  |
| [chemical_role_mixin](chemical_role_mixin.md) | A role played by the chemical entity or part thereof within a chemical contex... |
| [chemically_similar_to](chemically_similar_to.md) | holds between one small molecule entity and another that it approximates for ... |
| [chi_squared_statistic](chi_squared_statistic.md) | represents the chi-squared statistic computed from observations |
| [clinical_modifier_qualifier](clinical_modifier_qualifier.md) | the method or process of administering a pharmaceutical compound to achieve a... |
| [close_match](close_match.md) | a list of terms from different schemas or terminology systems that have a sem... |
| [coexists_with](coexists_with.md) | holds between two entities that are co-located in the same aggregate object, ... |
| [coexpressed_with](coexpressed_with.md) | holds between any two genes or gene products, in which both are generally exp... |
| [colocalizes_with](colocalizes_with.md) | holds between two entities that are observed to be located in the same place |
| [completed_by](completed_by.md) |  |
| [composed_primarily_of](composed_primarily_of.md) | x composed_primarily_of_y if:more than half of the mass of x is made from par... |
| [concept_count_object](concept_count_object.md) | The number of instances in a dataset/cohort whose records contain the concept... |
| [concept_count_subject](concept_count_subject.md) | The number of instances in a dataset/cohort whose records contain the concept... |
| [concept_pair_count](concept_pair_count.md) | The number of instances in a dataset/cohort whose records contain both the su... |
| [condition_associated_with_gene](condition_associated_with_gene.md) | holds between a gene and a disease or phenotypic feature that may be influenc... |
| [consumed_by](consumed_by.md) |  |
| [consumes](consumes.md) |  |
| [contains_process](contains_process.md) |  |
| [content_url](content_url.md) |  |
| [context_qualifier](context_qualifier.md) | Restricts the setting/context/location where the core concept (or qualified c... |
| [contraindicated_for](contraindicated_for.md) | Holds between a drug and a disease or phenotype, such that a person with that... |
| [contributes_to](contributes_to.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [contribution_from](contribution_from.md) |  |
| [contributor](contributor.md) |  |
| [correlated_with](correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [created_with](created_with.md) |  |
| [creation_date](creation_date.md) | date on which an entity was created |
| [creation_date](creation_date.md) |  |
| [dataset_count](dataset_count.md) | The total number of instances (e |
| [dataset_download_url](dataset_download_url.md) |  |
| [decreased_amount_in](decreased_amount_in.md) |  |
| [decreased_likelihood_associated_with](decreased_likelihood_associated_with.md) |  |
| [decreases_amount_or_activity_of](decreases_amount_or_activity_of.md) | A grouping mixin to help with searching for all the predicates that decrease ... |
| [decreases_response_to](decreases_response_to.md) | holds between two chemical entities where the action or effect of one decreas... |
| [derivative_qualifier](derivative_qualifier.md) | A qualifier that composes with a core subject/object  concept to describe som... |
| [derives_from](derives_from.md) | holds between two distinct material entities, the new entity and the old enti... |
| [derives_into](derives_into.md) | holds between two distinct material entities, the old entity and the new enti... |
| [description](description.md) | a human-readable description of an entity |
| [develops_from](develops_from.md) |  |
| [develops_into](develops_into.md) |  |
| [diagnoses](diagnoses.md) | a relationship that identifies the nature of (an illness or other problem) by... |
| [digest](digest.md) |  |
| [direction_qualifier](direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [directly_physically_interacts_with](directly_physically_interacts_with.md) | A causal mechanism mediated by a direct contact between the effector and targ... |
| [disease_has_basis_in](disease_has_basis_in.md) | A relation that holds between a disease and an entity where the state of the ... |
| [disease_has_location](disease_has_location.md) | A relationship between a disease and an anatomical entity where the disease h... |
| [disrupted_by](disrupted_by.md) | describes a relationship where the structure, function, or occurrence of one ... |
| [disrupts](disrupts.md) | describes a relationship where one entity degrades or interferes with the str... |
| [distribution_download_url](distribution_download_url.md) |  |
| [download_url](download_url.md) |  |
| [drug_regulatory_status_world_wide](drug_regulatory_status_world_wide.md) | An agglomeration of drug regulatory status worldwide |
| [editor](editor.md) | editor of a compiled work such as a book or a periodical (newspaper or an aca... |
| [enabled_by](enabled_by.md) | holds between a process and a physical entity, where the physical entity exec... |
| [enables](enables.md) | holds between a physical entity and a process, where the physical entity exec... |
| [end_coordinate](end_coordinate.md) | The position at which the subject genomic entity ends on the chromosome or ot... |
| [end_interbase_coordinate](end_interbase_coordinate.md) | The position at which the subject nucleic acid entity ends on the chromosome ... |
| [evidence_count](evidence_count.md) | The number of evidence instances that are connected to an association |
| [exacerbates](exacerbates.md) | A relationship between an entity (e |
| [exact_match](exact_match.md) | holds between two entities that have strictly equivalent meanings, with a hig... |
| [exact_matches](exact_matches.md) | A list of terms from different schemas or terminology systems that have an id... |
| [exact_synonym](exact_synonym.md) |  |
| [expected_count](expected_count.md) | The expected (calculated) number of instances in a dataset/cohort whose recor... |
| [expressed_in](expressed_in.md) | holds between a gene or gene product and an anatomical entity in which it is ... |
| [expresses](expresses.md) | holds between an anatomical entity and gene or gene product that is expressed... |
| [expression_site](expression_site.md) | location in which gene or protein expression takes place |
| [extraction_confidence_score](extraction_confidence_score.md) | A quantitative confidence value that represents the probability of obtaining ... |
| [FDA_adverse_event_level](FDA_adverse_event_level.md) |  |
| [FDA_approval_status](FDA_approval_status.md) |  |
| [food_component_of](food_component_of.md) | holds between a one or more chemical entities present in food, irrespective o... |
| [form_or_variant_qualifier](form_or_variant_qualifier.md) | A qualifier that composes with a core subject/object concept to define a spec... |
| [format](format.md) |  |
| [frequency_qualifier](frequency_qualifier.md) | a qualifier used in a phenotypic association to state how frequent the phenot... |
| [full_name](full_name.md) | a long-form human readable name for a thing |
| [gene_associated_with_condition](gene_associated_with_condition.md) | holds between a gene and a disease or phenotypic feature that the gene or its... |
| [gene_product_of](gene_product_of.md) | definition x has gene product of y if and only if y is a gene (SO:0000704) th... |
| [gene_fusion_with](gene_fusion_with.md) | holds between two independent genes that have fused through  translocation, i... |
| [gene_identifier_1](gene_identifier_1.md) |  |
| [gene_identifier_2](gene_identifier_2.md) |  |
| [genetic_association](genetic_association.md) |  |
| [genetic_neighborhood_of](genetic_neighborhood_of.md) | holds between two genes located nearby one another on a chromosome |
| [genetically_associated_with](genetically_associated_with.md) |  |
| [genetically_interacts_with](genetically_interacts_with.md) | holds between two genes whose phenotypic effects are dependent on each other ... |
| [genome_build](genome_build.md) | The version of the genome on which a feature is located |
| [genome_annotations](genome_annotations.md) |  |
| [genome_assemblies](genome_assemblies.md) |  |
| [has_active_component](has_active_component.md) |  |
| [has_active_ingredient](has_active_ingredient.md) | holds between a drug and a molecular entity in which the latter is a part of ... |
| [has_adverse_event](has_adverse_event.md) | An untoward medical occurrence in a patient or clinical investigation subject... |
| [has_attribute](has_attribute.md) | connects any entity to an attribute |
| [has_attribute_type](has_attribute_type.md) | connects an attribute to a class that describes it |
| [has_author](has_author.md) |  |
| [has_biological_sequence](has_biological_sequence.md) | connects a genomic feature to its sequence |
| [has_biomarker](has_biomarker.md) | holds between a disease or phenotypic feature and a measurable chemical entit... |
| [has_catalyst](has_catalyst.md) |  |
| [has_chemical_formula](has_chemical_formula.md) | description of chemical compound based on element symbols |
| [has_chemical_role](has_chemical_role.md) | A role is particular behaviour which a chemical entity may exhibit |
| [has_completed](has_completed.md) | holds between an entity and a process that the entity is capable of and has c... |
| [has_confidence_level](has_confidence_level.md) | connects an association to a qualitative term denoting the level of confidenc... |
| [has_constituent](has_constituent.md) | one or more molecular entities within a chemical mixture |
| [has_contraindication](has_contraindication.md) |  |
| [has_contributor](has_contributor.md) |  |
| [has_count](has_count.md) | number of things with a particular property |
| [has_dataset](has_dataset.md) |  |
| [has_decreased_amount](has_decreased_amount.md) |  |
| [has_device](has_device.md) | connects an entity to one or more (medical) devices |
| [has_distribution](has_distribution.md) |  |
| [has_drug](has_drug.md) | connects an entity to one or more drugs |
| [has_editor](has_editor.md) |  |
| [has_evidence](has_evidence.md) | connects an association to an instance of supporting evidence |
| [has_excipient](has_excipient.md) | holds between a drug and a molecular entities in which the latter is a part o... |
| [has_food_component](has_food_component.md) | holds between food and one or more chemical entities composing it, irrespecti... |
| [has_frameshift_variant](has_frameshift_variant.md) |  |
| [has_gene](has_gene.md) | connects an entity associated with one or more genes |
| [has_gene_or_gene_product](has_gene_or_gene_product.md) | connects an entity with one or more gene or gene products |
| [has_gene_product](has_gene_product.md) | holds between a gene and a transcribed and/or translated product generated fr... |
| [has_increased_amount](has_increased_amount.md) |  |
| [has_input](has_input.md) | holds between a process and a continuant, where the continuant is an input in... |
| [has_manifestation](has_manifestation.md) |  |
| [has_member](has_member.md) | Defines a mereological relation between a collection and an item |
| [has_metabolite](has_metabolite.md) | holds between two molecular entities in which the second one is derived from ... |
| [has_missense_variant](has_missense_variant.md) |  |
| [has_mode_of_inheritance](has_mode_of_inheritance.md) | Relates a disease or phenotypic feature to its observed genetic segregation a... |
| [has_molecular_consequence](has_molecular_consequence.md) | connects a sequence variant to a class describing the molecular consequence |
| [has_nearby_variant](has_nearby_variant.md) |  |
| [has_negative_upstream_actor](has_negative_upstream_actor.md) |  |
| [has_negative_upstream_or_within_actor](has_negative_upstream_or_within_actor.md) |  |
| [has_non_coding_variant](has_non_coding_variant.md) |  |
| [has_nonsense_variant](has_nonsense_variant.md) |  |
| [has_not_completed](has_not_completed.md) | holds between an entity and a process that the entity is capable of, but has ... |
| [has_numeric_value](has_numeric_value.md) | connects a quantity value to a number |
| [has_nutrient](has_nutrient.md) | one or more nutrients which are growth factors for a living organism |
| [has_output](has_output.md) | holds between a process and a continuant, where the continuant is an output o... |
| [has_part](has_part.md) | holds between wholes and their parts (material entities or processes) |
| [has_participant](has_participant.md) | holds between a process and a continuant, where the continuant is somehow inv... |
| [has_percentage](has_percentage.md) | equivalent to has quotient multiplied by 100 |
| [has_phenotype](has_phenotype.md) | holds between a biological entity and a phenotype, where a phenotype is const... |
| [has_plasma_membrane_part](has_plasma_membrane_part.md) | Holds between a cell c and a protein complex or protein p if and only if that... |
| [has_positive_upstream_actor](has_positive_upstream_actor.md) |  |
| [has_positive_upstream_or_within_actor](has_positive_upstream_or_within_actor.md) |  |
| [has_predisposing_factor](has_predisposing_factor.md) |  |
| [has_procedure](has_procedure.md) | connects an entity to one or more (medical) procedures |
| [has_provider](has_provider.md) |  |
| [has_publisher](has_publisher.md) |  |
| [has_qualitative_value](has_qualitative_value.md) | connects an attribute to a value |
| [has_quantitative_value](has_quantitative_value.md) | connects an attribute to a value |
| [has_quotient](has_quotient.md) |  |
| [has_receptor](has_receptor.md) | the organism or organism part being exposed |
| [has_route](has_route.md) | the process that results in the stressor coming into direct contact with the ... |
| [has_sequence_location](has_sequence_location.md) | holds between two nucleic acid entities when the subject can be localized in ... |
| [has_sequence_variant](has_sequence_variant.md) |  |
| [has_side_effect](has_side_effect.md) | An unintended, but predictable, secondary effect shown to be correlated with ... |
| [has_splice_site_variant](has_splice_site_variant.md) |  |
| [has_stressor](has_stressor.md) | the process or entity that the receptor is being exposed to |
| [has_substrate](has_substrate.md) |  |
| [has_supporting_study_result](has_supporting_study_result.md) | connects an association to an instance of supporting study result |
| [has_synonymous_variant](has_synonymous_variant.md) |  |
| [has_target](has_target.md) |  |
| [has_taxonomic_rank](has_taxonomic_rank.md) |  |
| [has_topic](has_topic.md) | Connects a node to a vocabulary term or ontology class that describes some as... |
| [has_total](has_total.md) | total number of things in a particular reference set |
| [has_unit](has_unit.md) | connects a quantity value to a unit |
| [has_upstream_actor](has_upstream_actor.md) |  |
| [has_upstream_or_within_actor](has_upstream_or_within_actor.md) |  |
| [has_variant_part](has_variant_part.md) | holds between a nucleic acid entity and a nucleic acid entity that is a sub-c... |
| [has_zygosity](has_zygosity.md) |  |
| [highest_FDA_approval_status](highest_FDA_approval_status.md) | Should be the highest level of FDA approval this chemical entity or device ha... |
| [homologous_to](homologous_to.md) | holds between two biological entities that have common evolutionary origin |
| [id](id.md) | A unique identifier for an entity |
| [in_cell_population_with](in_cell_population_with.md) | holds between two genes or gene products that are expressed in the same cell ... |
| [in_complex_with](in_complex_with.md) | holds between two genes or gene products that are part of (or code for produc... |
| [in_linkage_disequilibrium_with](in_linkage_disequilibrium_with.md) | holds between two sequence variants, the presence of which are correlated in ... |
| [in_pathway_with](in_pathway_with.md) | holds between two genes or gene products that are part of in the same biologi... |
| [in_taxon](in_taxon.md) | connects an entity to its taxonomic classification |
| [in_taxon_label](in_taxon_label.md) | The human readable scientific name for the taxon of the entity |
| [increased_amount_of](increased_amount_of.md) |  |
| [increased_likelihood_associated_with](increased_likelihood_associated_with.md) |  |
| [increases_amount_or_activity_of](increases_amount_or_activity_of.md) | A grouping mixin to help with searching for all the predicates that increase ... |
| [increases_response_to](increases_response_to.md) | holds between two chemical entities where the action or effect of one increas... |
| [indirectly_physically_interacts_with](indirectly_physically_interacts_with.md) |  |
| [ingest_date](ingest_date.md) |  |
| [interacting_molecules_category](interacting_molecules_category.md) |  |
| [interacts_with](interacts_with.md) | holds between any two entities that directly or indirectly interact with each... |
| [interbase_coordinate](interbase_coordinate.md) | A position in interbase coordinates |
| [iri](iri.md) | An IRI for an entity |
| [is_active_ingredient_of](is_active_ingredient_of.md) | holds between a molecular entity and a drug, in which the former is a part of... |
| [is_ameliorated_by](is_ameliorated_by.md) |  |
| [is_assessed_by](is_assessed_by.md) |  |
| [is_diagnosed_by](is_diagnosed_by.md) |  |
| [is_exacerbated_by](is_exacerbated_by.md) |  |
| [is_excipient_of](is_excipient_of.md) | holds between a molecular entity and a drug in which the former is a part of ... |
| [is_frameshift_variant_of](is_frameshift_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant causes... |
| [is_input_of](is_input_of.md) |  |
| [is_metabolite](is_metabolite.md) | indicates whether a molecular entity is a metabolite |
| [is_metabolite_of](is_metabolite_of.md) | holds between two molecular entities in which the first one is derived from t... |
| [is_missense_variant_of](is_missense_variant_of.md) | holds between a gene  and a sequence variant, such the sequence variant resul... |
| [is_molecular_consequence_of](is_molecular_consequence_of.md) |  |
| [is_nearby_variant_of](is_nearby_variant_of.md) | holds between a sequence variant and a gene sequence that the variant is geno... |
| [is_non_coding_variant_of](is_non_coding_variant_of.md) | holds between a sequence variant and a gene, where the variant does not affec... |
| [is_nonsense_variant_of](is_nonsense_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant result... |
| [is_output_of](is_output_of.md) |  |
| [is_sequence_variant_of](is_sequence_variant_of.md) | holds between a sequence variant and a nucleic acid entity |
| [is_side_effect_of](is_side_effect_of.md) |  |
| [is_splice_site_variant_of](is_splice_site_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant is in ... |
| [is_substrate_of](is_substrate_of.md) |  |
| [is_supplement](is_supplement.md) |  |
| [is_synonymous_variant_of](is_synonymous_variant_of.md) | holds between a sequence variant and a gene, such the sequence variant is in ... |
| [is_toxic](is_toxic.md) |  |
| [iso_abbreviation](iso_abbreviation.md) | Standard abbreviation for periodicals in the International Organization for S... |
| [issue](issue.md) | issue of a newspaper, a scientific journal or magazine for reference purpose |
| [keywords](keywords.md) | keywords tagging a publication |
| [knowledge_source](knowledge_source.md) | An Information Resource from which the knowledge expressed in an Association ... |
| [label](label.md) |  |
| [lacks_part](lacks_part.md) |  |
| [latitude](latitude.md) | latitude |
| [license](license.md) |  |
| [likelihood_associated_with](likelihood_associated_with.md) |  |
| [ln_ratio](ln_ratio.md) | the natural log of the ratio of co-occurrence to expected |
| [ln_ratio_confidence_interval](ln_ratio_confidence_interval.md) | The 99% confidence interval for the ln_ratio calculation (i |
| [located_in](located_in.md) | holds between a material entity and a material entity or site within which it... |
| [location_of](location_of.md) | holds between material entity or site and a material entity that is located w... |
| [location_of_disease](location_of_disease.md) |  |
| [log_odds_ratio](log_odds_ratio.md) | The logarithm of the odds ratio, or the ratio of the odds of event Y occurrin... |
| [log_odds_ration_95_ci](log_odds_ration_95_ci.md) | The ninety-five percent confidence range in which the true log odds ratio for... |
| [logical_interpretation](logical_interpretation.md) |  |
| [longitude](longitude.md) | longitude |
| [manifestation_of](manifestation_of.md) | that part of a phenomenon which is directly observable or visibly expressed, ... |
| [mapped_predicate](mapped_predicate.md) | The predicate that is being replaced by the fully qualified representation of... |
| [max_tolerated_dose](max_tolerated_dose.md) | The highest dose of a drug or treatment that does not cause unacceptable side... |
| [mechanism_of_action](mechanism_of_action.md) | a boolean flag to indicate if the edge is part of a path or subgraph of a kno... |
| [member_of](member_of.md) | Defines a mereological relation between a item and a collection |
| [mentioned_by](mentioned_by.md) | refers to is a relation between one named thing and the information content e... |
| [mentions](mentions.md) | refers to is a relation between one information content entity and the named ... |
| [mesh_terms](mesh_terms.md) | mesh terms tagging a publication |
| [method](method.md) |  |
| [missing_from](missing_from.md) |  |
| [mode_of_inheritance_of](mode_of_inheritance_of.md) |  |
| [model_of](model_of.md) | holds between a thing and some other thing it approximates for purposes of sc... |
| [models](models.md) |  |
| [molecular_type](molecular_type.md) |  |
| [name](name.md) | A human-readable name for an attribute or entity |
| [narrow_match](narrow_match.md) | a list of terms from different schemas or terminology systems that have a nar... |
| [narrow_matches](narrow_matches.md) | A list of terms from different schemas or terminology systems that have a nar... |
| [narrow_synonym](narrow_synonym.md) |  |
| [negated](negated.md) | if set to true, then the association is negated i |
| [negatively_correlated_with](negatively_correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [node_property](node_property.md) | A grouping for any property that holds between a node and a value |
| [not_completed_by](not_completed_by.md) |  |
| [nutrient_of](nutrient_of.md) | holds between a one or more chemical entities present in food, irrespective o... |
| [object](object.md) | connects an association to the object of the association |
| [object_aspect_qualifier](object_aspect_qualifier.md) |  |
| [object_category](object_category.md) | Used to hold the biolink class/category of an association |
| [object_category_closure](object_category_closure.md) | Used to hold the object category closure of an association |
| [object_closure](object_closure.md) | Used to hold the object closure of an association |
| [object_context_qualifier](object_context_qualifier.md) |  |
| [object_derivative_qualifier](object_derivative_qualifier.md) |  |
| [object_direction_qualifier](object_direction_qualifier.md) |  |
| [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) |  |
| [object_label_closure](object_label_closure.md) | Used to hold the object label closure of an association |
| [object_location_in_text](object_location_in_text.md) | Character offsets for the text span(s) in the supporting text corresponding t... |
| [object_namespace](object_namespace.md) | Used to hold the object namespace of an association |
| [object_part_qualifier](object_part_qualifier.md) |  |
| [occurs_in](occurs_in.md) | holds between a process and a material entity or site within which the proces... |
| [occurs_in_disease](occurs_in_disease.md) |  |
| [occurs_together_in_literature_with](occurs_together_in_literature_with.md) | holds between two entities where their co-occurrence is correlated by counts ... |
| [onset_qualifier](onset_qualifier.md) | a qualifier used in a phenotypic association to state when the phenotype appe... |
| [opposite_of](opposite_of.md) | x is the opposite of y if there exists some distance metric M, and there exis... |
| [original_object](original_object.md) | used to hold the original object of a relation (or predicate) that an externa... |
| [original_predicate](original_predicate.md) | used to hold the original relation/predicate that an external knowledge sourc... |
| [original_subject](original_subject.md) | used to hold the original subject of a relation (or predicate) that an extern... |
| [orthologous_to](orthologous_to.md) | a homology relationship between entities (typically genes) that diverged afte... |
| [overlaps](overlaps.md) | holds between entities that overlap in their extents (materials or processes) |
| [p_value](p_value.md) | A quantitative confidence value that represents the probability of obtaining ... |
| [pages](pages.md) | page number of source referenced for statement or publication |
| [paralogous_to](paralogous_to.md) | a homology relationship that holds between entities (typically genes) that di... |
| [part_of](part_of.md) | holds between parts and wholes (material entities or processes) |
| [part_qualifier](part_qualifier.md) | defines a specific part/component of the core concept (used in cases there th... |
| [participates_in](participates_in.md) | holds between a continuant and a process, where the continuant is somehow inv... |
| [phase](phase.md) | The phase for a coding sequence entity |
| [phenotype_of](phenotype_of.md) |  |
| [phenotypic_state](phenotypic_state.md) | in experiments (e |
| [physically_interacts_with](physically_interacts_with.md) | holds between two entities that make physical contact as part of some interac... |
| [plasma_membrane_part_of](plasma_membrane_part_of.md) |  |
| [population_context_qualifier](population_context_qualifier.md) | a biological population (general, study, cohort, etc |
| [positively_correlated_with](positively_correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [preceded_by](preceded_by.md) | holds between two processes, where the other is completed before the one begi... |
| [precedes](precedes.md) | holds between two processes, where one completes before the other begins |
| [predicate](predicate.md) | A high-level grouping for the relationship type |
| [predicate_mappings](predicate_mappings.md) | A collection of relationships that are not used in biolink, but have biolink ... |
| [predisposes](predisposes.md) | holds between two entities where exposure to one entity increases the chance ... |
| [prevented_by](prevented_by.md) | holds between a potential outcome of which the likelihood was reduced by the ... |
| [prevents](prevents.md) | holds between an entity whose application or use reduces the likelihood of a ... |
| [primarily_composed_of](primarily_composed_of.md) |  |
| [primary_knowledge_source](primary_knowledge_source.md) | The most upstream source of the knowledge expressed in an Association that an... |
| [produced_by](produced_by.md) |  |
| [produces](produces.md) | holds between a material entity and a product that is generated through the i... |
| [provided_by](provided_by.md) | The value in this node property represents the knowledge provider that create... |
| [provider](provider.md) | person, group, organization or project that provides a piece of information (... |
| [publication_type](publication_type.md) | Ontology term for publication type may be drawn from Dublin Core types (https... |
| [publications](publications.md) | One or more publications that report the statement expressed in an  Associati... |
| [published_in](published_in.md) | CURIE identifier of a broader publication context within which the publicatio... |
| [publisher](publisher.md) | organization or person responsible for publishing books, periodicals, podcast... |
| [qualified_predicate](qualified_predicate.md) | Predicate to be used in an association when subject and object qualifiers are... |
| [qualifier](qualifier.md) | grouping slot for all qualifiers on an edge |
| [qualifiers](qualifiers.md) | connects an association to qualifiers that modify or qualify the meaning of t... |
| [quantifier_qualifier](quantifier_qualifier.md) | A measurable quantity for the object of the association |
| [reaction_balanced](reaction_balanced.md) |  |
| [reaction_direction](reaction_direction.md) | the direction of a reaction as constrained by the direction enum (ie: left_to... |
| [reaction_side](reaction_side.md) | the side of a reaction being modeled (ie: left or right) |
| [reference_assembly](reference_assembly.md) |  |
| [referenced_in](referenced_in.md) |  |
| [regulated_by](regulated_by.md) |  |
| [regulates](regulates.md) | A more specific form of affects, that implies the effect results from a biolo... |
| [related_condition](related_condition.md) |  |
| [related_synonym](related_synonym.md) |  |
| [related_to](related_to.md) | A relationship that is asserted between two named things |
| [related_to_at_concept_level](related_to_at_concept_level.md) | Represents a relationship held between terminology components that describe t... |
| [related_to_at_instance_level](related_to_at_instance_level.md) | Represents a relationship held between two instances of a data classes |
| [relation](relation.md) |  |
| [relative_frequency_object](relative_frequency_object.md) | The frequency at which subject and object concepts co-occur in  records withi... |
| [relative_frequency_object_confidence_interval](relative_frequency_object_confidence_interval.md) | The 99% confidence interval for the relative_frequency_object calculation (i |
| [relative_frequency_subject](relative_frequency_subject.md) | The frequency at which subject and object concepts co-occur in  records withi... |
| [relative_frequency_subject_confidence_interval](relative_frequency_subject_confidence_interval.md) | The 99% confidence interval for the relative_frequency_subject calculation (i |
| [resistance_associated_with](resistance_associated_with.md) |  |
| [resource_id](resource_id.md) | The CURIE for an Information Resource that served as a source of knowledge ex... |
| [resource_role](resource_role.md) | The role played by the InformationResource in serving as a source for an Edge |
| [response_affected_by](response_affected_by.md) | holds between two chemical entities where the susceptibility of a biological ... |
| [response_decreased_by](response_decreased_by.md) |  |
| [response_increased_by](response_increased_by.md) |  |
| [retrieval_source_ids](retrieval_source_ids.md) | A list of retrieval sources that served as a source of knowledge expressed in... |
| [retrieved_on](retrieved_on.md) |  |
| [rights](rights.md) |  |
| [risk_affected_by](risk_affected_by.md) |  |
| [routes_of_delivery](routes_of_delivery.md) | the method or process of administering a pharmaceutical compound to achieve a... |
| [same_as](same_as.md) | holds between two entities that are considered equivalent to each other |
| [sensitivity_associated_with](sensitivity_associated_with.md) |  |
| [sequence_localization_attribute](sequence_localization_attribute.md) | An attribute that can be applied to a genome sequence localization edge |
| [sequence_location_of](sequence_location_of.md) |  |
| [sequence_variant_qualifier](sequence_variant_qualifier.md) | a qualifier used in an association with the variant |
| [severity_qualifier](severity_qualifier.md) | a qualifier used in a phenotypic association to state how severe the phenotyp... |
| [sex_qualifier](sex_qualifier.md) | a qualifier used in a phenotypic association to state whether the association... |
| [similar_to](similar_to.md) | holds between an entity and some other entity with similar features |
| [source_logo](source_logo.md) |  |
| [source_web_page](source_web_page.md) |  |
| [species_context_qualifier](species_context_qualifier.md) | A statement qualifier representing a taxonomic category of species in which a... |
| [stage_qualifier](stage_qualifier.md) | stage during which gene or protein expression of takes place |
| [start_coordinate](start_coordinate.md) | The position at which the subject genomic entity starts on the chromosome or ... |
| [start_interbase_coordinate](start_interbase_coordinate.md) | The position at which the subject nucleic acid entity starts on the chromosom... |
| [statement_qualifier](statement_qualifier.md) |  |
| [stoichiometry](stoichiometry.md) | the relationship between the relative quantities of substances taking part in... |
| [strand](strand.md) | The strand on which a feature is located |
| [subclass_of](subclass_of.md) | holds between two classes where the domain class is a specialization of the r... |
| [subject](subject.md) | connects an association to the subject of the association |
| [subject_aspect_qualifier](subject_aspect_qualifier.md) |  |
| [subject_category](subject_category.md) | Used to hold the biolink class/category of an association |
| [subject_category_closure](subject_category_closure.md) | Used to hold the subject category closure of an association |
| [subject_closure](subject_closure.md) | Used to hold the subject closure of an association |
| [subject_context_qualifier](subject_context_qualifier.md) |  |
| [subject_derivative_qualifier](subject_derivative_qualifier.md) |  |
| [subject_direction_qualifier](subject_direction_qualifier.md) |  |
| [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) |  |
| [subject_label_closure](subject_label_closure.md) | Used to hold the subject label closure of an association |
| [subject_location_in_text](subject_location_in_text.md) | Character offsets for the text span(s) in the supporting text corresponding t... |
| [subject_namespace](subject_namespace.md) | Used to hold the subject namespace of an association |
| [subject_part_qualifier](subject_part_qualifier.md) |  |
| [summary](summary.md) | executive  summary of a publication |
| [superclass_of](superclass_of.md) | holds between two classes where the domain class is a super class of the rang... |
| [support_graphs](support_graphs.md) | A list of knowledge graphs that support the existence of this node |
| [supporting_data_set](supporting_data_set.md) | A set of data used as evidence to generate the knowledge expressed in an Asso... |
| [supporting_data_source](supporting_data_source.md) | An Information Resource from which data was retrieved and subsequently used a... |
| [supporting_document_type](supporting_document_type.md) | The document type (e |
| [supporting_document_year](supporting_document_year.md) | The document year (typically the publication year) for the supporting documen... |
| [supporting_documents](supporting_documents.md) | One or more referenceable documents that report the statement expressed in an... |
| [supporting_study_cohort](supporting_study_cohort.md) | A description of a study population/cohort that was interrogated to provide e... |
| [supporting_study_context](supporting_study_context.md) | A term or terms describing the experimental setting/context in which evidence... |
| [supporting_study_date_range](supporting_study_date_range.md) | The date range over which data was collected in a study that provided evidenc... |
| [supporting_study_metadata](supporting_study_metadata.md) | Information about a study used to generate information used as evidence to su... |
| [supporting_study_method_description](supporting_study_method_description.md) | A uri or curie pointing to information about the methodology used to generate... |
| [supporting_study_method_type](supporting_study_method_type.md) | A type of method that was applied in a study used to generate the information... |
| [supporting_study_size](supporting_study_size.md) | The sample size used in a study that provided evidence for the association (e |
| [supporting_text](supporting_text.md) | The segment of text from a document that supports the mined assertion |
| [supporting_text_section_type](supporting_text_section_type.md) | The section of the supporting text of a Text Mining Result within the support... |
| [symbol](symbol.md) | Symbol for a particular thing |
| [synonym](synonym.md) | Alternate human-readable names for a thing |
| [systematic_synonym](systematic_synonym.md) | more commonly used for gene symbols in yeast |
| [target_for](target_for.md) | A gene is a target of a disease when its products are druggable and when a dr... |
| [taxon](taxon.md) |  |
| [taxon_of](taxon_of.md) |  |
| [temporal_context_qualifier](temporal_context_qualifier.md) | a constraint of time placed upon the truth value of an association |
| [temporal_interval_qualifier](temporal_interval_qualifier.md) | a constraint of a time interval placed upon the truth value of an association |
| [temporally_related_to](temporally_related_to.md) | holds between two entities with a temporal relationship |
| [timepoint](timepoint.md) | a point in time |
| [total_sample_size](total_sample_size.md) | The total number of patients or participants within a sample population |
| [trade_name](trade_name.md) |  |
| [transcribed_from](transcribed_from.md) | x is transcribed from y if and only if x is synthesized from template y |
| [transcribed_to](transcribed_to.md) | inverse of transcribed from |
| [translates_to](translates_to.md) | x (amino acid chain/polypeptide) is the ribosomal translation of y (transcrip... |
| [translation_of](translation_of.md) | inverse of translates to |
| [treated_by](treated_by.md) | holds between a disease or phenotypic feature and a therapeutic process or ch... |
| [treats](treats.md) | holds between a therapeutic procedure or chemical entity and a disease or phe... |
| [type](type.md) |  |
| [update_date](update_date.md) | date on which an entity was updated |
| [upstream_resource_ids](upstream_resource_ids.md) | An upstream InformationResource from which the resource being described direc... |
| [value](value.md) |  |
| [variant_part_of](variant_part_of.md) |  |
| [version](version.md) |  |
| [version_of](version_of.md) |  |
| [volume](volume.md) | volume of a book or music release in a collection/series or a published colle... |
| [xenologous_to](xenologous_to.md) | a homology relationship characterized by an interspecies (horizontal) transfe... |
| [xref](xref.md) | A database cross reference or alternative identifier for a NamedThing or edge... |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [BioType](BioType.md) |  |
| [CausalMechanismQualifierEnum](CausalMechanismQualifierEnum.md) |  |
| [ChemicalEntityDerivativeEnum](ChemicalEntityDerivativeEnum.md) |  |
| [ChemicalOrGeneOrGeneProductFormOrVariantEnum](ChemicalOrGeneOrGeneProductFormOrVariantEnum.md) |  |
| [DigestType](DigestType.md) |  |
| [DirectionQualifierEnum](DirectionQualifierEnum.md) |  |
| [DrugAvailabilityEnum](DrugAvailabilityEnum.md) |  |
| [DrugDeliveryEnum](DrugDeliveryEnum.md) |  |
| [DruggableGeneCategoryEnum](DruggableGeneCategoryEnum.md) |  |
| [FDAApprovalStatusEnum](FDAApprovalStatusEnum.md) |  |
| [FDAIDAAdverseEventEnum](FDAIDAAdverseEventEnum.md) | please consult with the FDA guidelines as proposed in this document: https://... |
| [GeneOrGeneProductOrChemicalEntityAspectEnum](GeneOrGeneProductOrChemicalEntityAspectEnum.md) |  |
| [GeneOrGeneProductOrChemicalPartQualifierEnum](GeneOrGeneProductOrChemicalPartQualifierEnum.md) |  |
| [LogicalInterpretationEnum](LogicalInterpretationEnum.md) |  |
| [PhaseEnum](PhaseEnum.md) | phase |
| [ReactionDirectionEnum](ReactionDirectionEnum.md) |  |
| [ReactionSideEnum](ReactionSideEnum.md) |  |
| [ResourceRoleEnum](ResourceRoleEnum.md) | The role played by the information reource in serving as a source for an edge... |
| [SequenceEnum](SequenceEnum.md) | type of sequence |
| [StrandEnum](StrandEnum.md) | strand |
| [TaxonType](TaxonType.md) |  |


## Types

| Type | Description |
| --- | --- |
| [BiologicalSequence](BiologicalSequence.md) |  |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [CategoryType](CategoryType.md) | A primitive type in which the value denotes a class within the biolink model |
| [ChemicalFormulaValue](ChemicalFormulaValue.md) | A chemical formula |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [FrequencyValue](FrequencyValue.md) |  |
| [Integer](Integer.md) | An integer |
| [IriType](IriType.md) | An IRI |
| [LabelType](LabelType.md) | A string that provides a human-readable name for an entity |
| [NarrativeText](NarrativeText.md) | A string that provides a human-readable description of something |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [PercentageFrequencyValue](PercentageFrequencyValue.md) |  |
| [PredicateType](PredicateType.md) | A CURIE from the biolink related_to hierarchy |
| [Quotient](Quotient.md) |  |
| [String](String.md) | A character string |
| [SymbolType](SymbolType.md) |  |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [TimeType](TimeType.md) |  |
| [Unit](Unit.md) |  |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [ModelOrganismDatabase](ModelOrganismDatabase.md) | Subset that is relevant for a typical Model Organism Database (MOD) |
| [Samples](Samples.md) | Sample/biosample datamodel |
| [Testing](Testing.md) | TBD |
| [TranslatorMinimal](TranslatorMinimal.md) | Minimum subset of translator work |
