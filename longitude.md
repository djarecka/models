# Slot: longitude


_longitude_



URI: [bican:longitude](https://identifiers.org/brain-bican/vocab/longitude)




## Inheritance

* [node_property](node_property.md)
    * **longitude**





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
name: longitude
description: longitude
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- wgs:long
rank: 1000
is_a: node property
domain: named thing
alias: longitude
domain_of:
- geographic location
range: float

```
</details>