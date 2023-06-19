# Class: Association


_A typed association between two entities, supported by evidence_





URI: [bican:Association](https://identifiers.org/brain-bican/vocab/Association)



```mermaid
 classDiagram
    class Association
      Entity <|-- Association
      

      Association <|-- ChemicalEntityAssessesNamedThingAssociation
      Association <|-- ContributorAssociation
      Association <|-- GenotypeToGenotypePartAssociation
      Association <|-- GenotypeToGeneAssociation
      Association <|-- GenotypeToVariantAssociation
      Association <|-- GeneToGeneAssociation
      Association <|-- GeneToGeneFamilyAssociation
      Association <|-- CellLineToDiseaseOrPhenotypicFeatureAssociation
      Association <|-- ChemicalToChemicalAssociation
      Association <|-- ChemicalToDiseaseOrPhenotypicFeatureAssociation
      Association <|-- ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation
      Association <|-- GeneToPathwayAssociation
      Association <|-- MolecularActivityToPathwayAssociation
      Association <|-- ChemicalToPathwayAssociation
      Association <|-- NamedThingAssociatedWithLikelihoodOfNamedThingAssociation
      Association <|-- ChemicalGeneInteractionAssociation
      Association <|-- ChemicalAffectsGeneAssociation
      Association <|-- DrugToGeneAssociation
      Association <|-- MaterialSampleDerivationAssociation
      Association <|-- MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
      Association <|-- DiseaseToExposureEventAssociation
      Association <|-- ExposureEventToOutcomeAssociation
      Association <|-- InformationContentEntityToNamedThingAssociation
      Association <|-- DiseaseOrPhenotypicFeatureToLocationAssociation
      Association <|-- DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation
      Association <|-- GenotypeToPhenotypicFeatureAssociation
      Association <|-- ExposureEventToPhenotypicFeatureAssociation
      Association <|-- DiseaseToPhenotypicFeatureAssociation
      Association <|-- CaseToPhenotypicFeatureAssociation
      Association <|-- BehaviorToBehavioralFeatureAssociation
      Association <|-- GeneToDiseaseOrPhenotypicFeatureAssociation
      Association <|-- VariantToGeneAssociation
      Association <|-- VariantToPopulationAssociation
      Association <|-- PopulationToPopulationAssociation
      Association <|-- VariantToPhenotypicFeatureAssociation
      Association <|-- VariantToDiseaseAssociation
      Association <|-- GenotypeToDiseaseAssociation
      Association <|-- OrganismalEntityAsAModelOfDiseaseAssociation
      Association <|-- OrganismToOrganismAssociation
      Association <|-- TaxonToTaxonAssociation
      Association <|-- GeneToExpressionSiteAssociation
      Association <|-- SequenceVariantModulatesTreatmentAssociation
      Association <|-- FunctionalAssociation
      Association <|-- MolecularActivityToChemicalEntityAssociation
      Association <|-- MolecularActivityToMolecularActivityAssociation
      Association <|-- EntityToDiseaseAssociation
      Association <|-- EntityToPhenotypicFeatureAssociation
      Association <|-- SequenceAssociation
      Association <|-- SequenceFeatureRelationship
      Association <|-- ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation
      Association <|-- AnatomicalEntityToAnatomicalEntityAssociation
      Association <|-- OrganismTaxonToOrganismTaxonAssociation
      Association <|-- OrganismTaxonToEnvironmentAssociation
      
      
      Association : aggregator_knowledge_source
        
      Association : category
        
      Association : description
        
      Association : has_attribute
        
          Association --|> attribute : has_attribute
        
      Association : has_evidence
        
          Association --|> evidence type : has_evidence
        
      Association : id
        
      Association : iri
        
      Association : knowledge_source
        
      Association : name
        
      Association : negated
        
      Association : object
        
          Association --|> named thing : object
        
      Association : object_category
        
          Association --|> ontology class : object_category
        
      Association : object_category_closure
        
          Association --|> ontology class : object_category_closure
        
      Association : object_closure
        
      Association : object_label_closure
        
      Association : object_namespace
        
      Association : original_object
        
      Association : original_predicate
        
      Association : original_subject
        
      Association : predicate
        
      Association : primary_knowledge_source
        
      Association : publications
        
          Association --|> publication : publications
        
      Association : qualifiers
        
          Association --|> ontology class : qualifiers
        
      Association : retrieval_source_ids
        
          Association --|> retrieval source : retrieval_source_ids
        
      Association : subject
        
          Association --|> named thing : subject
        
      Association : subject_category
        
          Association --|> ontology class : subject_category
        
      Association : subject_category_closure
        
          Association --|> ontology class : subject_category_closure
        
      Association : subject_closure
        
      Association : subject_label_closure
        
      Association : subject_namespace
        
      Association : timepoint
        
      Association : type
        
      
```





## Inheritance
* [Entity](Entity.md)
    * **Association**
        * [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md)
        * [ContributorAssociation](ContributorAssociation.md)
        * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)
        * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)
        * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)
        * [GeneToGeneAssociation](GeneToGeneAssociation.md)
        * [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md)
        * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) [ [CellLineToEntityAssociationMixin](CellLineToEntityAssociationMixin.md) [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)]
        * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) [ [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md)]
        * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) [ [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md) [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)]
        * [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) [ [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md) [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)]
        * [GeneToPathwayAssociation](GeneToPathwayAssociation.md) [ [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)]
        * [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md)
        * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) [ [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md)]
        * [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md)
        * [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) [ [ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md)]
        * [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md)
        * [DrugToGeneAssociation](DrugToGeneAssociation.md) [ [DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md)]
        * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md)
        * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) [ [MaterialSampleToEntityAssociationMixin](MaterialSampleToEntityAssociationMixin.md) [EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)]
        * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) [ [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md) [EntityToExposureEventAssociationMixin](EntityToExposureEventAssociationMixin.md)]
        * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) [ [EntityToOutcomeAssociationMixin](EntityToOutcomeAssociationMixin.md)]
        * [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md)
        * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) [ [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md)]
        * [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) [ [DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md)]
        * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md)]
        * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)]
        * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) [DiseaseToEntityAssociationMixin](DiseaseToEntityAssociationMixin.md)]
        * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) [CaseToEntityAssociationMixin](CaseToEntityAssociationMixin.md)]
        * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)]
        * [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) [ [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) [GeneToEntityAssociationMixin](GeneToEntityAssociationMixin.md)]
        * [VariantToGeneAssociation](VariantToGeneAssociation.md) [ [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md)]
        * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) [ [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) [FrequencyQuantifier](FrequencyQuantifier.md) [FrequencyQualifierMixin](FrequencyQualifierMixin.md)]
        * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)
        * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) [ [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md)]
        * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) [ [VariantToEntityAssociationMixin](VariantToEntityAssociationMixin.md) [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md)]
        * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) [ [GenotypeToEntityAssociationMixin](GenotypeToEntityAssociationMixin.md) [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md)]
        * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) [ [ModelToDiseaseAssociationMixin](ModelToDiseaseAssociationMixin.md) [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md)]
        * [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md)
        * [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md)
        * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)
        * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)
        * [FunctionalAssociation](FunctionalAssociation.md)
        * [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md)
        * [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md)
        * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md)
        * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
        * [SequenceAssociation](SequenceAssociation.md)
        * [SequenceFeatureRelationship](SequenceFeatureRelationship.md)
        * [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md)
        * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
        * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) [ [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md)]
        * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) [ [OrganismTaxonToEntityAssociation](OrganismTaxonToEntityAssociation.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 1..1 <br/> [NamedThing](NamedThing.md) | connects an association to the subject of the association | direct |
| [predicate](predicate.md) | 1..1 <br/> [PredicateType](PredicateType.md) | A high-level grouping for the relationship type | direct |
| [object](object.md) | 1..1 <br/> [NamedThing](NamedThing.md) | connects an association to the object of the association | direct |
| [negated](negated.md) | 0..1 <br/> [Boolean](Boolean.md) | if set to true, then the association is negated i | direct |
| [qualifiers](qualifiers.md) | 0..* <br/> [OntologyClass](OntologyClass.md) | connects an association to qualifiers that modify or qualify the meaning of t... | direct |
| [publications](publications.md) | 0..* <br/> [Publication](Publication.md) | One or more publications that report the statement expressed in an  Associati... | direct |
| [has_evidence](has_evidence.md) | 0..* <br/> [EvidenceType](EvidenceType.md) | connects an association to an instance of supporting evidence | direct |
| [knowledge_source](knowledge_source.md) | 0..1 <br/> [String](String.md) | An Information Resource from which the knowledge expressed in an Association ... | direct |
| [primary_knowledge_source](primary_knowledge_source.md) | 0..1 <br/> [String](String.md) | The most upstream source of the knowledge expressed in an Association that an... | direct |
| [aggregator_knowledge_source](aggregator_knowledge_source.md) | 0..* <br/> [String](String.md) | An intermediate aggregator resource from which knowledge expressed in an Asso... | direct |
| [timepoint](timepoint.md) | 0..1 <br/> [TimeType](TimeType.md) | a point in time | direct |
| [original_subject](original_subject.md) | 0..1 <br/> [String](String.md) | used to hold the original subject of a relation (or predicate) that an extern... | direct |
| [original_predicate](original_predicate.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | used to hold the original relation/predicate that an external knowledge sourc... | direct |
| [original_object](original_object.md) | 0..1 <br/> [String](String.md) | used to hold the original object of a relation (or predicate) that an externa... | direct |
| [subject_category](subject_category.md) | 0..1 <br/> [OntologyClass](OntologyClass.md) | Used to hold the biolink class/category of an association | direct |
| [object_category](object_category.md) | 0..1 <br/> [OntologyClass](OntologyClass.md) | Used to hold the biolink class/category of an association | direct |
| [subject_closure](subject_closure.md) | 0..* <br/> [String](String.md) | Used to hold the subject closure of an association | direct |
| [object_closure](object_closure.md) | 0..* <br/> [String](String.md) | Used to hold the object closure of an association | direct |
| [subject_category_closure](subject_category_closure.md) | 0..* <br/> [OntologyClass](OntologyClass.md) | Used to hold the subject category closure of an association | direct |
| [object_category_closure](object_category_closure.md) | 0..* <br/> [OntologyClass](OntologyClass.md) | Used to hold the object category closure of an association | direct |
| [subject_namespace](subject_namespace.md) | 0..1 <br/> [String](String.md) | Used to hold the subject namespace of an association | direct |
| [object_namespace](object_namespace.md) | 0..1 <br/> [String](String.md) | Used to hold the object namespace of an association | direct |
| [subject_label_closure](subject_label_closure.md) | 0..* <br/> [String](String.md) | Used to hold the subject label closure of an association | direct |
| [object_label_closure](object_label_closure.md) | 0..* <br/> [String](String.md) | Used to hold the object label closure of an association | direct |
| [retrieval_source_ids](retrieval_source_ids.md) | 0..* <br/> [RetrievalSource](RetrievalSource.md) | A list of retrieval sources that served as a source of knowledge expressed in... | direct |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md) |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md) |
| [category](category.md) | 0..* <br/> [CategoryType](CategoryType.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | 0..* <br/> [String](String.md) | rdf:type of biolink:Association should be fixed at rdf:Statement | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | 0..* <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PredicateMapping](PredicateMapping.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_derivative_qualifier](object_derivative_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [PredicateMapping](PredicateMapping.md) | [species_context_qualifier](species_context_qualifier.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object](object.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [Association](Association.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ContributorAssociation](ContributorAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | [Association](Association.md) |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [expression_site](expression_site.md) | domain | [Association](Association.md) |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [stage_qualifier](stage_qualifier.md) | domain | [Association](Association.md) |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [phenotypic_state](phenotypic_state.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [expression_site](expression_site.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [stage_qualifier](stage_qualifier.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [phenotypic_state](phenotypic_state.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object](object.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [interacting_molecules_category](interacting_molecules_category.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object](object.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [stoichiometry](stoichiometry.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [reaction_direction](reaction_direction.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [reaction_side](reaction_side.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [stoichiometry](stoichiometry.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [reaction_direction](reaction_direction.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [reaction_side](reaction_side.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [catalyst_qualifier](catalyst_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [FDA_adverse_event_level](FDA_adverse_event_level.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [FDA_adverse_event_level](FDA_adverse_event_level.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_part_qualifier](subject_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_derivative_qualifier](subject_derivative_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_context_qualifier](subject_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_direction_qualifier](subject_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_part_qualifier](object_part_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_aspect_qualifier](object_aspect_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_context_qualifier](object_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [anatomical_context_qualifier](anatomical_context_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [qualified_predicate](qualified_predicate.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [population_context_qualifier](population_context_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [temporal_context_qualifier](temporal_context_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [expression_site](expression_site.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [stage_qualifier](stage_qualifier.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [phenotypic_state](phenotypic_state.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_aspect_qualifier](subject_aspect_qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | [Association](Association.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [stage_qualifier](stage_qualifier.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [FDA_approval_status](FDA_approval_status.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [FDA_approval_status](FDA_approval_status.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object](object.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object](object.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object](object.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object](object.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object](object.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_direction_qualifier](object_direction_qualifier.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [associated_environmental_context](associated_environmental_context.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject](subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [predicate](predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object](object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [negated](negated.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [qualifiers](qualifiers.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [publications](publications.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_evidence](has_evidence.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [knowledge_source](knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [original_subject](original_subject.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [original_predicate](original_predicate.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [original_object](original_object.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_category](subject_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_category](object_category.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_closure](subject_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_closure](object_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_category_closure](subject_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_category_closure](object_category_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_namespace](subject_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_namespace](object_namespace.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject_label_closure](subject_label_closure.md) | domain | [Association](Association.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object_label_closure](object_label_closure.md) | domain | [Association](Association.md) |






## Comments

* This is roughly the model used by biolink and ontobio at the moment

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:Association |
| native | bican:Association |
| exact | OBAN:association, rdf:Statement, owl:Axiom |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: association
description: A typed association between two entities, supported by evidence
comments:
- This is roughly the model used by biolink and ontobio at the moment
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- OBAN:association
- rdf:Statement
- owl:Axiom
is_a: entity
slots:
- subject
- predicate
- object
- negated
- qualifiers
- publications
- has evidence
- knowledge source
- primary knowledge source
- aggregator knowledge source
- timepoint
- original subject
- original predicate
- original object
- subject category
- object category
- subject closure
- object closure
- subject category closure
- object category closure
- subject namespace
- object namespace
- subject label closure
- object label closure
- retrieval source ids
slot_usage:
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
    domain_of:
    - entity
  category:
    name: category
    domain_of:
    - entity
    range: category type
    required: false

```
</details>

### Induced

<details>
```yaml
name: association
description: A typed association between two entities, supported by evidence
comments:
- This is roughly the model used by biolink and ontobio at the moment
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- OBAN:association
- rdf:Statement
- owl:Axiom
is_a: entity
slot_usage:
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
    domain_of:
    - entity
  category:
    name: category
    domain_of:
    - entity
    range: category type
    required: false
attributes:
  subject:
    name: subject
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation subject
      neo4j:
        local_name_source: neo4j
        local_name_value: node with outgoing relationship
    description: connects an association to the subject of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - owl:annotatedSource
    - OBAN:association_has_subject
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    alias: subject
    owner: association
    domain_of:
    - association
    range: named thing
    required: true
  predicate:
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
    - Has a value from the Biolink related_to hierarchy. In RDF,  this corresponds
      to rdf:predicate and in Neo4j this corresponds to the relationship type. The
      convention is for an edge label in snake_case form. For example, biolink:related_to,
      biolink:causes, biolink:treats
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - owl:annotatedProperty
    - OBAN:association_has_predicate
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:predicate
    alias: predicate
    owner: association
    domain_of:
    - predicate mapping
    - association
    range: predicate type
    required: true
  object:
    name: object
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: descriptor
      neo4j:
        local_name_source: neo4j
        local_name_value: node with incoming relationship
    description: connects an association to the object of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - owl:annotatedTarget
    - OBAN:association_has_object
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:object
    alias: object
    owner: association
    domain_of:
    - association
    range: named thing
    required: true
  negated:
    name: negated
    description: if set to true, then the association is negated i.e. is not true
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    alias: negated
    owner: association
    domain_of:
    - association
    range: boolean
  qualifiers:
    name: qualifiers
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation qualifier
    description: connects an association to qualifiers that modify or qualify the
      meaning of that association
    deprecated: 'True'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: qualifiers
    owner: association
    domain_of:
    - association
    range: ontology class
  publications:
    name: publications
    description: One or more publications that report the statement expressed in an  Association,
      or provide information used as evidence supporting this statement.
    comments:
    - 'The notion of a ‘Publication’ is considered broadly to include any  document
      made available for public consumption. It covers journal issues,  individual
      articles, and books - and also things like article pre-prints,  white papers,
      patents, drug labels, web pages, protocol documents, etc. '
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - supporting publications
    - supporting documents
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: publications
    owner: association
    domain_of:
    - association
    range: publication
  has evidence:
    name: has evidence
    description: connects an association to an instance of supporting evidence
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - RO:0002558
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: has_evidence
    owner: association
    domain_of:
    - association
    range: evidence type
  knowledge source:
    name: knowledge source
    description: An Information Resource from which the knowledge expressed in an
      Association was retrieved, directly or indirectly. This can be any resource
      through which the knowledge passed on its way to its currently serialized form.
      In practice, implementers should use one of the more specific subtypes of this
      generic property.
    from_schema: https://identifiers.org/brain-bican/kb-model
    close_mappings:
    - pav:providedBy
    rank: 1000
    is_a: association slot
    domain: association
    alias: knowledge_source
    owner: association
    domain_of:
    - association
    range: string
  primary knowledge source:
    name: primary knowledge source
    description: The most upstream source of the knowledge expressed in an Association
      that an implementer can identify.  Performing a rigorous analysis of upstream
      data providers is expected; every effort is made to catalog the most upstream
      source of data in this property.  Only one data source should be declared primary
      in any association.  "aggregator knowledge source" can be used to capture non-primary
      sources.
    notes:
    - 'For example: a single ChemicalToGene Edge originally curated by ClinicalTrials.org,
      is aggregated by ChEMBL, then  incorporated into the MolePro KP, then sent via
      TRAPI message to the ARAGORN ARA, and finally sent to  the NCATS ARS. The retrieval
      path for this Edge is as follows:  ARS--retrieved_from-->  ARAGORN  --retrieved_from-->   MolePro  --retrieved_from-->
      ChEMBL --retrieved_from-->  ClinicalTrials.gov The "primary knowledge source"
      for this edge is "infores:clinical-trials-gov".  "infores:chembl" and "infores:molecular_data_provider"
      are listed in the "aggregator knowledge source" property.'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: knowledge source
    domain: association
    multivalued: false
    alias: primary_knowledge_source
    owner: association
    domain_of:
    - association
    range: string
  aggregator knowledge source:
    name: aggregator knowledge source
    description: An intermediate aggregator resource from which knowledge expressed
      in an Association was retrieved downstream of the original source, on its path
      to its current serialized form.
    notes:
    - 'For example, in this Feature Variable Association Edge generated by the Exposure
      Agent’s ICEES KP,  through statistical analysis of clinical and environmental
      data supplied by the UNC Clinical Data Warehouse,  the Edge is passed to the
      Ranking Agent’s ARAGORN ARA,  and then on to the ARS. The retrieval path for
      this Edge is as follows: ARS--retrieved_from-->  ARAGORN  --retrieved_from-->   ICEES
      --supporting_data_from-->  UNC Data Warehouse This example illustrates how to
      represent the source provenance of KP-generated knowledge, including the source
      of  data from which the knowledge was derived.    The "primary knowledge source"
      for this edge is "infores:icees-asthma". A "supporting data source" for this
      KP- generated knowledge is "infores:unc-cdw-health."  The "aggregator knowledge
      source" for this data is "infores:aragorn-ara"'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: knowledge source
    domain: association
    multivalued: true
    alias: aggregator_knowledge_source
    owner: association
    domain_of:
    - association
    range: string
  timepoint:
    name: timepoint
    description: a point in time
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - duration
    rank: 1000
    alias: timepoint
    owner: association
    domain_of:
    - geographic location at time
    - exposure event
    - association
    range: time type
  original subject:
    name: original subject
    description: used to hold the original subject of a relation (or predicate) that
      an external knowledge source uses before transformation to match the biolink-model
      specification.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    alias: original_subject
    owner: association
    domain_of:
    - association
    range: string
  original predicate:
    name: original predicate
    id_prefixes:
    - RO
    - BSPO
    - SIO
    description: used to hold the original relation/predicate that an external knowledge
      source uses before transformation to match the biolink-model specification.
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - original relation
    - relation
    rank: 1000
    is_a: association slot
    domain: association
    alias: original_predicate
    owner: association
    domain_of:
    - association
    range: uriorcurie
  original object:
    name: original object
    description: used to hold the original object of a relation (or predicate) that
      an external knowledge source uses before transformation to match the biolink-model
      specification.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    alias: original_object
    owner: association
    domain_of:
    - association
    range: string
  subject category:
    name: subject category
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the biolink class/category of an association. This is
      a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: biolink:Gene
      description: The subject category of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'biolink:Gene'.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: false
    alias: subject_category
    owner: association
    domain_of:
    - association
    range: ontology class
  object category:
    name: object category
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the biolink class/category of an association. This is
      a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: biolink:Disease
      description: The object category of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'biolink:Disease'.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: false
    alias: object_category
    owner: association
    domain_of:
    - association
    range: ontology class
  subject closure:
    name: subject closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the subject closure of an association. This is a denormalized  field
      used primarily in the SQL serialization of a knowledge graph via KGX.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: subject_closure
    owner: association
    domain_of:
    - association
    range: string
  object closure:
    name: object closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the object closure of an association. This is a denormalized  field
      used primarily in the SQL serialization of a knowledge graph via KGX.
    examples:
    - value: '[''MONDO:0000167'', ''MONDO:0005395'']'
      description: 'The object closure of the association between the gene ''BRCA1''
        and the disease ''breast cancer'' is the set of all diseases that are ancestors
        of ''breast cancer'' in the MONDO ontology.  Note: typically the "subclass
        of" and "part of"  relations are used to construct the closure, but other
        relations may be used as well.'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: object_closure
    owner: association
    domain_of:
    - association
    range: string
  subject category closure:
    name: subject category closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the subject category closure of an association. This
      is a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''biolink:Gene", "biolink:NamedThing'']'
      description: 'The subject category closure of the association between the gene
        ''BRCA1'' and the disease ''breast cancer'' is the set of all biolink classes
        that are ancestors of ''biolink:Gene'' in the biolink model.  Note: typically
        the "subclass of" and "part of"  relations are used to construct the closure,
        but other relations may be used as well.'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: subject_category_closure
    owner: association
    domain_of:
    - association
    range: ontology class
  object category closure:
    name: object category closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the object category closure of an association. This
      is a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''biolink:Disease", "biolink:NamedThing'']'
      description: 'The object category closure of the association between the gene
        ''BRCA1'' and the disease ''breast cancer'' is the set of all biolink classes
        that are ancestors of ''biolink:Disease'' in the biolink model.  Note: typically
        the "subclass of" and "part of"  relations are used to construct the closure,
        but other relations may be used as well.'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: object_category_closure
    owner: association
    domain_of:
    - association
    range: ontology class
  subject namespace:
    name: subject namespace
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the subject namespace of an association. This is a denormalized  field
      used primarily in the SQL serialization of a knowledge graph via KGX.
    examples:
    - value: NCBIGene
      description: The subject namespace of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'NCBIGene'.
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - subject prefix
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: false
    alias: subject_namespace
    owner: association
    domain_of:
    - association
    range: string
  object namespace:
    name: object namespace
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the object namespace of an association. This is a denormalized  field
      used primarily in the SQL serialization of a knowledge graph via KGX.
    examples:
    - value: MONDO
      description: The object namespace of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'MONDO'.
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - object prefix
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: false
    alias: object_namespace
    owner: association
    domain_of:
    - association
    range: string
  subject label closure:
    name: subject label closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the subject label closure of an association. This is
      a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''BRACA1'']'
      description: The subject label closure of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is the set of all labels that are ancestors
        of 'BRCA1' in the biolink model.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: subject_label_closure
    owner: association
    domain_of:
    - association
    range: string
  object label closure:
    name: object label closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the object label closure of an association. This is
      a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''breast cancer'', ''cancer'']'
      description: The object label closure of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is the set of all labels that are ancestors
        of 'breast cancer' in the biolink model.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: object_label_closure
    owner: association
    domain_of:
    - association
    range: string
  retrieval source ids:
    name: retrieval source ids
    description: A list of retrieval sources that served as a source of knowledge
      expressed in an Edge, or a source of data used to generate this knowledge.
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    multivalued: true
    alias: retrieval_source_ids
    owner: association
    domain_of:
    - association
    range: retrieval source
  id:
    name: id
    description: A unique identifier for an entity. Must be either a CURIE shorthand
      for a URI or a complete URI
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - AGRKB:primaryId
    - gff3:ID
    - gpi:DB_Object_ID
    rank: 1000
    domain: entity
    identifier: true
    alias: id
    owner: association
    domain_of:
    - genome assembly
    - ontology class
    - entity
    range: string
    required: true
  iri:
    name: iri
    description: An IRI for an entity. This is determined by the id using expansion
      rules.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - WIKIDATA_PROPERTY:P854
    rank: 1000
    alias: iri
    owner: association
    domain_of:
    - attribute
    - entity
    range: iri type
  category:
    name: category
    description: "Name of the high level ontology class in which this entity is categorized.\
      \ Corresponds to the label for the biolink entity type class.\n * In a neo4j\
      \ database this MAY correspond to the neo4j label tag.\n * In an RDF database\
      \ it should be a biolink model class URI.\nThis field is multi-valued. It should\
      \ include values for ancestors of the biolink class; for example, a protein\
      \ such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`,\
      \ `biolink:MolecularEntity`, ...\nIn an RDF database, nodes will typically have\
      \ an rdf:type triples. This can be to the most specific biolink class, or potentially\
      \ to a class more specific than something in biolink. For example, a sequence\
      \ feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site,\
      \ which is more specific than anything in biolink. Here we would have categories\
      \ {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}"
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: type
    domain: entity
    multivalued: true
    designates_type: true
    alias: category
    owner: association
    domain_of:
    - entity
    is_class_field: true
    range: category type
    required: false
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    domain: entity
    slot_uri: rdf:type
    multivalued: true
    alias: type
    owner: association
    domain_of:
    - entity
    range: string
  name:
    name: name
    description: A human-readable name for an attribute or entity.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    rank: 1000
    domain: entity
    slot_uri: rdfs:label
    alias: name
    owner: association
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: label type
  description:
    name: description
    description: a human-readable description of an entity
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - definition
    exact_mappings:
    - IAO:0000115
    - skos:definitions
    narrow_mappings:
    - gff3:Description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: association
    domain_of:
    - genome assembly
    - entity
    range: narrative text
  has attribute:
    name: has attribute
    description: connects any entity to an attribute
    in_subset:
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - SIO:000008
    close_mappings:
    - OBI:0001927
    narrow_mappings:
    - OBAN:association_has_subject_property
    - OBAN:association_has_object_property
    - CPT:has_possibly_included_panel_element
    - DRUGBANK:category
    - EFO:is_executed_in
    - HANCESTRO:0301
    - LOINC:has_action_guidance
    - LOINC:has_adjustment
    - LOINC:has_aggregation_view
    - LOINC:has_approach_guidance
    - LOINC:has_divisor
    - LOINC:has_exam
    - LOINC:has_method
    - LOINC:has_modality_subtype
    - LOINC:has_object_guidance
    - LOINC:has_scale
    - LOINC:has_suffix
    - LOINC:has_time_aspect
    - LOINC:has_time_modifier
    - LOINC:has_timing_of
    - NCIT:R88
    - NCIT:eo_disease_has_property_or_attribute
    - NCIT:has_data_element
    - NCIT:has_pharmaceutical_administration_method
    - NCIT:has_pharmaceutical_basic_dose_form
    - NCIT:has_pharmaceutical_intended_site
    - NCIT:has_pharmaceutical_release_characteristics
    - NCIT:has_pharmaceutical_state_of_matter
    - NCIT:has_pharmaceutical_transformation
    - NCIT:is_qualified_by
    - NCIT:qualifier_applies_to
    - NCIT:role_has_domain
    - NCIT:role_has_range
    - INO:0000154
    - HANCESTRO:0308
    - OMIM:has_inheritance_type
    - orphanet:C016
    - orphanet:C017
    - RO:0000053
    - RO:0000086
    - RO:0000087
    - SNOMED:has_access
    - SNOMED:has_clinical_course
    - SNOMED:has_count_of_base_of_active_ingredient
    - SNOMED:has_dose_form_administration_method
    - SNOMED:has_dose_form_release_characteristic
    - SNOMED:has_dose_form_transformation
    - SNOMED:has_finding_context
    - SNOMED:has_finding_informer
    - SNOMED:has_inherent_attribute
    - SNOMED:has_intent
    - SNOMED:has_interpretation
    - SNOMED:has_laterality
    - SNOMED:has_measurement_method
    - SNOMED:has_method
    - SNOMED:has_priority
    - SNOMED:has_procedure_context
    - SNOMED:has_process_duration
    - SNOMED:has_property
    - SNOMED:has_revision_status
    - SNOMED:has_scale_type
    - SNOMED:has_severity
    - SNOMED:has_specimen
    - SNOMED:has_state_of_matter
    - SNOMED:has_subject_relationship_context
    - SNOMED:has_surgical_approach
    - SNOMED:has_technique
    - SNOMED:has_temporal_context
    - SNOMED:has_time_aspect
    - SNOMED:has_units
    - UMLS:has_structural_class
    - UMLS:has_supported_concept_property
    - UMLS:has_supported_concept_relationship
    - UMLS:may_be_qualified_by
    rank: 1000
    domain: entity
    multivalued: true
    alias: has_attribute
    owner: association
    domain_of:
    - entity
    range: attribute

```
</details>