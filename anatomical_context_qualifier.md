# Slot: anatomical_context_qualifier


_A statement qualifier representing an anatomical location where an relationship expressed in an association took place (can be a tissue, cell type, or sub-cellular location)._



URI: [bican:anatomical_context_qualifier](https://identifiers.org/brain-bican/vocab/anatomical_context_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [statement_qualifier](statement_qualifier.md)
            * **anatomical_context_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes a physical interaction between a chemical entity and a gene or gene... |  yes  |
[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  yes  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| blood |
| cerebral cortext |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: anatomical context qualifier
description: A statement qualifier representing an anatomical location where an relationship
  expressed in an association took place (can be a tissue, cell type, or sub-cellular
  location).
notes:
- Anatomical context values can be any term from UBERON. For example, the context
  qualifier ‘cerebral cortext’  combines with a core concept of ‘neuron’  to express
  the composed concept ‘neuron in the cerebral cortext’. The species_context_qualifier
  applies  taxonomic context, e.g. species-specific molecular activity.  Ontology
  CURIEs are expected as values  here, the examples below are intended to help clarify
  the content of the CURIEs.
examples:
- value: blood
- value: cerebral cortext
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: statement qualifier
domain: association
alias: anatomical_context_qualifier
domain_of:
- predicate mapping
- chemical gene interaction association
- chemical affects gene association
range: string

```
</details>