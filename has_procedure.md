# Slot: has_procedure


_connects an entity to one or more (medical) procedures_



URI: [bican:has_procedure](https://identifiers.org/brain-bican/vocab/has_procedure)




## Inheritance

* [node_property](node_property.md)
    * **has_procedure**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple dr... |  no  |







## Properties

* Range: [Procedure](Procedure.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has procedure
description: connects an entity to one or more (medical) procedures
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: node property
domain: named thing
multivalued: true
alias: has_procedure
domain_of:
- treatment
range: procedure

```
</details>