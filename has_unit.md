# Slot: has_unit


_connects a quantity value to a unit_



URI: [bican:has_unit](https://identifiers.org/brain-bican/vocab/has_unit)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[QuantityValue](QuantityValue.md) | A value of an attribute that is quantitative and measurable, expressed as a c... |  no  |







## Properties

* Range: [Unit](Unit.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has unit
description: connects a quantity value to a unit
in_subset:
- samples
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- qud:unit
- IAO:0000039
close_mappings:
- EFO:0001697
- UO-PROPERTY:is_unit_of
narrow_mappings:
- SNOMED:has_concentration_strength_denominator_unit
- SNOMED:has_concentration_strength_numerator_unit
- SNOMED:has_presentation_strength_denominator_unit
- SNOMED:has_presentation_strength_numerator_unit
- SNOMED:has_unit_of_presentation
rank: 1000
domain: quantity value
multivalued: false
alias: has_unit
domain_of:
- quantity value
range: unit

```
</details>