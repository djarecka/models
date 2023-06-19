# Slot: publication_type


_Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass._



URI: [dct:type](http://purl.org/dc/terms/type)



<!-- no inheritance hierarchy -->







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: publication type
description: Ontology term for publication type may be drawn from Dublin Core types
  (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned
  Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html),
  the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation
  of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres
  (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata
  (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication
  type ontology. When a given publication type ontology term is used within a given
  knowledge graph, then the CURIE identified term must be documented in the graph
  as a concept node of biolink:category biolink:OntologyClass.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
values_from:
- dctypes
- fabio
- MESH_PUB
- COAR_RESOURCE
- WIKIDATA
slot_uri: dct:type
multivalued: true
alias: publication_type
range: string

```
</details>