# Slot: has_drug


_connects an entity to one or more drugs_



URI: [bican:has_drug](https://identifiers.org/brain-bican/vocab/has_drug)




## Inheritance

* [node_property](node_property.md)
    * **has_drug**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple dr... |  no  |







## Properties

* Range: [Drug](Drug.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has drug
description: connects an entity to one or more drugs
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: node property
domain: named thing
multivalued: true
alias: has_drug
domain_of:
- treatment
range: drug

```
</details>