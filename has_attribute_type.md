# Slot: has_attribute_type


_connects an attribute to a class that describes it_



URI: [bican:has_attribute_type](https://identifiers.org/brain-bican/vocab/has_attribute_type)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Attribute](Attribute.md) | A property or characteristic of an entity |  no  |
[ChemicalRole](ChemicalRole.md) | 	A role played by the molecular entity or part thereof within a chemical cont... |  no  |
[BiologicalSex](BiologicalSex.md) |  |  no  |
[PhenotypicSex](PhenotypicSex.md) | An attribute corresponding to the phenotypic sex of the individual, based upo... |  no  |
[GenotypicSex](GenotypicSex.md) | An attribute corresponding to the genotypic sex of the individual, based upon... |  no  |
[SeverityValue](SeverityValue.md) | describes the severity of a phenotypic feature or disease |  no  |
[OrganismAttribute](OrganismAttribute.md) | describes a characteristic of an organismal entity |  no  |
[PhenotypicQuality](PhenotypicQuality.md) | A property of a phenotype |  no  |
[Zygosity](Zygosity.md) |  |  no  |
[ClinicalAttribute](ClinicalAttribute.md) | Attributes relating to a clinical manifestation |  no  |
[ClinicalMeasurement](ClinicalMeasurement.md) | A clinical measurement is a special kind of attribute which results from a la... |  yes  |
[ClinicalModifier](ClinicalModifier.md) | Used to characterize and specify the phenotypic abnormalities defined in the ... |  no  |
[ClinicalCourse](ClinicalCourse.md) | The course a disease typically takes from its onset, progression in time, and... |  no  |
[Onset](Onset.md) | The age group in which (disease) symptom manifestations appear |  no  |
[SocioeconomicAttribute](SocioeconomicAttribute.md) | Attributes relating to a socioeconomic manifestation |  no  |
[GenomicBackgroundExposure](GenomicBackgroundExposure.md) | A genomic background exposure is where an individual's specific genomic backg... |  no  |
[PathologicalProcessExposure](PathologicalProcessExposure.md) | A pathological process, when viewed as an exposure, representing a preconditi... |  no  |
[PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | An abnormal anatomical structure, when viewed as an exposure, representing an... |  no  |
[DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | A disease or phenotypic feature state, when viewed as an exposure, represents... |  no  |
[ChemicalExposure](ChemicalExposure.md) | A chemical exposure is an intake of a particular chemical entity |  no  |
[ComplexChemicalExposure](ComplexChemicalExposure.md) | A complex chemical exposure is an intake of a chemical mixture (e |  no  |
[DrugExposure](DrugExposure.md) | A drug exposure is an intake of a particular drug |  no  |
[DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | drug to gene interaction exposure is a drug exposure is where the interaction... |  no  |
[BioticExposure](BioticExposure.md) | An external biotic exposure is an intake of (sometimes pathological) biologic... |  no  |
[GeographicExposure](GeographicExposure.md) | A geographic exposure is a factor relating to geographic proximity to some im... |  no  |
[EnvironmentalExposure](EnvironmentalExposure.md) | A environmental exposure is a factor relating to abiotic processes in the env... |  no  |
[BehavioralExposure](BehavioralExposure.md) | A behavioral exposure is a factor relating to behavior impacting an individua... |  no  |
[SocioeconomicExposure](SocioeconomicExposure.md) | A socioeconomic exposure is a factor relating to social and financial status ... |  no  |







## Properties

* Range: [OntologyClass](OntologyClass.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
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
domain_of:
- attribute
range: ontology class
required: true

```
</details>