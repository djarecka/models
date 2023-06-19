# Slot: has_molecular_consequence


_connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583_



URI: [bican:has_molecular_consequence](https://identifiers.org/brain-bican/vocab/has_molecular_consequence)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **has_molecular_consequence**








## Properties

* Range: [OntologyClass](OntologyClass.md)

* Multivalued: True



## Aliases


* allele has activity



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
name: has molecular consequence
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: connects a sequence variant to a class describing the molecular consequence.
  E.g.  SO:0001583
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- allele has activity
narrow_mappings:
- NCIT:allele_has_activity
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: has_molecular_consequence
range: ontology class

```
</details>