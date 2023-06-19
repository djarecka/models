# Enum: LogicalInterpretationEnum



URI: [LogicalInterpretationEnum](LogicalInterpretationEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| some_some | os:SomeSomeInterpretation | A modifier on a triple that causes the triple to be interpreted as a some-som... |
| all_some | os:AllSomeInterpretation | A modifier on a triple that causes the triple to be interpreted as an all-som... |
| inverse_all_some | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [logical_interpretation](logical_interpretation.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: LogicalInterpretationEnum
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
permissible_values:
  some_some:
    text: some_some
    description: A modifier on a triple that causes the triple to be interpreted as
      a some-some statement
    meaning: os:SomeSomeInterpretation
  all_some:
    text: all_some
    description: A modifier on a triple that causes the triple to be interpreted as
      an all-some statement.
    meaning: os:AllSomeInterpretation
  inverse_all_some:
    text: inverse_all_some

```
</details>
