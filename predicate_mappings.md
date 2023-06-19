# Slot: predicate_mappings


_A collection of relationships that are not used in biolink, but have biolink patterns that can  be used to replace them.  This is a temporary slot to help with the transition to the fully qualified predicate model in Biolink3._



URI: [bican:predicate_mappings](https://identifiers.org/brain-bican/vocab/predicate_mappings)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MappingCollection](MappingCollection.md) | A collection of deprecated mappings |  no  |







## Properties

* Range: [PredicateMapping](PredicateMapping.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: predicate mappings
description: A collection of relationships that are not used in biolink, but have
  biolink patterns that can  be used to replace them.  This is a temporary slot to
  help with the transition to the fully qualified predicate model in Biolink3.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
multivalued: true
alias: predicate_mappings
domain_of:
- mapping collection
range: predicate mapping
inlined: true
inlined_as_list: true

```
</details>