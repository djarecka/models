# Slot: resource_id


_The CURIE for an Information Resource that served as a source of knowledge expressed in an Edge, or a source of data used to generate this knowledge._



URI: [bican:resource_id](https://identifiers.org/brain-bican/vocab/resource_id)




## Inheritance

* [node_property](node_property.md)
    * **resource_id**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[RetrievalSource](RetrievalSource.md) | Provides information about how a particular InformationResource served as a s... |  yes  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: resource id
description: The CURIE for an Information Resource that served as a source of knowledge
  expressed in an Edge, or a source of data used to generate this knowledge.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: node property
domain: retrieval source
alias: resource_id
domain_of:
- retrieval source
range: uriorcurie

```
</details>