# Enum: StrandEnum




_strand_



URI: [StrandEnum](StrandEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| + | None | Positive |
| - | None | Negative |
| . | None | Unstranded |
| ? | None | Unknown |




## Slots

| Name | Description |
| ---  | --- |
| [genome_build](genome_build.md) | The version of the genome on which a feature is located |
| [strand](strand.md) | The strand on which a feature is located |






## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: StrandEnum
description: strand
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
permissible_values:
  +:
    text: +
    description: Positive
  '-':
    text: '-'
    description: Negative
  .:
    text: .
    description: Unstranded
  '?':
    text: '?'
    description: Unknown

```
</details>
