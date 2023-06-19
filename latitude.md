# Slot: latitude


_latitude_



URI: [bican:latitude](https://identifiers.org/brain-bican/vocab/latitude)




## Inheritance

* [node_property](node_property.md)
    * **latitude**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[GeographicLocation](GeographicLocation.md) | a location that can be described in lat/long coordinates |  no  |
[GeographicLocationAtTime](GeographicLocationAtTime.md) | a location that can be described in lat/long coordinates, for a particular ti... |  no  |







## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: latitude
description: latitude
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- wgs:lat
rank: 1000
is_a: node property
domain: named thing
alias: latitude
domain_of:
- geographic location
range: float

```
</details>