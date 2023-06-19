# Slot: affiliation


_a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations._



URI: [bican:affiliation](https://identifiers.org/brain-bican/vocab/affiliation)




## Inheritance

* [node_property](node_property.md)
    * **affiliation**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Agent](Agent.md) | person, group, organization or project that provides a piece of information (... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: affiliation
description: a professional relationship between one provider (often a person) within
  another provider (often an organization). Target provider identity should be specified
  by a CURIE. Providers may have multiple affiliations.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: node property
domain: agent
multivalued: true
alias: affiliation
domain_of:
- agent
range: uriorcurie

```
</details>