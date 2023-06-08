# Slot: cell_type_name


_The primary name/symbol to be used for the cell type defined by this cell set._



URI: [ccn2:cell_type_name](https://github.com/brain-bican/CCN2cell_type_name)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Taxonomy](Taxonomy.md) |  |  yes  |
[CrossTaxonomyMapping](CrossTaxonomyMapping.md) |  |  yes  |
[LocationMapping](LocationMapping.md) |  |  yes  |







## Properties

* Range: [String](String.md)



## Aliases


* primary_cell_type_alias



## Identifier and Mapping Information







### Schema Source


* from schema: CCN2




## LinkML Source

<details>
```yaml
name: cell type name
description: The primary name/symbol to be used for the cell type defined by this
  cell set.
from_schema: CCN2
aliases:
- primary_cell_type_alias
rank: 1000
alias: cell_type_name
domain_of:
- taxonomy
- cross taxonomy mapping
- location mapping
range: string

```
</details>