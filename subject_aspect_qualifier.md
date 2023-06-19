# Slot: subject_aspect_qualifier

URI: [bican:subject_aspect_qualifier](https://identifiers.org/brain-bican/vocab/subject_aspect_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [aspect_qualifier](aspect_qualifier.md)
            * **subject_aspect_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  yes  |
[GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) |  |  yes  |
[GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) |  |  no  |
[GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) |  |  no  |
[CausalGeneToDiseaseAssociation](CausalGeneToDiseaseAssociation.md) |  |  no  |
[CorrelatedGeneToDiseaseAssociation](CorrelatedGeneToDiseaseAssociation.md) |  |  no  |
[DruggableGeneToDiseaseAssociation](DruggableGeneToDiseaseAssociation.md) |  |  no  |
[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) |  |  no  |
[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: subject aspect qualifier
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: aspect qualifier
domain: association
alias: subject_aspect_qualifier
domain_of:
- predicate mapping
- chemical affects gene association
- gene to disease or phenotypic feature association
range: string

```
</details>