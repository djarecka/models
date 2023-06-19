# Slot: end_coordinate


_The position at which the subject genomic entity ends on the chromosome or other entity to which it is located on._



URI: [bican:end_coordinate](https://identifiers.org/brain-bican/vocab/end_coordinate)




## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * [base_coordinate](base_coordinate.md)
            * **end_coordinate**








## Properties

* Range: [Integer](Integer.md)



## Aliases


* end



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: end coordinate
description: The position at which the subject genomic entity ends on the chromosome
  or other entity to which it is located on.
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- end
exact_mappings:
- gff3:end
close_mappings:
- faldo:end
rank: 1000
is_a: base coordinate
domain: genomic sequence localization
alias: end_coordinate
range: integer

```
</details>