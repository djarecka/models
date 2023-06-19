# Slot: has_device


_connects an entity to one or more (medical) devices_



URI: [bican:has_device](https://identifiers.org/brain-bican/vocab/has_device)




## Inheritance

* [node_property](node_property.md)
    * **has_device**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Treatment](Treatment.md) | A treatment is targeted at a disease or phenotype and may involve multiple dr... |  no  |







## Properties

* Range: [Device](Device.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has device
description: connects an entity to one or more (medical) devices
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: node property
domain: named thing
multivalued: true
alias: has_device
domain_of:
- treatment
range: device

```
</details>