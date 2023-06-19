# Slot: interbase_coordinate


_A position in interbase coordinates. Interbase coordinates start at position 0 instead of position 1. This is applied to a sequence localization edge._



URI: [bican:interbase_coordinate](https://identifiers.org/brain-bican/vocab/interbase_coordinate)




## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **interbase_coordinate**
            * [start_interbase_coordinate](start_interbase_coordinate.md)
            * [end_interbase_coordinate](end_interbase_coordinate.md)








## Properties

* Range: [Integer](Integer.md)



## Aliases


* zero-based
* half-open
* space-based



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: interbase coordinate
description: A position in interbase coordinates. Interbase coordinates start at position
  0 instead of position 1. This is applied to a sequence localization edge.
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- zero-based
- half-open
- space-based
rank: 1000
is_a: sequence localization attribute
domain: genomic sequence localization
alias: interbase_coordinate
range: integer

```
</details>