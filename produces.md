# Slot: produces


_holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity_



URI: [bican:produces](https://identifiers.org/brain-bican/vocab/produces)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **produces**








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
name: produces
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a material entity and a product that is generated through
  the intentional actions or functioning of the material entity
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0003000
- WIKIDATA_PROPERTY:P1056
- SEMMEDDB:PRODUCES
related_mappings:
- GOREL:0001010
narrow_mappings:
- NCIT:R29
- SNOMED:has_process_output
- SNOMED:specimen_procedure_of
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: produces
range: named thing

```
</details>