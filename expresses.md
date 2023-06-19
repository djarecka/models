# Slot: expresses


_holds between an anatomical entity and gene or gene product that is expressed there_



URI: [bican:expresses](https://identifiers.org/brain-bican/vocab/expresses)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [location_of](location_of.md)
            * **expresses**








## Properties

* Range: [GeneOrGeneProduct](GeneOrGeneProduct.md)

* Multivalued: True



## Aliases


* anatomy expresses gene



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: expresses
description: holds between an anatomical entity and gene or gene product that is expressed
  there
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- anatomy expresses gene
exact_mappings:
- RO:0002292
rank: 1000
is_a: location of
domain: anatomical entity
multivalued: true
inherited: true
alias: expresses
inverse: expressed in
range: gene or gene product

```
</details>