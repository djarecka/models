# Slot: associated_environmental_context


_An attribute that can be applied to an association where the association holds between two entities located or occurring in a particular environment. For example, two microbial taxa may interact in the context of a human gut; a disease may give rise to a particular phenotype in a particular environmental exposure._

_ # TODO: add examples of values for this property._



URI: [bican:associated_environmental_context](https://identifiers.org/brain-bican/vocab/associated_environmental_context)




## Inheritance

* [association_slot](association_slot.md)
    * **associated_environmental_context**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | An interaction relationship between two taxa |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: associated environmental context
description: "An attribute that can be applied to an association where the association\
  \ holds between two entities located or occurring in a particular environment. For\
  \ example, two microbial taxa may interact in the context of a human gut; a disease\
  \ may give rise to a particular phenotype in a particular environmental exposure.\n\
  \ # TODO: add examples of values for this property."
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: association slot
domain: association
alias: associated_environmental_context
domain_of:
- organism taxon to organism taxon interaction
range: string

```
</details>