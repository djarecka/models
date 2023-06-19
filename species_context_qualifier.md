# Slot: species_context_qualifier


_A statement qualifier representing a taxonomic category of species in which a relationship expressed in an association took place._



URI: [bican:species_context_qualifier](https://identifiers.org/brain-bican/vocab/species_context_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [statement_qualifier](statement_qualifier.md)
            * **species_context_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |







## Properties

* Range: [OrganismTaxon](OrganismTaxon.md)






## Examples

| Value |
| --- |
| zebrafish |
| human |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: species context qualifier
description: A statement qualifier representing a taxonomic category of species in
  which a relationship expressed in an association took place.
notes:
- Ontology CURIEs are expected as values here, the examples below are intended to
  help clarify the content of the CURIEs.
examples:
- value: zebrafish
- value: human
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: statement qualifier
domain: association
alias: species_context_qualifier
domain_of:
- predicate mapping
range: organism taxon

```
</details>