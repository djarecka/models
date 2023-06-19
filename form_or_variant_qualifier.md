# Slot: form_or_variant_qualifier


_A qualifier that composes with a core subject/object concept to define a specific type, variant, alternative version of this concept. The composed concept remains a subtype or instance of the core concept. For example, the qualifier ‘mutation’ combines with the core concept ‘Gene X’ to express the compose concept ‘a mutation of Gene X’._



URI: [bican:form_or_variant_qualifier](https://identifiers.org/brain-bican/vocab/form_or_variant_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **form_or_variant_qualifier**
            * [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md)
            * [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md)








## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| mutation |
| late stage |
| severe |
| transplant |
| chemical analog |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: form or variant qualifier
description: A qualifier that composes with a core subject/object concept to define
  a specific type, variant, alternative version of this concept. The composed concept
  remains a subtype or instance of the core concept. For example, the qualifier ‘mutation’
  combines with the core concept ‘Gene X’ to express the compose concept ‘a mutation
  of Gene X’.
notes:
- please see the ChemicalOrGeneOrGeneProductFormOrVariantEnum (below) for examples
  of 'form or variant qualifier' terms in the gene->chemical association space.  the
  qualifier ‘mutation’ combines with the core concept ‘Gene X’ to express the compose
  concept ‘Mutated forms of Gene X’. the qualifier ‘late stage’ combines with a core
  concept of ‘Disease X’ to express the  more specific concept ‘Late Stage forms of
  Disease X’ the qualifier ‘recombinant’ combines with a core concept of ‘FLT1 Gene’
  to express the composed concept ‘Recombinant forms of the FLT1 gene’ the qualifier
  ‘chemical analog’ combines with a core concept of ‘Ditiocarb’ to express the composed
  concept ‘analog forms of Ditiocarb’
examples:
- value: mutation
- value: late stage
- value: severe
- value: transplant
- value: chemical analog
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: qualifier
abstract: true
domain: association
alias: form_or_variant_qualifier
range: string

```
</details>