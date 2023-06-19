# Slot: direction_qualifier


_Composes with the core concept (+ aspect if provided) to describe a change in its direction or degree._



URI: [bican:direction_qualifier](https://identifiers.org/brain-bican/vocab/direction_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **direction_qualifier**
            * [subject_direction_qualifier](subject_direction_qualifier.md)
            * [object_direction_qualifier](object_direction_qualifier.md)








## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: direction qualifier
description: Composes with the core concept (+ aspect if provided) to describe a change
  in its direction or degree.
notes:
- the qualifier ‘increased’ combines with a core concept of ‘Gene X’ and an aspect
  of ‘expression’ to express the composed concept ‘increased expression of Gene X’    the
  qualifier ‘decreased’ combines with a core concept of ‘Protein X’ and an aspect
  of ‘abundance’ to express the composed concept ‘decreased abundance of Protein X’
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: direction_qualifier
range: string

```
</details>