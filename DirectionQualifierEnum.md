# Enum: DirectionQualifierEnum



URI: [DirectionQualifierEnum](DirectionQualifierEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| increased | None |  |
| upregulated | None |  |
| decreased | None |  |
| downregulated | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [subject_direction_qualifier](subject_direction_qualifier.md) |  |
| [object_direction_qualifier](object_direction_qualifier.md) |  |
| [subject_direction_qualifier](subject_direction_qualifier.md) |  |
| [object_direction_qualifier](object_direction_qualifier.md) |  |
| [object_direction_qualifier](object_direction_qualifier.md) |  |
| [object_direction_qualifier](object_direction_qualifier.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: DirectionQualifierEnum
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
permissible_values:
  increased:
    text: increased
  upregulated:
    text: upregulated
    is_a: increased
    exact_mappings:
    - RO:0002213
    close_mappings:
    - RO:0002336
    narrow_mappings:
    - RO:0004032
    - RO:0004034
    - RO:0002629
  decreased:
    text: decreased
  downregulated:
    text: downregulated
    is_a: decreased
    exact_mappings:
    - RO:0004035
    - RO:0002212
    close_mappings:
    - RO:0002335
    broad_mappings:
    - RO:0004033

```
</details>
