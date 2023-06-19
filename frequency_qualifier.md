# Slot: frequency_qualifier


_a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_



URI: [bican:frequency_qualifier](https://identifiers.org/brain-bican/vocab/frequency_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **frequency_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FrequencyQualifierMixin](FrequencyQualifierMixin.md) | Qualifier for frequency type associations |  no  |
[EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | Qualifiers for entity to disease or phenotype associations |  no  |
[EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) |  |  no  |
[EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | mixin class for any association whose object (target node) is a disease |  no  |
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
[VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |  no  |
[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) |  |  no  |
[VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) |  |  no  |
[GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) |  |  no  |
[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) |  |  no  |
[VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) |  |  no  |
[GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) |  |  no  |
[CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) |  |  no  |
[OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) |  |  no  |
[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) |  |  no  |







## Properties

* Range: [FrequencyValue](FrequencyValue.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: frequency qualifier
description: a qualifier used in a phenotypic association to state how frequent the
  phenotype is observed in the subject
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: qualifier
domain: association
alias: frequency_qualifier
domain_of:
- frequency qualifier mixin
range: frequency value

```
</details>