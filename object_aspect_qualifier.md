# Slot: object_aspect_qualifier

URI: [bican:object_aspect_qualifier](https://identifiers.org/brain-bican/vocab/object_aspect_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [aspect_qualifier](aspect_qualifier.md)
            * **object_aspect_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: object aspect qualifier
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: aspect qualifier
domain: association
alias: object_aspect_qualifier
domain_of:
- predicate mapping
- chemical affects gene association
range: string

```
</details>