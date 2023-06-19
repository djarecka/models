# Slot: derivative_qualifier


_A qualifier that composes with a core subject/object  concept to describe something that is derived from the core concept.  For example, the qualifier ‘metabolite’ combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite of Chemical X’._



URI: [bican:derivative_qualifier](https://identifiers.org/brain-bican/vocab/derivative_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **derivative_qualifier**
            * [subject_derivative_qualifier](subject_derivative_qualifier.md)
            * [object_derivative_qualifier](object_derivative_qualifier.md)








## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| metabolite |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: derivative qualifier
description: A qualifier that composes with a core subject/object  concept to describe
  something that is derived from the core concept.  For example, the qualifier ‘metabolite’
  combines with a ‘Chemical X’ core concept to express the composed concept ‘a metabolite
  of Chemical X’.
examples:
- value: metabolite
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: derivative_qualifier
range: string

```
</details>