# Slot: subject_direction_qualifier

URI: [bican:subject_direction_qualifier](https://identifiers.org/brain-bican/vocab/subject_direction_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [direction_qualifier](direction_qualifier.md)
            * **subject_direction_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  yes  |







## Properties

* Range: [DirectionQualifierEnum](DirectionQualifierEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: subject direction qualifier
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: direction qualifier
domain: association
alias: subject_direction_qualifier
domain_of:
- predicate mapping
- chemical affects gene association
range: DirectionQualifierEnum

```
</details>