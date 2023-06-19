# Slot: population_context_qualifier


_a biological population (general, study, cohort, etc.) with a specific set of characteristics to constrain an association._



URI: [bican:population_context_qualifier](https://identifiers.org/brain-bican/vocab/population_context_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **population_context_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome |  no  |







## Properties

* Range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: population context qualifier
description: a biological population (general, study, cohort, etc.) with a specific
  set of characteristics to constrain an association.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: qualifier
domain: association
alias: population_context_qualifier
domain_of:
- exposure event to outcome association
range: population of individual organisms

```
</details>