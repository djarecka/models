# Slot: causal_mechanism_qualifier


_A statement qualifier representing a type of molecular control mechanism through which an effect of a chemical on a gene or gene product is mediated (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')_



URI: [bican:causal_mechanism_qualifier](https://identifiers.org/brain-bican/vocab/causal_mechanism_qualifier)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * [statement_qualifier](statement_qualifier.md)
            * **causal_mechanism_qualifier**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  yes  |







## Properties

* Range: [CausalMechanismQualifierEnum](CausalMechanismQualifierEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: causal mechanism qualifier
description: A statement qualifier representing a type of molecular control mechanism
  through which an effect of a chemical on a gene or gene product is mediated (e.g.
  'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: statement qualifier
domain: association
alias: causal_mechanism_qualifier
domain_of:
- predicate mapping
- chemical affects gene association
range: CausalMechanismQualifierEnum

```
</details>