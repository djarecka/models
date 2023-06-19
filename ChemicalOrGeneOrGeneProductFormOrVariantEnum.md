# Enum: ChemicalOrGeneOrGeneProductFormOrVariantEnum



URI: [ChemicalOrGeneOrGeneProductFormOrVariantEnum](ChemicalOrGeneOrGeneProductFormOrVariantEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| genetic_variant_form | None |  |
| modified_form | None |  |
| loss_of_function_variant_form | None |  |
| gain_of_function_variant_form | None |  |
| polymorphic_form | None |  |
| snp_form | None |  |
| analog_form | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) |  |
| [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) |  |
| [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) |  |
| [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: ChemicalOrGeneOrGeneProductFormOrVariantEnum
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
permissible_values:
  genetic_variant_form:
    text: genetic_variant_form
    is_a: modified_form
  modified_form:
    text: modified_form
  loss_of_function_variant_form:
    text: loss_of_function_variant_form
    is_a: genetic_variant_form
  gain_of_function_variant_form:
    text: gain_of_function_variant_form
    is_a: genetic_variant_form
  polymorphic_form:
    text: polymorphic_form
    is_a: genetic_variant_form
  snp_form:
    text: snp_form
    is_a: polymorphic_form
  analog_form:
    text: analog_form
    is_a: modified_form

```
</details>
