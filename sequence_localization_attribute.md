# Slot: sequence_localization_attribute


_An attribute that can be applied to a genome sequence localization edge. These edges connect a nucleic acid entity such as an exon to an entity such as a chromosome. Edge properties are used to ascribe specific positional information and other metadata to the localization. In pragmatic terms this can be thought of as columns in a GFF3 line._



URI: [bican:sequence_localization_attribute](https://identifiers.org/brain-bican/vocab/sequence_localization_attribute)




## Inheritance

* [association_slot](association_slot.md)
    * **sequence_localization_attribute**
        * [base_coordinate](base_coordinate.md)
        * [interbase_coordinate](interbase_coordinate.md)
        * [genome_build](genome_build.md)
        * [strand](strand.md)
        * [phase](phase.md)








## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: sequence localization attribute
description: An attribute that can be applied to a genome sequence localization edge.
  These edges connect a nucleic acid entity such as an exon to an entity such as a
  chromosome. Edge properties are used to ascribe specific positional information
  and other metadata to the localization. In pragmatic terms this can be thought of
  as columns in a GFF3 line.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: association slot
domain: genomic sequence localization
alias: sequence_localization_attribute
range: string

```
</details>