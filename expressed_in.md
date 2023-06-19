# Slot: expressed_in


_holds between a gene or gene product and an anatomical entity in which it is expressed_



URI: [bican:expressed_in](https://identifiers.org/brain-bican/vocab/expressed_in)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [located_in](located_in.md)
            * **expressed_in**








## Properties

* Range: [AnatomicalEntity](AnatomicalEntity.md)

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
name: expressed in
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: holds between a gene or gene product and an anatomical entity in which
  it is expressed
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002206
narrow_mappings:
- NCIT:R49
- NCIT:R46
rank: 1000
is_a: located in
domain: gene or gene product
multivalued: true
inherited: true
alias: expressed_in
range: anatomical entity

```
</details>