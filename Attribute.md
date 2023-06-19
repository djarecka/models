# Class: Attribute


_A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material._





URI: [bican:Attribute](https://identifiers.org/brain-bican/vocab/Attribute)



```mermaid
 classDiagram
    class Attribute
      OntologyClass <|-- Attribute
      NamedThing <|-- Attribute
      

      Attribute <|-- ChemicalRole
      Attribute <|-- BiologicalSex
      Attribute <|-- SeverityValue
      Attribute <|-- OrganismAttribute
      Attribute <|-- Zygosity
      Attribute <|-- ClinicalAttribute
      Attribute <|-- SocioeconomicAttribute
      Attribute <|-- GenomicBackgroundExposure
      Attribute <|-- PathologicalProcessExposure
      Attribute <|-- PathologicalAnatomicalExposure
      Attribute <|-- DiseaseOrPhenotypicFeatureExposure
      Attribute <|-- ChemicalExposure
      Attribute <|-- ComplexChemicalExposure
      Attribute <|-- BioticExposure
      Attribute <|-- EnvironmentalExposure
      Attribute <|-- BehavioralExposure
      Attribute <|-- SocioeconomicExposure
      
      
      Attribute : category
        
      Attribute : description
        
      Attribute : full_name
        
      Attribute : has_attribute
        
          Attribute --|> attribute : has_attribute
        
      Attribute : has_attribute_type
        
          Attribute --|> ontology class : has_attribute_type
        
      Attribute : has_qualitative_value
        
          Attribute --|> named thing : has_qualitative_value
        
      Attribute : has_quantitative_value
        
          Attribute --|> quantity value : has_quantitative_value
        
      Attribute : id
        
      Attribute : iri
        
      Attribute : name
        
      Attribute : provided_by
        
      Attribute : type
        
      Attribute : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * **Attribute** [ [OntologyClass](OntologyClass.md)]
            * [ChemicalRole](ChemicalRole.md)
            * [BiologicalSex](BiologicalSex.md)
            * [SeverityValue](SeverityValue.md)
            * [OrganismAttribute](OrganismAttribute.md)
            * [Zygosity](Zygosity.md)
            * [ClinicalAttribute](ClinicalAttribute.md)
            * [SocioeconomicAttribute](SocioeconomicAttribute.md)
            * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) [ [ExposureEvent](ExposureEvent.md) [GeneGroupingMixin](GeneGroupingMixin.md) [PhysicalEssence](PhysicalEssence.md) [GenomicEntity](GenomicEntity.md) [ThingWithTaxon](ThingWithTaxon.md) [OntologyClass](OntologyClass.md)]
            * [PathologicalProcessExposure](PathologicalProcessExposure.md) [ [ExposureEvent](ExposureEvent.md)]
            * [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) [ [ExposureEvent](ExposureEvent.md)]
            * [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) [ [ExposureEvent](ExposureEvent.md) [PathologicalEntityMixin](PathologicalEntityMixin.md)]
            * [ChemicalExposure](ChemicalExposure.md) [ [ExposureEvent](ExposureEvent.md)]
            * [ComplexChemicalExposure](ComplexChemicalExposure.md)
            * [BioticExposure](BioticExposure.md) [ [ExposureEvent](ExposureEvent.md)]
            * [EnvironmentalExposure](EnvironmentalExposure.md) [ [ExposureEvent](ExposureEvent.md)]
            * [BehavioralExposure](BehavioralExposure.md) [ [ExposureEvent](ExposureEvent.md)]
            * [SocioeconomicExposure](SocioeconomicExposure.md) [ [ExposureEvent](ExposureEvent.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | The human-readable 'attribute name' can be set to a string which reflects its... | direct |
| [has_attribute_type](has_attribute_type.md) | 1..1 <br/> [OntologyClass](OntologyClass.md) | connects an attribute to a class that describes it | direct |
| [has_quantitative_value](has_quantitative_value.md) | 0..* <br/> [QuantityValue](QuantityValue.md) | connects an attribute to a value | direct |
| [has_qualitative_value](has_qualitative_value.md) | 0..1 <br/> [NamedThing](NamedThing.md) | connects an attribute to a value | direct |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | direct |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md), [OntologyClass](OntologyClass.md) |
| [provided_by](provided_by.md) | 0..* <br/> [String](String.md) | The value in this node property represents the knowledge provider that create... | [NamedThing](NamedThing.md) |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge... | [NamedThing](NamedThing.md) |
| [full_name](full_name.md) | 0..1 <br/> [LabelType](LabelType.md) | a long-form human readable name for a thing | [NamedThing](NamedThing.md) |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | 0..* <br/> [String](String.md) |  | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | 0..* <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneAnnotation](GeneAnnotation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenomeAnnotation](GenomeAnnotation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Checksum](Checksum.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Attribute](Attribute.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [Attribute](Attribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [Attribute](Attribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [Attribute](Attribute.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalRole](ChemicalRole.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ChemicalRole](ChemicalRole.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ChemicalRole](ChemicalRole.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ChemicalRole](ChemicalRole.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalSex](BiologicalSex.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [BiologicalSex](BiologicalSex.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [BiologicalSex](BiologicalSex.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [BiologicalSex](BiologicalSex.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhenotypicSex](PhenotypicSex.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicSex](PhenotypicSex.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicSex](PhenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicSex](PhenotypicSex.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypicSex](GenotypicSex.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [GenotypicSex](GenotypicSex.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [GenotypicSex](GenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [GenotypicSex](GenotypicSex.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SeverityValue](SeverityValue.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [SeverityValue](SeverityValue.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [SeverityValue](SeverityValue.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [SeverityValue](SeverityValue.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Entity](Entity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NamedThing](NamedThing.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxon](OrganismTaxon.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Event](Event.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AdministrativeEntity](AdministrativeEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [StudyResult](StudyResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Study](Study.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [StudyVariable](StudyVariable.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CommonDataElement](CommonDataElement.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TextMiningResult](TextMiningResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [LogOddsAnalysisResult](LogOddsAnalysisResult.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Agent](Agent.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [InformationContentEntity](InformationContentEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Dataset](Dataset.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DatasetDistribution](DatasetDistribution.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DatasetVersion](DatasetVersion.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DatasetSummary](DatasetSummary.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ConfidenceLevel](ConfidenceLevel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EvidenceType](EvidenceType.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Publication](Publication.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Book](Book.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BookChapter](BookChapter.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Serial](Serial.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Article](Article.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [JournalArticle](JournalArticle.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Patent](Patent.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [WebPage](WebPage.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PreprintPublication](PreprintPublication.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DrugLabel](DrugLabel.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RetrievalSource](RetrievalSource.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhysicalEntity](PhysicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Activity](Activity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Procedure](Procedure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Phenomenon](Phenomenon.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Device](Device.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiagnosticAid](DiagnosticAid.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [StudyPopulation](StudyPopulation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MaterialSample](MaterialSample.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PlanetaryEntity](PlanetaryEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeographicLocation](GeographicLocation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalEntity](BiologicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularEntity](MolecularEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntity](ChemicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SmallMolecule](SmallMolecule.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalMixture](ChemicalMixture.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RegulatoryRegion](RegulatoryRegion.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularMixture](MolecularMixture.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularActivity](MolecularActivity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BiologicalProcess](BiologicalProcess.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Pathway](Pathway.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Behavior](Behavior.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Drug](Drug.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [FoodAdditive](FoodAdditive.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Food](Food.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismAttribute](OrganismAttribute.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [OrganismAttribute](OrganismAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [OrganismAttribute](OrganismAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [OrganismAttribute](OrganismAttribute.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneticInheritance](GeneticInheritance.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismalEntity](OrganismalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Bacterium](Bacterium.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Virus](Virus.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellularOrganism](CellularOrganism.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Mammal](Mammal.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Human](Human.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Plant](Plant.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Invertebrate](Invertebrate.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Vertebrate](Vertebrate.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Fungus](Fungus.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [LifeStage](LifeStage.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [IndividualOrganism](IndividualOrganism.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Disease](Disease.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PhenotypicFeature](PhenotypicFeature.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BehavioralFeature](BehavioralFeature.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnatomicalEntity](AnatomicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellularComponent](CellularComponent.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Cell](Cell.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellLine](CellLine.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Gene](Gene.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MacromolecularComplex](MacromolecularComplex.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NucleosomeModification](NucleosomeModification.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Genome](Genome.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Exon](Exon.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Transcript](Transcript.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CodingSequence](CodingSequence.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Polypeptide](Polypeptide.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Protein](Protein.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ProteinIsoform](ProteinIsoform.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ProteinDomain](ProteinDomain.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PosttranslationalModification](PosttranslationalModification.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ProteinFamily](ProteinFamily.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RNAProduct](RNAProduct.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MicroRNA](MicroRNA.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SiRNA](SiRNA.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneFamily](GeneFamily.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Zygosity](Zygosity.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [Zygosity](Zygosity.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [Zygosity](Zygosity.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [Zygosity](Zygosity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Genotype](Genotype.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Haplotype](Haplotype.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SequenceVariant](SequenceVariant.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Snv](Snv.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalModifier](ClinicalModifier.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ClinicalModifier](ClinicalModifier.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalModifier](ClinicalModifier.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalModifier](ClinicalModifier.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalCourse](ClinicalCourse.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ClinicalCourse](ClinicalCourse.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalCourse](ClinicalCourse.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ClinicalCourse](ClinicalCourse.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Onset](Onset.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [Onset](Onset.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [Onset](Onset.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [Onset](Onset.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalEntity](ClinicalEntity.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalTrial](ClinicalTrial.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ClinicalIntervention](ClinicalIntervention.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Hospitalization](Hospitalization.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Case](Case.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Cohort](Cohort.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathologicalProcess](PathologicalProcess.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalExposure](ChemicalExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ChemicalExposure](ChemicalExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ChemicalExposure](ChemicalExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ChemicalExposure](ChemicalExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DrugExposure](DrugExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [DrugExposure](DrugExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [DrugExposure](DrugExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [DrugExposure](DrugExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [Treatment](Treatment.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BioticExposure](BioticExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [BioticExposure](BioticExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [BioticExposure](BioticExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [BioticExposure](BioticExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeographicExposure](GeographicExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [GeographicExposure](GeographicExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [GeographicExposure](GeographicExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [GeographicExposure](GeographicExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BehavioralExposure](BehavioralExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [BehavioralExposure](BehavioralExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [BehavioralExposure](BehavioralExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [BehavioralExposure](BehavioralExposure.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SocioeconomicExposure](SocioeconomicExposure.md) | [has_attribute_type](has_attribute_type.md) | domain | [Attribute](Attribute.md) |
| [SocioeconomicExposure](SocioeconomicExposure.md) | [has_quantitative_value](has_quantitative_value.md) | domain | [Attribute](Attribute.md) |
| [SocioeconomicExposure](SocioeconomicExposure.md) | [has_qualitative_value](has_qualitative_value.md) | domain | [Attribute](Attribute.md) |
| [Association](Association.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ContributorAssociation](ContributorAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation](ChemicalOrDrugOrTreatmentSideEffectDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToPathwayAssociation](GeneToPathwayAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation](DiseaseOrPhenotypicFeatureToGeneticInheritanceAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SequenceAssociation](SequenceAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation](ChemicalEntityOrGeneOrGeneProductRegulatesGeneAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_attribute](has_attribute.md) | range | [Attribute](Attribute.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* EDAM-DATA

* EDAM-FORMAT

* EDAM-OPERATION

* EDAM-TOPIC








### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:Attribute |
| native | bican:Attribute |
| exact | SIO:000614 |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: attribute
id_prefixes:
- EDAM-DATA
- EDAM-FORMAT
- EDAM-OPERATION
- EDAM-TOPIC
description: A property or characteristic of an entity. For example, an apple may
  have properties such as color, shape, age, crispiness. An environmental sample may
  have attributes such as depth, lat, long, material.
in_subset:
- samples
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SIO:000614
is_a: named thing
mixins:
- ontology class
slots:
- name
- has attribute type
- has quantitative value
- has qualitative value
- iri
slot_usage:
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin

```
</details>

### Induced

<details>
```yaml
name: attribute
id_prefixes:
- EDAM-DATA
- EDAM-FORMAT
- EDAM-OPERATION
- EDAM-TOPIC
description: A property or characteristic of an entity. For example, an apple may
  have properties such as color, shape, age, crispiness. An environmental sample may
  have attributes such as depth, lat, long, material.
in_subset:
- samples
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SIO:000614
is_a: named thing
mixins:
- ontology class
slot_usage:
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
attributes:
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    domain: entity
    slot_uri: rdfs:label
    alias: name
    owner: attribute
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: label type
  has attribute type:
    name: has attribute type
    description: connects an attribute to a class that describes it
    in_subset:
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    narrow_mappings:
    - LOINC:has_modality_type
    - LOINC:has_view_type
    rank: 1000
    domain: attribute
    multivalued: false
    alias: has_attribute_type
    owner: attribute
    domain_of:
    - attribute
    range: ontology class
    required: true
  has quantitative value:
    name: has quantitative value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - qud:quantityValue
    narrow_mappings:
    - SNOMED:has_concentration_strength_numerator_value
    - SNOMED:has_presentation_strength_denominator_value
    - SNOMED:has_presentation_strength_numerator_value
    rank: 1000
    domain: attribute
    multivalued: true
    alias: has_quantitative_value
    owner: attribute
    domain_of:
    - attribute
    - chemical exposure
    range: quantity value
  has qualitative value:
    name: has qualitative value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    domain: attribute
    multivalued: false
    alias: has_qualitative_value
    owner: attribute
    domain_of:
    - attribute
    range: named thing
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
    owner: attribute
    domain_of:
    - attribute
    - entity
    range: iri type
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
    owner: attribute
    domain_of:
    - genome assembly
    - ontology class
    - entity
    range: string
    required: true
  provided by:
    name: provided by
    description: The value in this node property represents the knowledge provider
      that created or assembled the node and all of its attributes.  Used internally
      to represent how a particular node made its way into a knowledge provider or
      graph.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: node property
    domain: named thing
    multivalued: true
    alias: provided_by
    owner: attribute
    domain_of:
    - named thing
    range: string
  xref:
    name: xref
    description: A database cross reference or alternative identifier for a NamedThing
      or edge between two  NamedThings.  This property should point to a database
      record or webpage that supports the existence of the edge, or  gives more detail
      about the edge. This property can be used on a node or edge to provide multiple
      URIs or CURIE cross references.
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - dbxref
    - Dbxref
    - DbXref
    - record_url
    - source_record_urls
    narrow_mappings:
    - gff3:Dbxref
    - gpi:DB_Xrefs
    rank: 1000
    domain: named thing
    multivalued: true
    alias: xref
    owner: attribute
    domain_of:
    - named thing
    - publication
    - retrieval source
    - gene
    - gene product mixin
    range: uriorcurie
  full name:
    name: full name
    description: a long-form human readable name for a thing
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: node property
    domain: named thing
    alias: full_name
    owner: attribute
    domain_of:
    - named thing
    range: label type
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
    owner: attribute
    domain_of:
    - entity
    is_class_field: true
    range: category type
    required: true
    pattern: ^biolink:[A-Z][A-Za-z]+$
  type:
    name: type
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - AGRKB:soTermId
    - gff3:type
    - gpi:DB_Object_Type
    rank: 1000
    domain: entity
    slot_uri: rdf:type
    multivalued: true
    alias: type
    owner: attribute
    domain_of:
    - entity
    range: string
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
    owner: attribute
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
    owner: attribute
    domain_of:
    - entity
    range: attribute

```
</details>