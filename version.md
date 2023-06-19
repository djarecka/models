# Slot: version

URI: [bican:version](https://identifiers.org/brain-bican/vocab/version)




## Inheritance

* [node_property](node_property.md)
    * **version**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomeAnnotation](GenomeAnnotation.md) | Location and nomenclature of genes and all of the coding regions in a genome ... |  no  |
[GenomeAssembly](GenomeAssembly.md) | Genome assembly to contain version and label information |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: version
from_schema: https://identifiers.org/brain-bican/kb-model
broad_mappings:
- pav:version
- owl:versionInfo
rank: 1000
is_a: node property
domain: dataset
alias: version
domain_of:
- genome annotation
- genome assembly
range: string

```
</details>