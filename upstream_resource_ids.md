# Slot: upstream_resource_ids


_An upstream InformationResource from which the resource being described directly retrieved a record of the knowledge expressed in the Edge, or data used to generate this knowledge. This is an array because there are cases where a merged Edge holds knowledge that was retrieved from multiple sources. e.g. an Edge provided by the ARAGORN ARA can expressing knowledge it retrieved from both the automat-mychem-info and molepro KPs, which both provided it with records of this single fact._



URI: [bican:upstream_resource_ids](https://identifiers.org/brain-bican/vocab/upstream_resource_ids)




## Inheritance

* [node_property](node_property.md)
    * **upstream_resource_ids**





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
name: upstream resource ids
description: An upstream InformationResource from which the resource being described
  directly retrieved a record of the knowledge expressed in the Edge, or data used
  to generate this knowledge. This is an array because there are cases where a merged
  Edge holds knowledge that was retrieved from multiple sources. e.g. an Edge provided
  by the ARAGORN ARA can expressing knowledge it retrieved from both the automat-mychem-info
  and molepro KPs, which both provided it with records of this single fact.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: node property
domain: retrieval source
alias: upstream_resource_ids
domain_of:
- retrieval source
range: uriorcurie

```
</details>