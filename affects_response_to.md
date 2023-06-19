# Slot: affects_response_to

URI: [bican:affects_response_to](https://identifiers.org/brain-bican/vocab/affects_response_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **affects_response_to**
                * [increases_response_to](increases_response_to.md)
                * [decreases_response_to](decreases_response_to.md)








## Properties

* Range: [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)

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
name: affects response to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- CTD:affects_response_to
rank: 1000
is_a: affects
domain: chemical entity or gene or gene product
multivalued: true
inherited: true
alias: affects_response_to
inverse: response affected by
range: chemical entity or gene or gene product

```
</details>