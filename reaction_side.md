# Slot: reaction_side


_the side of a reaction being modeled (ie: left or right)_



URI: [bican:reaction_side](https://identifiers.org/brain-bican/vocab/reaction_side)




## Inheritance

* [association_slot](association_slot.md)
    * **reaction_side**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) |  |  no  |
[ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) |  |  no  |







## Properties

* Range: [ReactionSideEnum](ReactionSideEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: reaction side
description: 'the side of a reaction being modeled (ie: left or right)'
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: association slot
domain: association
alias: reaction_side
domain_of:
- reaction to participant association
range: ReactionSideEnum

```
</details>