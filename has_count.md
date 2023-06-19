# Slot: has_count


_number of things with a particular property_



URI: [bican:has_count](https://identifiers.org/brain-bican/vocab/has_count)




## Inheritance

* [node_property](node_property.md)
    * [aggregate_statistic](aggregate_statistic.md)
        * **has_count**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[FrequencyQuantifier](FrequencyQuantifier.md) |  |  no  |
[EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) |  |  no  |
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
[VariantToPopulationAssociation](VariantToPopulationAssociation.md) | An association between a variant and a population, where the variant has part... |  yes  |
[VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) |  |  no  |
[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) |  |  no  |
[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) |  |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has count
description: number of things with a particular property
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- LOINC:has_count
rank: 1000
is_a: aggregate statistic
domain: named thing
alias: has_count
domain_of:
- frequency quantifier
range: integer

```
</details>