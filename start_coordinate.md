# Slot: start_coordinate


_The position at which the subject genomic entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 1)._



URI: [bican:start_coordinate](https://identifiers.org/brain-bican/vocab/start_coordinate)




## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * [base_coordinate](base_coordinate.md)
            * **start_coordinate**








## Properties

* Range: [Integer](Integer.md)



## Aliases


* start



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: start coordinate
description: 'The position at which the subject genomic entity starts on the chromosome
  or other entity to which it is located on. (ie: the start of the sequence being
  referenced is 1).'
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- start
exact_mappings:
- gff3:start
close_mappings:
- faldo:begin
rank: 1000
is_a: base coordinate
domain: genomic sequence localization
alias: start_coordinate
range: integer

```
</details>