# Slot: genome_build


_The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens._



URI: [bican:genome_build](https://identifiers.org/brain-bican/vocab/genome_build)




## Inheritance

* [association_slot](association_slot.md)
    * [sequence_localization_attribute](sequence_localization_attribute.md)
        * **genome_build**





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
name: genome build
description: The version of the genome on which a feature is located. For example,
  GRCh38 for Homo sapiens.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- gff3:strand
rank: 1000
is_a: sequence localization attribute
domain: genomic sequence localization
alias: genome_build
domain_of:
- genomic sequence localization
range: StrandEnum

```
</details>