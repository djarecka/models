# Slot: occurs_in


_holds between a process and a material entity or site within which the process occurs_



URI: [bican:occurs_in](https://identifiers.org/brain-bican/vocab/occurs_in)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **occurs_in**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: occurs in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a process and a material entity or site within which the
  process occurs
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- BFO:0000066
- PathWhiz:has_location
- SNOMED:occurs_in
close_mappings:
- BFO:0000067
- SNOMED:has_occurrence
- UBERON:site_of
narrow_mappings:
- SEMMEDDB:OCCURS_IN
- SEMMEDDB:PROCESS_OF
- UBERON_CORE:site_of
- LOINC:has_imaged_location
- PathWhiz:in_species
- RO:0002231
- RO:0002232
- SNOMED:has_direct_procedure_site
- SNOMED:has_direct_site
- SNOMED:has_procedure_site
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: occurs_in
range: named thing

```
</details>