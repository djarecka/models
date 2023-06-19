# Slot: symbol


_Symbol for a particular thing_



URI: [bican:symbol](https://identifiers.org/brain-bican/vocab/symbol)




## Inheritance

* [node_property](node_property.md)
    * **symbol**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |  no  |
[GeneAnnotation](GeneAnnotation.md) | An annotation describing the location, boundaries, and functions of  individu... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: symbol
description: Symbol for a particular thing
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- AGRKB:symbol
- gpi:DB_Object_Symbol
rank: 1000
is_a: node property
domain: named thing
alias: symbol
domain_of:
- gene
range: string

```
</details>