# Slot: reaction_direction


_the direction of a reaction as constrained by the direction enum (ie: left_to_right, neutral, etc.)_



URI: [bican:reaction_direction](https://identifiers.org/brain-bican/vocab/reaction_direction)




## Inheritance

* [association_slot](association_slot.md)
    * **reaction_direction**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) |  |  no  |
[ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) |  |  no  |







## Properties

* Range: [ReactionDirectionEnum](ReactionDirectionEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: reaction direction
description: 'the direction of a reaction as constrained by the direction enum (ie:
  left_to_right, neutral, etc.)'
from_schema: https://identifiers.org/brain-bican/kb-model
narrow_mappings:
- NCIT:C42677
rank: 1000
is_a: association slot
domain: association
alias: reaction_direction
domain_of:
- reaction to participant association
range: ReactionDirectionEnum

```
</details>