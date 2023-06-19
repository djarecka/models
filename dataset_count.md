# Slot: dataset_count


_The total number of instances (e.g., number of patients, number of rows, etc) in a dataset/cohort._



URI: [bican:dataset_count](https://identifiers.org/brain-bican/vocab/dataset_count)




## Inheritance

* [association_slot](association_slot.md)
    * **dataset_count**
        * [total_sample_size](total_sample_size.md)








## Properties

* Range: [Integer](Integer.md)






## Examples

| Value |
| --- |
| 100000 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: dataset count
description: The total number of instances (e.g., number of patients, number of rows,
  etc) in a dataset/cohort.
examples:
- value: '100000'
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: association slot
domain: association
alias: dataset_count
range: integer

```
</details>