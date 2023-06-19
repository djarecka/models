# Slot: genetically_associated_with

URI: [bican:genetically_associated_with](https://identifiers.org/brain-bican/vocab/genetically_associated_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * **genetically_associated_with**
                * [gene_associated_with_condition](gene_associated_with_condition.md)
                * [condition_associated_with_gene](condition_associated_with_gene.md)








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True || description | Co-occurrence of a certain allele of a genetic marker and the phenotype of interest in the same individuals at above-chance level |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: genetically associated with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
  description:
    tag: description
    value: Co-occurrence of a certain allele of a genetic marker and the phenotype
      of interest in the same individuals at above-chance level
description: ''
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA_PROPERTY:P2293
rank: 1000
is_a: associated with
domain: named thing
multivalued: true
inherited: true
alias: genetically_associated_with
symmetric: true
range: named thing

```
</details>