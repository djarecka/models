# Class: NamedThing


_a databased entity or concept/class_





URI: [bican:NamedThing](https://identifiers.org/brain-bican/vocab/NamedThing)



```mermaid
 classDiagram
    class NamedThing
      Entity <|-- NamedThing
      

      NamedThing <|-- Attribute
      NamedThing <|-- OrganismTaxon
      NamedThing <|-- Event
      NamedThing <|-- AdministrativeEntity
      NamedThing <|-- InformationContentEntity
      NamedThing <|-- PhysicalEntity
      NamedThing <|-- Activity
      NamedThing <|-- Procedure
      NamedThing <|-- Phenomenon
      NamedThing <|-- Device
      NamedThing <|-- DiagnosticAid
      NamedThing <|-- PlanetaryEntity
      NamedThing <|-- BiologicalEntity
      NamedThing <|-- ChemicalEntity
      NamedThing <|-- ClinicalEntity
      NamedThing <|-- Treatment
      
      
      NamedThing : category
        
      NamedThing : description
        
      NamedThing : full_name
        
      NamedThing : has_attribute
        
          NamedThing --|> attribute : has_attribute
        
      NamedThing : id
        
      NamedThing : iri
        
      NamedThing : name
        
      NamedThing : provided_by
        
      NamedThing : type
        
      NamedThing : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * **NamedThing**
        * [Attribute](Attribute.md) [ [OntologyClass](OntologyClass.md)]
        * [OrganismTaxon](OrganismTaxon.md)
        * [Event](Event.md)
        * [AdministrativeEntity](AdministrativeEntity.md)
        * [InformationContentEntity](InformationContentEntity.md)
        * [PhysicalEntity](PhysicalEntity.md) [ [PhysicalEssence](PhysicalEssence.md)]
        * [Activity](Activity.md) [ [ActivityAndBehavior](ActivityAndBehavior.md)]
        * [Procedure](Procedure.md) [ [ActivityAndBehavior](ActivityAndBehavior.md)]
        * [Phenomenon](Phenomenon.md) [ [Occurrent](Occurrent.md)]
        * [Device](Device.md)
        * [DiagnosticAid](DiagnosticAid.md)
        * [PlanetaryEntity](PlanetaryEntity.md)
        * [BiologicalEntity](BiologicalEntity.md) [ [ThingWithTaxon](ThingWithTaxon.md)]
        * [ChemicalEntity](ChemicalEntity.md) [ [PhysicalEssence](PhysicalEssence.md) [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md) [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) [ChemicalEntityOrProteinOrPolypeptide](ChemicalEntityOrProteinOrPolypeptide.md)]
        * [ClinicalEntity](ClinicalEntity.md)
        * [Treatment](Treatment.md) [ [ExposureEvent](ExposureEvent.md) [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [provided_by](provided_by.md) | 0..* <br/> [String](String.md) | The value in this node property represents the knowledge provider that create... | direct |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge... | direct |
| [full_name](full_name.md) | 0..1 <br/> [LabelType](LabelType.md) | a long-form human readable name for a thing | direct |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md) |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md) |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | 0..* <br/> [String](String.md) |  | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | 0..* <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneAnnotation](GeneAnnotation.md) | [symbol](symbol.md) | domain | [NamedThing](NamedThing.md) |
| [GeneAnnotation](GeneAnnotation.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [GeneAnnotation](GeneAnnotation.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GeneAnnotation](GeneAnnotation.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [GeneAnnotation](GeneAnnotation.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GeneAnnotation](GeneAnnotation.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GenomeAnnotation](GenomeAnnotation.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [GenomeAnnotation](GenomeAnnotation.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GenomeAnnotation](GenomeAnnotation.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GenomeAnnotation](GenomeAnnotation.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Mapping](Mapping.md) | [member_of](member_of.md) | domain | [NamedThing](NamedThing.md) |
| [Mapping](Mapping.md) | [member_of](member_of.md) | range | [NamedThing](NamedThing.md) |
| [Mappings](Mappings.md) | [has_member](has_member.md) | domain | [NamedThing](NamedThing.md) |
| [Mappings](Mappings.md) | [has_member](has_member.md) | range | [NamedThing](NamedThing.md) |
| [PredicateMapping](PredicateMapping.md) | [exact_match](exact_match.md) | domain | [NamedThing](NamedThing.md) |
| [PredicateMapping](PredicateMapping.md) | [exact_match](exact_match.md) | range | [NamedThing](NamedThing.md) |
| [PredicateMapping](PredicateMapping.md) | [narrow_match](narrow_match.md) | domain | [NamedThing](NamedThing.md) |
| [PredicateMapping](PredicateMapping.md) | [narrow_match](narrow_match.md) | range | [NamedThing](NamedThing.md) |
| [PredicateMapping](PredicateMapping.md) | [broad_match](broad_match.md) | domain | [NamedThing](NamedThing.md) |
| [PredicateMapping](PredicateMapping.md) | [broad_match](broad_match.md) | range | [NamedThing](NamedThing.md) |
| [Attribute](Attribute.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [Attribute](Attribute.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Attribute](Attribute.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Attribute](Attribute.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalRole](ChemicalRole.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [ChemicalRole](ChemicalRole.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalRole](ChemicalRole.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalRole](ChemicalRole.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalSex](BiologicalSex.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [BiologicalSex](BiologicalSex.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalSex](BiologicalSex.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalSex](BiologicalSex.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PhenotypicSex](PhenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [PhenotypicSex](PhenotypicSex.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PhenotypicSex](PhenotypicSex.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PhenotypicSex](PhenotypicSex.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GenotypicSex](GenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [GenotypicSex](GenotypicSex.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GenotypicSex](GenotypicSex.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GenotypicSex](GenotypicSex.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [SeverityValue](SeverityValue.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [SeverityValue](SeverityValue.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [SeverityValue](SeverityValue.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [SeverityValue](SeverityValue.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [FrequencyQuantifier](FrequencyQuantifier.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [FrequencyQuantifier](FrequencyQuantifier.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [FrequencyQuantifier](FrequencyQuantifier.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [FrequencyQuantifier](FrequencyQuantifier.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [NamedThing](NamedThing.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [NamedThing](NamedThing.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [NamedThing](NamedThing.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [OrganismTaxon](OrganismTaxon.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [OrganismTaxon](OrganismTaxon.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [OrganismTaxon](OrganismTaxon.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Event](Event.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Event](Event.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Event](Event.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [AdministrativeEntity](AdministrativeEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [AdministrativeEntity](AdministrativeEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [AdministrativeEntity](AdministrativeEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [StudyResult](StudyResult.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [StudyResult](StudyResult.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [StudyResult](StudyResult.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [StudyResult](StudyResult.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Study](Study.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Study](Study.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Study](Study.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [StudyVariable](StudyVariable.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [StudyVariable](StudyVariable.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [StudyVariable](StudyVariable.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [StudyVariable](StudyVariable.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [CommonDataElement](CommonDataElement.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [CommonDataElement](CommonDataElement.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [CommonDataElement](CommonDataElement.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [CommonDataElement](CommonDataElement.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ConceptCountAnalysisResult](ConceptCountAnalysisResult.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ObservedExpectedFrequencyAnalysisResult](ObservedExpectedFrequencyAnalysisResult.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [RelativeFrequencyAnalysisResult](RelativeFrequencyAnalysisResult.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [TextMiningResult](TextMiningResult.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [TextMiningResult](TextMiningResult.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [TextMiningResult](TextMiningResult.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [TextMiningResult](TextMiningResult.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ChiSquaredAnalysisResult](ChiSquaredAnalysisResult.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [LogOddsAnalysisResult](LogOddsAnalysisResult.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [LogOddsAnalysisResult](LogOddsAnalysisResult.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [LogOddsAnalysisResult](LogOddsAnalysisResult.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [LogOddsAnalysisResult](LogOddsAnalysisResult.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Agent](Agent.md) | [address](address.md) | domain | [NamedThing](NamedThing.md) |
| [Agent](Agent.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Agent](Agent.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Agent](Agent.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [InformationContentEntity](InformationContentEntity.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [InformationContentEntity](InformationContentEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [InformationContentEntity](InformationContentEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [InformationContentEntity](InformationContentEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Dataset](Dataset.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [Dataset](Dataset.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Dataset](Dataset.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Dataset](Dataset.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetDistribution](DatasetDistribution.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetDistribution](DatasetDistribution.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetDistribution](DatasetDistribution.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetDistribution](DatasetDistribution.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetVersion](DatasetVersion.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetVersion](DatasetVersion.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetVersion](DatasetVersion.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetVersion](DatasetVersion.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetSummary](DatasetSummary.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetSummary](DatasetSummary.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetSummary](DatasetSummary.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [DatasetSummary](DatasetSummary.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ConfidenceLevel](ConfidenceLevel.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [ConfidenceLevel](ConfidenceLevel.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ConfidenceLevel](ConfidenceLevel.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ConfidenceLevel](ConfidenceLevel.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [EvidenceType](EvidenceType.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [EvidenceType](EvidenceType.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [EvidenceType](EvidenceType.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [EvidenceType](EvidenceType.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Publication](Publication.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Publication](Publication.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [Publication](Publication.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Publication](Publication.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Book](Book.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Book](Book.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [Book](Book.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Book](Book.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [BookChapter](BookChapter.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [BookChapter](BookChapter.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [BookChapter](BookChapter.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [BookChapter](BookChapter.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Serial](Serial.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Serial](Serial.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [Serial](Serial.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Serial](Serial.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Article](Article.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Article](Article.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [Article](Article.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Article](Article.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [JournalArticle](JournalArticle.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [JournalArticle](JournalArticle.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [JournalArticle](JournalArticle.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [JournalArticle](JournalArticle.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Patent](Patent.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Patent](Patent.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [Patent](Patent.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Patent](Patent.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [WebPage](WebPage.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [WebPage](WebPage.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [WebPage](WebPage.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [WebPage](WebPage.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PreprintPublication](PreprintPublication.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PreprintPublication](PreprintPublication.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [PreprintPublication](PreprintPublication.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PreprintPublication](PreprintPublication.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [DrugLabel](DrugLabel.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [DrugLabel](DrugLabel.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [DrugLabel](DrugLabel.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [DrugLabel](DrugLabel.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [RetrievalSource](RetrievalSource.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [RetrievalSource](RetrievalSource.md) | [creation_date](creation_date.md) | domain | [NamedThing](NamedThing.md) |
| [RetrievalSource](RetrievalSource.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [RetrievalSource](RetrievalSource.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PhysicalEntity](PhysicalEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PhysicalEntity](PhysicalEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PhysicalEntity](PhysicalEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Activity](Activity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Activity](Activity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Activity](Activity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Procedure](Procedure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Procedure](Procedure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Procedure](Procedure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Phenomenon](Phenomenon.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Phenomenon](Phenomenon.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Phenomenon](Phenomenon.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Device](Device.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Device](Device.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Device](Device.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [DiagnosticAid](DiagnosticAid.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [DiagnosticAid](DiagnosticAid.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [DiagnosticAid](DiagnosticAid.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [StudyPopulation](StudyPopulation.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [StudyPopulation](StudyPopulation.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [StudyPopulation](StudyPopulation.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [MaterialSample](MaterialSample.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [MaterialSample](MaterialSample.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [MaterialSample](MaterialSample.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PlanetaryEntity](PlanetaryEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PlanetaryEntity](PlanetaryEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PlanetaryEntity](PlanetaryEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocation](GeographicLocation.md) | [latitude](latitude.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocation](GeographicLocation.md) | [longitude](longitude.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocation](GeographicLocation.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocation](GeographicLocation.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocation](GeographicLocation.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [latitude](latitude.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [longitude](longitude.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalEntity](BiologicalEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalEntity](BiologicalEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalEntity](BiologicalEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GenomicEntity](GenomicEntity.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [EpigenomicEntity](EpigenomicEntity.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularEntity](MolecularEntity.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularEntity](MolecularEntity.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularEntity](MolecularEntity.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularEntity](MolecularEntity.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularEntity](MolecularEntity.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularEntity](MolecularEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularEntity](MolecularEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularEntity](MolecularEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalEntity](ChemicalEntity.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalEntity](ChemicalEntity.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalEntity](ChemicalEntity.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalEntity](ChemicalEntity.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalEntity](ChemicalEntity.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalEntity](ChemicalEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalEntity](ChemicalEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalEntity](ChemicalEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [SmallMolecule](SmallMolecule.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [SmallMolecule](SmallMolecule.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [SmallMolecule](SmallMolecule.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [SmallMolecule](SmallMolecule.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [SmallMolecule](SmallMolecule.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [SmallMolecule](SmallMolecule.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [SmallMolecule](SmallMolecule.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [SmallMolecule](SmallMolecule.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalMixture](ChemicalMixture.md) | [is_supplement](is_supplement.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalMixture](ChemicalMixture.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalMixture](ChemicalMixture.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalMixture](ChemicalMixture.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalMixture](ChemicalMixture.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalMixture](ChemicalMixture.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalMixture](ChemicalMixture.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalMixture](ChemicalMixture.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalMixture](ChemicalMixture.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [RegulatoryRegion](RegulatoryRegion.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [RegulatoryRegion](RegulatoryRegion.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [RegulatoryRegion](RegulatoryRegion.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [RegulatoryRegion](RegulatoryRegion.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularMixture](MolecularMixture.md) | [is_supplement](is_supplement.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularMixture](MolecularMixture.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularMixture](MolecularMixture.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularMixture](MolecularMixture.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularMixture](MolecularMixture.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularMixture](MolecularMixture.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularMixture](MolecularMixture.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularMixture](MolecularMixture.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularMixture](MolecularMixture.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [is_supplement](is_supplement.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [has_input](has_input.md) | range | [NamedThing](NamedThing.md) |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [has_output](has_output.md) | range | [NamedThing](NamedThing.md) |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularActivity](MolecularActivity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularActivity](MolecularActivity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [MolecularActivity](MolecularActivity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalProcess](BiologicalProcess.md) | [has_input](has_input.md) | range | [NamedThing](NamedThing.md) |
| [BiologicalProcess](BiologicalProcess.md) | [has_output](has_output.md) | range | [NamedThing](NamedThing.md) |
| [BiologicalProcess](BiologicalProcess.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalProcess](BiologicalProcess.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [BiologicalProcess](BiologicalProcess.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Pathway](Pathway.md) | [has_input](has_input.md) | range | [NamedThing](NamedThing.md) |
| [Pathway](Pathway.md) | [has_output](has_output.md) | range | [NamedThing](NamedThing.md) |
| [Pathway](Pathway.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Pathway](Pathway.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Pathway](Pathway.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [has_input](has_input.md) | range | [NamedThing](NamedThing.md) |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [has_output](has_output.md) | range | [NamedThing](NamedThing.md) |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Behavior](Behavior.md) | [has_input](has_input.md) | range | [NamedThing](NamedThing.md) |
| [Behavior](Behavior.md) | [has_output](has_output.md) | range | [NamedThing](NamedThing.md) |
| [Behavior](Behavior.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Behavior](Behavior.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Behavior](Behavior.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [is_supplement](is_supplement.md) | domain | [NamedThing](NamedThing.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ProcessedMaterial](ProcessedMaterial.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Drug](Drug.md) | [is_supplement](is_supplement.md) | domain | [NamedThing](NamedThing.md) |
| [Drug](Drug.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [Drug](Drug.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [Drug](Drug.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [Drug](Drug.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [Drug](Drug.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [Drug](Drug.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Drug](Drug.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Drug](Drug.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [FoodAdditive](FoodAdditive.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [FoodAdditive](FoodAdditive.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [FoodAdditive](FoodAdditive.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [FoodAdditive](FoodAdditive.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [FoodAdditive](FoodAdditive.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [FoodAdditive](FoodAdditive.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [FoodAdditive](FoodAdditive.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [FoodAdditive](FoodAdditive.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Food](Food.md) | [is_supplement](is_supplement.md) | domain | [NamedThing](NamedThing.md) |
| [Food](Food.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [Food](Food.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [Food](Food.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [Food](Food.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [Food](Food.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [Food](Food.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Food](Food.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Food](Food.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [OrganismAttribute](OrganismAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [OrganismAttribute](OrganismAttribute.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [OrganismAttribute](OrganismAttribute.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [OrganismAttribute](OrganismAttribute.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PhenotypicQuality](PhenotypicQuality.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GeneticInheritance](GeneticInheritance.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GeneticInheritance](GeneticInheritance.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GeneticInheritance](GeneticInheritance.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [OrganismalEntity](OrganismalEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [OrganismalEntity](OrganismalEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [OrganismalEntity](OrganismalEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Bacterium](Bacterium.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Bacterium](Bacterium.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Bacterium](Bacterium.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Virus](Virus.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Virus](Virus.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Virus](Virus.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [CellularOrganism](CellularOrganism.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [CellularOrganism](CellularOrganism.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [CellularOrganism](CellularOrganism.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Mammal](Mammal.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Mammal](Mammal.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Mammal](Mammal.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Human](Human.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Human](Human.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Human](Human.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Plant](Plant.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Plant](Plant.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Plant](Plant.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Invertebrate](Invertebrate.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Invertebrate](Invertebrate.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Invertebrate](Invertebrate.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Vertebrate](Vertebrate.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Vertebrate](Vertebrate.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Vertebrate](Vertebrate.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Fungus](Fungus.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Fungus](Fungus.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Fungus](Fungus.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [LifeStage](LifeStage.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [LifeStage](LifeStage.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [LifeStage](LifeStage.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [IndividualOrganism](IndividualOrganism.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [IndividualOrganism](IndividualOrganism.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [IndividualOrganism](IndividualOrganism.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Disease](Disease.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Disease](Disease.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Disease](Disease.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PhenotypicFeature](PhenotypicFeature.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PhenotypicFeature](PhenotypicFeature.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PhenotypicFeature](PhenotypicFeature.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [BehavioralFeature](BehavioralFeature.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [BehavioralFeature](BehavioralFeature.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [BehavioralFeature](BehavioralFeature.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [AnatomicalEntity](AnatomicalEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [AnatomicalEntity](AnatomicalEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [AnatomicalEntity](AnatomicalEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [CellularComponent](CellularComponent.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [CellularComponent](CellularComponent.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [CellularComponent](CellularComponent.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Cell](Cell.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Cell](Cell.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Cell](Cell.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [CellLine](CellLine.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [CellLine](CellLine.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [CellLine](CellLine.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Gene](Gene.md) | [symbol](symbol.md) | domain | [NamedThing](NamedThing.md) |
| [Gene](Gene.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [Gene](Gene.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Gene](Gene.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [Gene](Gene.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Gene](Gene.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GeneProductMixin](GeneProductMixin.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [GeneProductMixin](GeneProductMixin.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GeneProductIsoformMixin](GeneProductIsoformMixin.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [GeneProductIsoformMixin](GeneProductIsoformMixin.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [MacromolecularComplex](MacromolecularComplex.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [MacromolecularComplex](MacromolecularComplex.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [MacromolecularComplex](MacromolecularComplex.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [NucleosomeModification](NucleosomeModification.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [NucleosomeModification](NucleosomeModification.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [NucleosomeModification](NucleosomeModification.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [NucleosomeModification](NucleosomeModification.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [NucleosomeModification](NucleosomeModification.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [Genome](Genome.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [Genome](Genome.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Genome](Genome.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Genome](Genome.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Exon](Exon.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [Exon](Exon.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [Exon](Exon.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [Exon](Exon.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [Exon](Exon.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [Exon](Exon.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [Exon](Exon.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Exon](Exon.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Exon](Exon.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Transcript](Transcript.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [Transcript](Transcript.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [Transcript](Transcript.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [Transcript](Transcript.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [Transcript](Transcript.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [Transcript](Transcript.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [Transcript](Transcript.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Transcript](Transcript.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Transcript](Transcript.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [CodingSequence](CodingSequence.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [CodingSequence](CodingSequence.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [CodingSequence](CodingSequence.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [CodingSequence](CodingSequence.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [CodingSequence](CodingSequence.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [CodingSequence](CodingSequence.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [CodingSequence](CodingSequence.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [CodingSequence](CodingSequence.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [CodingSequence](CodingSequence.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Polypeptide](Polypeptide.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Polypeptide](Polypeptide.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Polypeptide](Polypeptide.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Protein](Protein.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [Protein](Protein.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Protein](Protein.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Protein](Protein.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinIsoform](ProteinIsoform.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinIsoform](ProteinIsoform.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinIsoform](ProteinIsoform.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinIsoform](ProteinIsoform.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinDomain](ProteinDomain.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinDomain](ProteinDomain.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinDomain](ProteinDomain.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinDomain](ProteinDomain.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PosttranslationalModification](PosttranslationalModification.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PosttranslationalModification](PosttranslationalModification.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PosttranslationalModification](PosttranslationalModification.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PosttranslationalModification](PosttranslationalModification.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinFamily](ProteinFamily.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinFamily](ProteinFamily.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinFamily](ProteinFamily.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ProteinFamily](ProteinFamily.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProduct](RNAProduct.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [MicroRNA](MicroRNA.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [synonym](synonym.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [trade_name](trade_name.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [available_from](available_from.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [is_toxic](is_toxic.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [has_chemical_role](has_chemical_role.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [SiRNA](SiRNA.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GeneGroupingMixin](GeneGroupingMixin.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | [NamedThing](NamedThing.md) |
| [GeneFamily](GeneFamily.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | [NamedThing](NamedThing.md) |
| [GeneFamily](GeneFamily.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GeneFamily](GeneFamily.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GeneFamily](GeneFamily.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Zygosity](Zygosity.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [Zygosity](Zygosity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Zygosity](Zygosity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Zygosity](Zygosity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Genotype](Genotype.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [Genotype](Genotype.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Genotype](Genotype.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Genotype](Genotype.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Haplotype](Haplotype.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [Haplotype](Haplotype.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Haplotype](Haplotype.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Haplotype](Haplotype.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [SequenceVariant](SequenceVariant.md) | [has_gene](has_gene.md) | domain | [NamedThing](NamedThing.md) |
| [SequenceVariant](SequenceVariant.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [SequenceVariant](SequenceVariant.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [SequenceVariant](SequenceVariant.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [SequenceVariant](SequenceVariant.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Snv](Snv.md) | [has_gene](has_gene.md) | domain | [NamedThing](NamedThing.md) |
| [Snv](Snv.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [Snv](Snv.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Snv](Snv.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Snv](Snv.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalAttribute](ClinicalAttribute.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalModifier](ClinicalModifier.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [ClinicalModifier](ClinicalModifier.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalModifier](ClinicalModifier.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalModifier](ClinicalModifier.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalCourse](ClinicalCourse.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [ClinicalCourse](ClinicalCourse.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalCourse](ClinicalCourse.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalCourse](ClinicalCourse.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Onset](Onset.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [Onset](Onset.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Onset](Onset.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Onset](Onset.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalEntity](ClinicalEntity.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalEntity](ClinicalEntity.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalEntity](ClinicalEntity.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalTrial](ClinicalTrial.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalTrial](ClinicalTrial.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalTrial](ClinicalTrial.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalIntervention](ClinicalIntervention.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalIntervention](ClinicalIntervention.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalIntervention](ClinicalIntervention.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalFinding](ClinicalFinding.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalFinding](ClinicalFinding.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ClinicalFinding](ClinicalFinding.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Hospitalization](Hospitalization.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Hospitalization](Hospitalization.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Hospitalization](Hospitalization.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Case](Case.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Case](Case.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Case](Case.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Cohort](Cohort.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Cohort](Cohort.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Cohort](Cohort.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | [NamedThing](NamedThing.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_biological_sequence](has_biological_sequence.md) | domain | [NamedThing](NamedThing.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalProcess](PathologicalProcess.md) | [has_input](has_input.md) | range | [NamedThing](NamedThing.md) |
| [PathologicalProcess](PathologicalProcess.md) | [has_output](has_output.md) | range | [NamedThing](NamedThing.md) |
| [PathologicalProcess](PathologicalProcess.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalProcess](PathologicalProcess.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalProcess](PathologicalProcess.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalExposure](ChemicalExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [ChemicalExposure](ChemicalExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalExposure](ChemicalExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ChemicalExposure](ChemicalExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [ComplexChemicalExposure](ComplexChemicalExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [DrugExposure](DrugExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [DrugExposure](DrugExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [DrugExposure](DrugExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [DrugExposure](DrugExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | [NamedThing](NamedThing.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Treatment](Treatment.md) | [has_drug](has_drug.md) | domain | [NamedThing](NamedThing.md) |
| [Treatment](Treatment.md) | [has_device](has_device.md) | domain | [NamedThing](NamedThing.md) |
| [Treatment](Treatment.md) | [has_procedure](has_procedure.md) | domain | [NamedThing](NamedThing.md) |
| [Treatment](Treatment.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [Treatment](Treatment.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [Treatment](Treatment.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [BioticExposure](BioticExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [BioticExposure](BioticExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [BioticExposure](BioticExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [BioticExposure](BioticExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicExposure](GeographicExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [GeographicExposure](GeographicExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicExposure](GeographicExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [GeographicExposure](GeographicExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [BehavioralExposure](BehavioralExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [BehavioralExposure](BehavioralExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [BehavioralExposure](BehavioralExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [BehavioralExposure](BehavioralExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [SocioeconomicExposure](SocioeconomicExposure.md) | [has_qualitative_value](has_qualitative_value.md) | range | [NamedThing](NamedThing.md) |
| [SocioeconomicExposure](SocioeconomicExposure.md) | [provided_by](provided_by.md) | domain | [NamedThing](NamedThing.md) |
| [SocioeconomicExposure](SocioeconomicExposure.md) | [xref](xref.md) | domain | [NamedThing](NamedThing.md) |
| [SocioeconomicExposure](SocioeconomicExposure.md) | [full_name](full_name.md) | domain | [NamedThing](NamedThing.md) |
| [Association](Association.md) | [subject](subject.md) | range | [NamedThing](NamedThing.md) |
| [Association](Association.md) | [object](object.md) | range | [NamedThing](NamedThing.md) |
| [ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md) | [object](object.md) | range | [NamedThing](NamedThing.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [subject](subject.md) | range | [NamedThing](NamedThing.md) |
| [NamedThingAssociatedWithLikelihoodOfNamedThingAssociation](NamedThingAssociatedWithLikelihoodOfNamedThingAssociation.md) | [object](object.md) | range | [NamedThing](NamedThing.md) |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object](object.md) | range | [NamedThing](NamedThing.md) |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject](subject.md) | range | [NamedThing](NamedThing.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject](subject.md) | range | [NamedThing](NamedThing.md) |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object](object.md) | range | [NamedThing](NamedThing.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_count](has_count.md) | domain | [NamedThing](NamedThing.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_total](has_total.md) | domain | [NamedThing](NamedThing.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_quotient](has_quotient.md) | domain | [NamedThing](NamedThing.md) |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_percentage](has_percentage.md) | domain | [NamedThing](NamedThing.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject](subject.md) | range | [NamedThing](NamedThing.md) |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object](object.md) | range | [NamedThing](NamedThing.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject](subject.md) | range | [NamedThing](NamedThing.md) |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object](object.md) | range | [NamedThing](NamedThing.md) |
| [SequenceAssociation](SequenceAssociation.md) | [subject](subject.md) | range | [NamedThing](NamedThing.md) |
| [SequenceAssociation](SequenceAssociation.md) | [object](object.md) | range | [NamedThing](NamedThing.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object](object.md) | range | [NamedThing](NamedThing.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:NamedThing |
| native | bican:NamedThing |
| exact | BFO:0000001, WIKIDATA:Q35120, UMLSSG:OBJC, STY:T071, dcid:Thing |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: named thing
description: a databased entity or concept/class
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- BFO:0000001
- WIKIDATA:Q35120
- UMLSSG:OBJC
- STY:T071
- dcid:Thing
is_a: entity
slots:
- provided by
- xref
- full name
slot_usage:
  category:
    name: category
    domain_of:
    - entity
    required: true
    pattern: ^biolink:[A-Z][A-Za-z]+$

```
</details>

### Induced

<details>
```yaml
name: named thing
description: a databased entity or concept/class
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- BFO:0000001
- WIKIDATA:Q35120
- UMLSSG:OBJC
- STY:T071
- dcid:Thing
is_a: entity
slot_usage:
  category:
    name: category
    domain_of:
    - entity
    required: true
    pattern: ^biolink:[A-Z][A-Za-z]+$
attributes:
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
    owner: named thing
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
    owner: named thing
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
    owner: named thing
    domain_of:
    - named thing
    range: label type
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
    owner: named thing
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
    owner: named thing
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
    owner: named thing
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
    owner: named thing
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
    owner: named thing
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
    owner: named thing
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
    owner: named thing
    domain_of:
    - entity
    range: attribute

```
</details>