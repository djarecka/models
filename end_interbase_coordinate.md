# Slot: end_interbase_coordinate


_The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on._



URI: [bican:end_interbase_coordinate](https://identifiers.org/brain-bican/vocab/end_interbase_coordinate)




## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * [interbase_coordinate](interbase_coordinate.md)
            * **end_interbase_coordinate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |  no  |







## Properties

* Range: [Integer](Integer.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| opposite_of | start interbase coordinate |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: end interbase coordinate
annotations:
  opposite_of:
    tag: opposite_of
    value: start interbase coordinate
description: The position at which the subject nucleic acid entity ends on the chromosome
  or other entity to which it is located on.
from_schema: https://identifiers.org/brain-bican/kb-model
close_mappings:
- faldo:end
rank: 1000
is_a: interbase coordinate
domain: genomic sequence localization
alias: end_interbase_coordinate
domain_of:
- genomic sequence localization
range: integer

```
</details>