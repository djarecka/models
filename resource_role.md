# Slot: resource_role


_The role played by the InformationResource in serving as a source for an Edge. Note that a given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting data' sources._



URI: [bican:resource_role](https://identifiers.org/brain-bican/vocab/resource_role)




## Inheritance

* [node_property](node_property.md)
    * **resource_role**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[RetrievalSource](RetrievalSource.md) | Provides information about how a particular InformationResource served as a s... |  yes  |







## Properties

* Range: [ResourceRoleEnum](ResourceRoleEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: resource role
description: The role played by the InformationResource in serving as a source for
  an Edge. Note that a given Edge should have one and only one 'primary' source, and
  may have any number of 'aggregator' or 'supporting data' sources.
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: node property
domain: retrieval source
alias: resource_role
domain_of:
- retrieval source
range: ResourceRoleEnum

```
</details>