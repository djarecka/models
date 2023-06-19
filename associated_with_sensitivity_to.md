# Slot: associated_with_sensitivity_to


_A relation that holds between a named thing and a chemical that specifies that the change in the named thing is found to be associated with the degree of sensitivity to treatment by the chemical._



URI: [bican:associated_with_sensitivity_to](https://identifiers.org/brain-bican/vocab/associated_with_sensitivity_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * **associated_with_sensitivity_to**








## Properties

* Range: [ChemicalEntity](ChemicalEntity.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: associated with sensitivity to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: A relation that holds between a named thing and a chemical that specifies
  that the change in the named thing is found to be associated with the degree of
  sensitivity to treatment by the chemical.
from_schema: https://identifiers.org/brain-bican/kb-model
narrow_mappings:
- SNOMEDCT:418038007
broad_mappings:
- PATO:0000085
rank: 1000
is_a: associated with
domain: named thing
multivalued: true
inherited: true
alias: associated_with_sensitivity_to
range: chemical entity

```
</details>