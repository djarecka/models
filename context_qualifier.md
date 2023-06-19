# Slot: context_qualifier


_Restricts the setting/context/location where the core concept (or qualified core concept) resides or occurs._



URI: [bican:context_qualifier](https://identifiers.org/brain-bican/vocab/context_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **context_qualifier**
            * [subject_context_qualifier](subject_context_qualifier.md)
            * [object_context_qualifier](object_context_qualifier.md)








## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| cohort x (e.g. a specific population, referenced by an identifier) |
| gut microbiome |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: context qualifier
description: Restricts the setting/context/location where the core concept (or qualified
  core concept) resides or occurs.
examples:
- value: cohort x (e.g. a specific population, referenced by an identifier)
- value: gut microbiome
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: context_qualifier
range: string

```
</details>