# Class: RelationshipType


_An OWL property used as an edge label_





URI: [bican:RelationshipType](https://identifiers.org/brain-bican/vocab/RelationshipType)



```mermaid
 classDiagram
    class RelationshipType
      OntologyClass <|-- RelationshipType
      
      RelationshipType : id
        
      
```





## Inheritance
* [OntologyClass](OntologyClass.md)
    * **RelationshipType**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for an entity | [OntologyClass](OntologyClass.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:RelationshipType |
| native | bican:RelationshipType |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: relationship type
description: An OWL property used as an edge label
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: ontology class

```
</details>

### Induced

<details>
```yaml
name: relationship type
description: An OWL property used as an edge label
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: ontology class
attributes:
  id:
    name: id
    description: A unique identifier for an entity. Must be either a CURIE shorthand
      for a URI or a complete URI
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - AGRKB:primaryId
    - gff3:ID
    - gpi:DB_Object_ID
    rank: 1000
    domain: entity
    identifier: true
    alias: id
    owner: relationship type
    domain_of:
    - genome assembly
    - ontology class
    - entity
    range: string
    required: true

```
</details>