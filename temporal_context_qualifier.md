# Slot: temporal_context_qualifier


_a constraint of time placed upon the truth value of an association. for time intervales, use temporal interval qualifier._



URI: [bican:temporal_context_qualifier](https://identifiers.org/brain-bican/vocab/temporal_context_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **temporal_context_qualifier**
            * [temporal_interval_qualifier](temporal_interval_qualifier.md)





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | An association between an exposure event and an outcome |  no  |







## Properties

* Range: [TimeType](TimeType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: temporal context qualifier
description: a constraint of time placed upon the truth value of an association. for
  time intervales, use temporal interval qualifier.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: qualifier
domain: association
alias: temporal_context_qualifier
domain_of:
- exposure event to outcome association
range: time type

```
</details>