# Class: SocioeconomicExposure


_A socioeconomic exposure is a factor relating to social and financial status of an affected individual (e.g. poverty)._





URI: [bican:SocioeconomicExposure](https://identifiers.org/brain-bican/vocab/SocioeconomicExposure)



```mermaid
 classDiagram
    class SocioeconomicExposure
      ExposureEvent <|-- SocioeconomicExposure
      Attribute <|-- SocioeconomicExposure
      
      SocioeconomicExposure : category
        
      SocioeconomicExposure : description
        
      SocioeconomicExposure : full_name
        
      SocioeconomicExposure : has_attribute
        
          SocioeconomicExposure --|> socioeconomic attribute : has_attribute
        
      SocioeconomicExposure : has_attribute_type
        
          SocioeconomicExposure --|> ontology class : has_attribute_type
        
      SocioeconomicExposure : has_qualitative_value
        
          SocioeconomicExposure --|> named thing : has_qualitative_value
        
      SocioeconomicExposure : has_quantitative_value
        
          SocioeconomicExposure --|> quantity value : has_quantitative_value
        
      SocioeconomicExposure : id
        
      SocioeconomicExposure : iri
        
      SocioeconomicExposure : name
        
      SocioeconomicExposure : provided_by
        
      SocioeconomicExposure : timepoint
        
      SocioeconomicExposure : type
        
      SocioeconomicExposure : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [Attribute](Attribute.md) [ [OntologyClass](OntologyClass.md)]
            * **SocioeconomicExposure** [ [ExposureEvent](ExposureEvent.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [timepoint](timepoint.md) | 0..1 <br/> [TimeType](TimeType.md) | a point in time | [ExposureEvent](ExposureEvent.md) |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | The human-readable 'attribute name' can be set to a string which reflects its... | [Entity](Entity.md), [Attribute](Attribute.md) |
| [has_attribute_type](has_attribute_type.md) | 1..1 <br/> [OntologyClass](OntologyClass.md) | connects an attribute to a class that describes it | [Attribute](Attribute.md) |
| [has_quantitative_value](has_quantitative_value.md) | 0..* <br/> [QuantityValue](QuantityValue.md) | connects an attribute to a value | [Attribute](Attribute.md) |
| [has_qualitative_value](has_qualitative_value.md) | 0..1 <br/> [NamedThing](NamedThing.md) | connects an attribute to a value | [Attribute](Attribute.md) |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md), [Attribute](Attribute.md) |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md), [OntologyClass](OntologyClass.md) |
| [provided_by](provided_by.md) | 0..* <br/> [String](String.md) | The value in this node property represents the knowledge provider that create... | [NamedThing](NamedThing.md) |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge... | [NamedThing](NamedThing.md) |
| [full_name](full_name.md) | 0..1 <br/> [LabelType](LabelType.md) | a long-form human readable name for a thing | [NamedThing](NamedThing.md) |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | 0..* <br/> [String](String.md) |  | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | 1..* <br/> [SocioeconomicAttribute](SocioeconomicAttribute.md) | connects any entity to an attribute | [Entity](Entity.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:SocioeconomicExposure |
| native | bican:SocioeconomicExposure |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: socioeconomic exposure
description: A socioeconomic exposure is a factor relating to social and financial
  status of an affected individual (e.g. poverty).
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: attribute
mixins:
- exposure event
slot_usage:
  has attribute:
    name: has attribute
    domain_of:
    - entity
    range: socioeconomic attribute
    required: true

```
</details>

### Induced

<details>
```yaml
name: socioeconomic exposure
description: A socioeconomic exposure is a factor relating to social and financial
  status of an affected individual (e.g. poverty).
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: attribute
mixins:
- exposure event
slot_usage:
  has attribute:
    name: has attribute
    domain_of:
    - entity
    range: socioeconomic attribute
    required: true
attributes:
  timepoint:
    name: timepoint
    description: a point in time
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - duration
    rank: 1000
    alias: timepoint
    owner: socioeconomic exposure
    domain_of:
    - geographic location at time
    - exposure event
    - association
    range: time type
  name:
    name: name
    description: The human-readable 'attribute name' can be set to a string which
      reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence
      annotation or it can default to the name associated with the 'has attribute
      type' slot ontology term.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    domain: entity
    slot_uri: rdfs:label
    alias: name
    owner: socioeconomic exposure
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: label type
  has attribute type:
    name: has attribute type
    description: connects an attribute to a class that describes it
    in_subset:
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    narrow_mappings:
    - LOINC:has_modality_type
    - LOINC:has_view_type
    rank: 1000
    domain: attribute
    multivalued: false
    alias: has_attribute_type
    owner: socioeconomic exposure
    domain_of:
    - attribute
    range: ontology class
    required: true
  has quantitative value:
    name: has quantitative value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - qud:quantityValue
    narrow_mappings:
    - SNOMED:has_concentration_strength_numerator_value
    - SNOMED:has_presentation_strength_denominator_value
    - SNOMED:has_presentation_strength_numerator_value
    rank: 1000
    domain: attribute
    multivalued: true
    alias: has_quantitative_value
    owner: socioeconomic exposure
    domain_of:
    - attribute
    - chemical exposure
    range: quantity value
  has qualitative value:
    name: has qualitative value
    description: connects an attribute to a value
    in_subset:
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    domain: attribute
    multivalued: false
    alias: has_qualitative_value
    owner: socioeconomic exposure
    domain_of:
    - attribute
    range: named thing
  iri:
    name: iri
    description: An IRI for an entity. This is determined by the id using expansion
      rules.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - WIKIDATA_PROPERTY:P854
    rank: 1000
    alias: iri
    owner: socioeconomic exposure
    domain_of:
    - attribute
    - entity
    range: iri type
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
    owner: socioeconomic exposure
    domain_of:
    - genome assembly
    - ontology class
    - entity
    range: string
    required: true
  provided by:
    name: provided by
    description: The value in this node property represents the knowledge provider
      that created or assembled the node and all of its attributes.  Used internally
      to represent how a particular node made its way into a knowledge provider or
      graph.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: node property
    domain: named thing
    multivalued: true
    alias: provided_by
    owner: socioeconomic exposure
    domain_of:
    - named thing
    range: string
  xref:
    name: xref
    description: A database cross reference or alternative identifier for a NamedThing
      or edge between two  NamedThings.  This property should point to a database
      record or webpage that supports the existence of the edge, or  gives more detail
      about the edge. This property can be used on a node or edge to provide multiple
      URIs or CURIE cross references.
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - dbxref
    - Dbxref
    - DbXref
    - record_url
    - source_record_urls
    narrow_mappings:
    - gff3:Dbxref
    - gpi:DB_Xrefs
    rank: 1000
    domain: named thing
    multivalued: true
    alias: xref
    owner: socioeconomic exposure
    domain_of:
    - named thing
    - publication
    - retrieval source
    - gene
    - gene product mixin
    range: uriorcurie
  full name:
    name: full name
    description: a long-form human readable name for a thing
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: node property
    domain: named thing
    alias: full_name
    owner: socioeconomic exposure
    domain_of:
    - named thing
    range: label type
  category:
    name: category
    description: "Name of the high level ontology class in which this entity is categorized.\
      \ Corresponds to the label for the biolink entity type class.\n * In a neo4j\
      \ database this MAY correspond to the neo4j label tag.\n * In an RDF database\
      \ it should be a biolink model class URI.\nThis field is multi-valued. It should\
      \ include values for ancestors of the biolink class; for example, a protein\
      \ such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`,\
      \ `biolink:MolecularEntity`, ...\nIn an RDF database, nodes will typically have\
      \ an rdf:type triples. This can be to the most specific biolink class, or potentially\
      \ to a class more specific than something in biolink. For example, a sequence\
      \ feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site,\
      \ which is more specific than anything in biolink. Here we would have categories\
      \ {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}"
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: type
    domain: entity
    multivalued: true
    designates_type: true
    alias: category
    owner: socioeconomic exposure
    domain_of:
    - entity
    is_class_field: true
    range: category type
    required: true
    pattern: ^biolink:[A-Z][A-Za-z]+$
  type:
    name: type
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - AGRKB:soTermId
    - gff3:type
    - gpi:DB_Object_Type
    rank: 1000
    domain: entity
    slot_uri: rdf:type
    multivalued: true
    alias: type
    owner: socioeconomic exposure
    domain_of:
    - entity
    range: string
  description:
    name: description
    description: a human-readable description of an entity
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - definition
    exact_mappings:
    - IAO:0000115
    - skos:definitions
    narrow_mappings:
    - gff3:Description
    rank: 1000
    slot_uri: dct:description
    alias: description
    owner: socioeconomic exposure
    domain_of:
    - genome assembly
    - entity
    range: narrative text
  has attribute:
    name: has attribute
    description: connects any entity to an attribute
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    domain: entity
    multivalued: true
    alias: has_attribute
    owner: socioeconomic exposure
    domain_of:
    - entity
    range: socioeconomic attribute
    required: true

```
</details>