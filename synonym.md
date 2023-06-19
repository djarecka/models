# Slot: synonym


_Alternate human-readable names for a thing_



URI: [bican:synonym](https://identifiers.org/brain-bican/vocab/synonym)




## Inheritance

* [node_property](node_property.md)
    * **synonym**
        * [exact_synonym](exact_synonym.md)
        * [broad_synonym](broad_synonym.md)
        * [narrow_synonym](narrow_synonym.md)
        * [related_synonym](related_synonym.md)





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |  no  |
[GeneProductMixin](GeneProductMixin.md) | The functional molecular product of a single gene locus |  no  |
[GeneAnnotation](GeneAnnotation.md) | An annotation describing the location, boundaries, and functions of  individu... |  no  |
[GeneProductIsoformMixin](GeneProductIsoformMixin.md) | This is an abstract class that can be mixed in with different kinds of gene p... |  no  |
[NucleosomeModification](NucleosomeModification.md) | A chemical modification of a histone protein within a nucleosome octomer or a... |  no  |
[Protein](Protein.md) | A gene product that is composed of a chain of amino acid sequences and is pro... |  no  |
[ProteinIsoform](ProteinIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |  no  |
[PosttranslationalModification](PosttranslationalModification.md) | A chemical modification of a polypeptide or protein that occurs after transla... |  no  |
[RNAProduct](RNAProduct.md) |  |  no  |
[RNAProductIsoform](RNAProductIsoform.md) | Represents a protein that is a specific isoform of the canonical or reference... |  no  |
[NoncodingRNAProduct](NoncodingRNAProduct.md) |  |  no  |
[MicroRNA](MicroRNA.md) |  |  no  |
[SiRNA](SiRNA.md) | A small RNA molecule that is the product of a longer exogenous or endogenous ... |  no  |







## Properties

* Range: [LabelType](LabelType.md)

* Multivalued: True



## Aliases


* alias



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: synonym
description: Alternate human-readable names for a thing
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- alias
narrow_mappings:
- skos:altLabel
- gff3:Alias
- AGRKB:synonyms
- gpi:DB_Object_Synonyms
- HANCESTRO:0330
- IAO:0000136
- RXNORM:has_tradename
rank: 1000
is_a: node property
domain: named thing
multivalued: true
alias: synonym
domain_of:
- gene
- gene product mixin
range: label type

```
</details>