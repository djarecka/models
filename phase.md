# Slot: phase


_The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2._



URI: [bican:phase](https://identifiers.org/brain-bican/vocab/phase)




## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **phase**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |  no  |







## Properties

* Range: [PhaseEnum](PhaseEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: phase
description: The phase for a coding sequence entity. For example, phase of a CDS as
  represented in a GFF3 with a value of 0, 1 or 2.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- gff3:phase
rank: 1000
is_a: sequence localization attribute
domain: coding sequence
alias: phase
domain_of:
- genomic sequence localization
range: PhaseEnum

```
</details>