# Slot: object_part_qualifier

URI: [bican:object_part_qualifier](https://identifiers.org/brain-bican/vocab/object_part_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [part_qualifier](part_qualifier.md)
            * **object_part_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md) | describes a physical interaction between a chemical entity and a gene or gene... |  yes  |
[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: object part qualifier
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: part qualifier
domain: association
alias: object_part_qualifier
domain_of:
- predicate mapping
- chemical gene interaction association
- chemical affects gene association
range: string

```
</details>