# Slot: strand


_The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand)._



URI: [bican:strand](https://identifiers.org/brain-bican/vocab/strand)




## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **strand**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GenomicSequenceLocalization](GenomicSequenceLocalization.md) | A relationship between a sequence feature and a nucleic acid entity it is loc... |  no  |







## Properties

* Range: [StrandEnum](StrandEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: strand
description: The strand on which a feature is located. Has a value of '+' (sense strand
  or forward strand) or '-' (anti-sense strand or reverse strand).
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- gff3:strand
rank: 1000
is_a: sequence localization attribute
domain: genomic sequence localization
alias: strand
domain_of:
- genomic sequence localization
range: StrandEnum

```
</details>