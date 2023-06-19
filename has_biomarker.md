# Slot: has_biomarker


_holds between a disease or phenotypic feature and a measurable chemical entity that is used as an indicator of the presence or state of the disease or feature._

_ # metabolite_



URI: [bican:has_biomarker](https://identifiers.org/brain-bican/vocab/has_biomarker)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * [correlated_with](correlated_with.md)
                * **has_biomarker**








## Properties

* Range: [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has biomarker
description: "holds between a disease or phenotypic feature and a measurable chemical\
  \ entity that is used as an indicator of the presence or state of the disease or\
  \ feature.\n # metabolite"
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
narrow_mappings:
- NCIT:disease_has_molecular_abnormality
- NCIT:disease_is_marked_by_gene
rank: 1000
is_a: correlated with
domain: disease or phenotypic feature
multivalued: true
inherited: true
alias: has_biomarker
inverse: biomarker for
range: chemical entity or gene or gene product

```
</details>