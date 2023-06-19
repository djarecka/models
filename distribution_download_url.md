# Slot: distribution_download_url

URI: [bican:distribution_download_url](https://identifiers.org/brain-bican/vocab/distribution_download_url)




## Inheritance

* [node_property](node_property.md)
    * **distribution_download_url**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[DatasetDistribution](DatasetDistribution.md) | an item that holds distribution level information about a dataset |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: distribution download url
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- dcat:downloadURL
rank: 1000
is_a: node property
domain: dataset distribution
alias: distribution_download_url
domain_of:
- dataset distribution
range: string

```
</details>