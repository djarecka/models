# Slot: has_topic


_Connects a node to a vocabulary term or ontology class that describes some aspect of the entity. In general specific characterization is preferred. See https://github.com/biolink/biolink-model/issues/238_



URI: [bican:has_topic](https://identifiers.org/brain-bican/vocab/has_topic)




## Inheritance

* [node_property](node_property.md)
    * **has_topic**








## Properties

* Range: [OntologyClass](OntologyClass.md)



## Aliases


* topic
* descriptors



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: has topic
description: Connects a node to a vocabulary term or ontology class that describes
  some aspect of the entity. In general specific characterization is preferred. See
  https://github.com/biolink/biolink-model/issues/238
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- topic
- descriptors
exact_mappings:
- foaf:topic
rank: 1000
is_a: node property
domain: named thing
alias: has_topic
range: ontology class

```
</details>