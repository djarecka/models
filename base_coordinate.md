# Slot: base_coordinate


_A position in the base coordinate system.  Base coordinates start at position 1 instead of position 0._



URI: [bican:base_coordinate](https://identifiers.org/brain-bican/vocab/base_coordinate)




## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **base_coordinate**
            * [start_coordinate](start_coordinate.md)
            * [end_coordinate](end_coordinate.md)








## Properties

* Range: [Integer](Integer.md)



## Aliases


* one-based
* fully-closed



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: base coordinate
description: A position in the base coordinate system.  Base coordinates start at
  position 1 instead of position 0.
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- one-based
- fully-closed
rank: 1000
is_a: sequence localization attribute
domain: genomic sequence localization
alias: base_coordinate
range: integer

```
</details>