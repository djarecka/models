# Slot: part_qualifier


_defines a specific part/component of the core concept (used in cases there this specific part has no IRI we can use to directly represent it, e.g. 'ESR1 transcript' q: polyA tail)._



URI: [bican:part_qualifier](https://identifiers.org/brain-bican/vocab/part_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **part_qualifier**
            * [subject_part_qualifier](subject_part_qualifier.md)
            * [object_part_qualifier](object_part_qualifier.md)








## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| polyA tail |
| upstream control region |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: part qualifier
description: 'defines a specific part/component of the core concept (used in cases
  there this specific part has no IRI we can use to directly represent it, e.g. ''ESR1
  transcript'' q: polyA tail).'
examples:
- value: polyA tail
- value: upstream control region
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: part_qualifier
range: string

```
</details>