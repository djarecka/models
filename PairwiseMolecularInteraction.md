# Class: PairwiseMolecularInteraction


_An interaction at the molecular level between two physical entities_





URI: [bican:PairwiseMolecularInteraction](https://identifiers.org/brain-bican/vocab/PairwiseMolecularInteraction)



```mermaid
 classDiagram
    class PairwiseMolecularInteraction
      PairwiseGeneToGeneInteraction <|-- PairwiseMolecularInteraction
      
      PairwiseMolecularInteraction : aggregator_knowledge_source
        
      PairwiseMolecularInteraction : category
        
      PairwiseMolecularInteraction : description
        
      PairwiseMolecularInteraction : has_attribute
        
          PairwiseMolecularInteraction --|> attribute : has_attribute
        
      PairwiseMolecularInteraction : has_evidence
        
          PairwiseMolecularInteraction --|> evidence type : has_evidence
        
      PairwiseMolecularInteraction : id
        
      PairwiseMolecularInteraction : interacting_molecules_category
        
          PairwiseMolecularInteraction --|> ontology class : interacting_molecules_category
        
      PairwiseMolecularInteraction : iri
        
      PairwiseMolecularInteraction : knowledge_source
        
      PairwiseMolecularInteraction : name
        
      PairwiseMolecularInteraction : negated
        
      PairwiseMolecularInteraction : object
        
          PairwiseMolecularInteraction --|> molecular entity : object
        
      PairwiseMolecularInteraction : object_category
        
          PairwiseMolecularInteraction --|> ontology class : object_category
        
      PairwiseMolecularInteraction : object_category_closure
        
          PairwiseMolecularInteraction --|> ontology class : object_category_closure
        
      PairwiseMolecularInteraction : object_closure
        
      PairwiseMolecularInteraction : object_label_closure
        
      PairwiseMolecularInteraction : object_namespace
        
      PairwiseMolecularInteraction : original_object
        
      PairwiseMolecularInteraction : original_predicate
        
      PairwiseMolecularInteraction : original_subject
        
      PairwiseMolecularInteraction : predicate
        
      PairwiseMolecularInteraction : primary_knowledge_source
        
      PairwiseMolecularInteraction : publications
        
          PairwiseMolecularInteraction --|> publication : publications
        
      PairwiseMolecularInteraction : qualifiers
        
          PairwiseMolecularInteraction --|> ontology class : qualifiers
        
      PairwiseMolecularInteraction : retrieval_source_ids
        
          PairwiseMolecularInteraction --|> retrieval source : retrieval_source_ids
        
      PairwiseMolecularInteraction : subject
        
          PairwiseMolecularInteraction --|> molecular entity : subject
        
      PairwiseMolecularInteraction : subject_category
        
          PairwiseMolecularInteraction --|> ontology class : subject_category
        
      PairwiseMolecularInteraction : subject_category_closure
        
          PairwiseMolecularInteraction --|> ontology class : subject_category_closure
        
      PairwiseMolecularInteraction : subject_closure
        
      PairwiseMolecularInteraction : subject_label_closure
        
      PairwiseMolecularInteraction : subject_namespace
        
      PairwiseMolecularInteraction : timepoint
        
      PairwiseMolecularInteraction : type
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [Association](Association.md)
        * [GeneToGeneAssociation](GeneToGeneAssociation.md)
            * [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md)
                * **PairwiseMolecularInteraction**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [interacting_molecules_category](interacting_molecules_category.md) | 0..1 <br/> [OntologyClass](OntologyClass.md) |  | direct |
| [subject](subject.md) | 1..1 <br/> [MolecularEntity](MolecularEntity.md) | the subject gene in the association | [Association](Association.md) |
| [predicate](predicate.md) | 1..1 <br/> [PredicateType](PredicateType.md) | interaction relationship type | [Association](Association.md) |
| [object](object.md) | 1..1 <br/> [MolecularEntity](MolecularEntity.md) | the object gene in the association | [Association](Association.md) |
| [negated](negated.md) | 0..1 <br/> [Boolean](Boolean.md) | if set to true, then the association is negated i | [Association](Association.md) |
| [qualifiers](qualifiers.md) | 0..* <br/> [OntologyClass](OntologyClass.md) | connects an association to qualifiers that modify or qualify the meaning of t... | [Association](Association.md) |
| [publications](publications.md) | 0..* <br/> [Publication](Publication.md) | One or more publications that report the statement expressed in an  Associati... | [Association](Association.md) |
| [has_evidence](has_evidence.md) | 0..* <br/> [EvidenceType](EvidenceType.md) | connects an association to an instance of supporting evidence | [Association](Association.md) |
| [knowledge_source](knowledge_source.md) | 0..1 <br/> [String](String.md) | An Information Resource from which the knowledge expressed in an Association ... | [Association](Association.md) |
| [primary_knowledge_source](primary_knowledge_source.md) | 0..1 <br/> [String](String.md) | The most upstream source of the knowledge expressed in an Association that an... | [Association](Association.md) |
| [aggregator_knowledge_source](aggregator_knowledge_source.md) | 0..* <br/> [String](String.md) | An intermediate aggregator resource from which knowledge expressed in an Asso... | [Association](Association.md) |
| [timepoint](timepoint.md) | 0..1 <br/> [TimeType](TimeType.md) | a point in time | [Association](Association.md) |
| [original_subject](original_subject.md) | 0..1 <br/> [String](String.md) | used to hold the original subject of a relation (or predicate) that an extern... | [Association](Association.md) |
| [original_predicate](original_predicate.md) | 0..1 <br/> [Uriorcurie](Uriorcurie.md) | used to hold the original relation/predicate that an external knowledge sourc... | [Association](Association.md) |
| [original_object](original_object.md) | 0..1 <br/> [String](String.md) | used to hold the original object of a relation (or predicate) that an externa... | [Association](Association.md) |
| [subject_category](subject_category.md) | 0..1 <br/> [OntologyClass](OntologyClass.md) | Used to hold the biolink class/category of an association | [Association](Association.md) |
| [object_category](object_category.md) | 0..1 <br/> [OntologyClass](OntologyClass.md) | Used to hold the biolink class/category of an association | [Association](Association.md) |
| [subject_closure](subject_closure.md) | 0..* <br/> [String](String.md) | Used to hold the subject closure of an association | [Association](Association.md) |
| [object_closure](object_closure.md) | 0..* <br/> [String](String.md) | Used to hold the object closure of an association | [Association](Association.md) |
| [subject_category_closure](subject_category_closure.md) | 0..* <br/> [OntologyClass](OntologyClass.md) | Used to hold the subject category closure of an association | [Association](Association.md) |
| [object_category_closure](object_category_closure.md) | 0..* <br/> [OntologyClass](OntologyClass.md) | Used to hold the object category closure of an association | [Association](Association.md) |
| [subject_namespace](subject_namespace.md) | 0..1 <br/> [String](String.md) | Used to hold the subject namespace of an association | [Association](Association.md) |
| [object_namespace](object_namespace.md) | 0..1 <br/> [String](String.md) | Used to hold the object namespace of an association | [Association](Association.md) |
| [subject_label_closure](subject_label_closure.md) | 0..* <br/> [String](String.md) | Used to hold the subject label closure of an association | [Association](Association.md) |
| [object_label_closure](object_label_closure.md) | 0..* <br/> [String](String.md) | Used to hold the object label closure of an association | [Association](Association.md) |
| [retrieval_source_ids](retrieval_source_ids.md) | 0..* <br/> [RetrievalSource](RetrievalSource.md) | A list of retrieval sources that served as a source of knowledge expressed in... | [Association](Association.md) |
| [id](id.md) | 1..1 <br/> [String](String.md) | identifier for the interaction | [Entity](Entity.md) |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md) |
| [category](category.md) | 0..* <br/> [CategoryType](CategoryType.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | 0..* <br/> [String](String.md) | rdf:type of biolink:Association should be fixed at rdf:Statement | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | 0..* <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:PairwiseMolecularInteraction |
| native | bican:PairwiseMolecularInteraction |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: pairwise molecular interaction
description: An interaction at the molecular level between two physical entities
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: pairwise gene to gene interaction
slots:
- interacting molecules category
slot_usage:
  subject:
    name: subject
    domain_of:
    - association
    range: molecular entity
  id:
    name: id
    description: identifier for the interaction. This may come from an interaction
      database such as IMEX.
    examples:
    - value: WB:WBInteraction000538741
    values_from:
    - IMEX
    - BioGRID
    domain_of:
    - genome assembly
    - ontology class
    - entity
  predicate:
    name: predicate
    description: interaction relationship type
    examples:
    - value: RO:0002447
      description: the subject molecular phosphorylates the object molecule
    domain_of:
    - predicate mapping
    - association
    subproperty_of: interacts with
  object:
    name: object
    domain_of:
    - association
    range: molecular entity
defining_slots:
- subject
- predicate
- object

```
</details>

### Induced

<details>
```yaml
name: pairwise molecular interaction
description: An interaction at the molecular level between two physical entities
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: pairwise gene to gene interaction
slot_usage:
  subject:
    name: subject
    domain_of:
    - association
    range: molecular entity
  id:
    name: id
    description: identifier for the interaction. This may come from an interaction
      database such as IMEX.
    examples:
    - value: WB:WBInteraction000538741
    values_from:
    - IMEX
    - BioGRID
    domain_of:
    - genome assembly
    - ontology class
    - entity
  predicate:
    name: predicate
    description: interaction relationship type
    examples:
    - value: RO:0002447
      description: the subject molecular phosphorylates the object molecule
    domain_of:
    - predicate mapping
    - association
    subproperty_of: interacts with
  object:
    name: object
    domain_of:
    - association
    range: molecular entity
attributes:
  interacting molecules category:
    name: interacting molecules category
    examples:
    - value: MI:1048
      description: smallmolecule-protein
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - MI:1046
    rank: 1000
    is_a: association slot
    values_from:
    - MI
    domain: association
    alias: interacting_molecules_category
    owner: pairwise molecular interaction
    domain_of:
    - pairwise molecular interaction
    range: ontology class
  subject:
    name: subject
    description: the subject gene in the association. If the relation is symmetric,
      subject vs object is arbitrary. We allow a gene product to stand as a proxy
      for the gene or vice versa.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    alias: subject
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: molecular entity
    required: true
  predicate:
    name: predicate
    description: interaction relationship type
    examples:
    - value: RO:0002447
      description: the subject molecular phosphorylates the object molecule
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:predicate
    alias: predicate
    owner: pairwise molecular interaction
    domain_of:
    - predicate mapping
    - association
    subproperty_of: interacts with
    symmetric: true
    range: predicate type
    required: true
  object:
    name: object
    description: the object gene in the association. If the relation is symmetric,
      subject vs object is arbitrary. We allow a gene product to stand as a proxy
      for the gene or vice versa.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:object
    alias: object
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: molecular entity
    required: true
  negated:
    name: negated
    description: if set to true, then the association is negated i.e. is not true
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    alias: negated
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: boolean
  qualifiers:
    name: qualifiers
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation qualifier
    description: connects an association to qualifiers that modify or qualify the
      meaning of that association
    deprecated: 'True'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: qualifiers
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: ontology class
  publications:
    name: publications
    description: One or more publications that report the statement expressed in an  Association,
      or provide information used as evidence supporting this statement.
    comments:
    - 'The notion of a ‘Publication’ is considered broadly to include any  document
      made available for public consumption. It covers journal issues,  individual
      articles, and books - and also things like article pre-prints,  white papers,
      patents, drug labels, web pages, protocol documents, etc. '
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - supporting publications
    - supporting documents
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: publications
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: publication
  has evidence:
    name: has evidence
    description: connects an association to an instance of supporting evidence
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - RO:0002558
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: has_evidence
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: evidence type
  knowledge source:
    name: knowledge source
    description: An Information Resource from which the knowledge expressed in an
      Association was retrieved, directly or indirectly. This can be any resource
      through which the knowledge passed on its way to its currently serialized form.
      In practice, implementers should use one of the more specific subtypes of this
      generic property.
    from_schema: https://identifiers.org/brain-bican/kb-model
    close_mappings:
    - pav:providedBy
    rank: 1000
    is_a: association slot
    domain: association
    alias: knowledge_source
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  primary knowledge source:
    name: primary knowledge source
    description: The most upstream source of the knowledge expressed in an Association
      that an implementer can identify.  Performing a rigorous analysis of upstream
      data providers is expected; every effort is made to catalog the most upstream
      source of data in this property.  Only one data source should be declared primary
      in any association.  "aggregator knowledge source" can be used to capture non-primary
      sources.
    notes:
    - 'For example: a single ChemicalToGene Edge originally curated by ClinicalTrials.org,
      is aggregated by ChEMBL, then  incorporated into the MolePro KP, then sent via
      TRAPI message to the ARAGORN ARA, and finally sent to  the NCATS ARS. The retrieval
      path for this Edge is as follows:  ARS--retrieved_from-->  ARAGORN  --retrieved_from-->   MolePro  --retrieved_from-->
      ChEMBL --retrieved_from-->  ClinicalTrials.gov The "primary knowledge source"
      for this edge is "infores:clinical-trials-gov".  "infores:chembl" and "infores:molecular_data_provider"
      are listed in the "aggregator knowledge source" property.'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: knowledge source
    domain: association
    multivalued: false
    alias: primary_knowledge_source
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  aggregator knowledge source:
    name: aggregator knowledge source
    description: An intermediate aggregator resource from which knowledge expressed
      in an Association was retrieved downstream of the original source, on its path
      to its current serialized form.
    notes:
    - 'For example, in this Feature Variable Association Edge generated by the Exposure
      Agent’s ICEES KP,  through statistical analysis of clinical and environmental
      data supplied by the UNC Clinical Data Warehouse,  the Edge is passed to the
      Ranking Agent’s ARAGORN ARA,  and then on to the ARS. The retrieval path for
      this Edge is as follows: ARS--retrieved_from-->  ARAGORN  --retrieved_from-->   ICEES
      --supporting_data_from-->  UNC Data Warehouse This example illustrates how to
      represent the source provenance of KP-generated knowledge, including the source
      of  data from which the knowledge was derived.    The "primary knowledge source"
      for this edge is "infores:icees-asthma". A "supporting data source" for this
      KP- generated knowledge is "infores:unc-cdw-health."  The "aggregator knowledge
      source" for this data is "infores:aragorn-ara"'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: knowledge source
    domain: association
    multivalued: true
    alias: aggregator_knowledge_source
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  timepoint:
    name: timepoint
    description: a point in time
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - duration
    rank: 1000
    alias: timepoint
    owner: pairwise molecular interaction
    domain_of:
    - geographic location at time
    - exposure event
    - association
    range: time type
  original subject:
    name: original subject
    description: used to hold the original subject of a relation (or predicate) that
      an external knowledge source uses before transformation to match the biolink-model
      specification.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    alias: original_subject
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  original predicate:
    name: original predicate
    id_prefixes:
    - RO
    - BSPO
    - SIO
    description: used to hold the original relation/predicate that an external knowledge
      source uses before transformation to match the biolink-model specification.
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - original relation
    - relation
    rank: 1000
    is_a: association slot
    domain: association
    alias: original_predicate
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: uriorcurie
  original object:
    name: original object
    description: used to hold the original object of a relation (or predicate) that
      an external knowledge source uses before transformation to match the biolink-model
      specification.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    alias: original_object
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  subject category:
    name: subject category
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the biolink class/category of an association. This is
      a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: biolink:Gene
      description: The subject category of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'biolink:Gene'.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: false
    alias: subject_category
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: ontology class
  object category:
    name: object category
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the biolink class/category of an association. This is
      a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: biolink:Disease
      description: The object category of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'biolink:Disease'.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: false
    alias: object_category
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: ontology class
  subject closure:
    name: subject closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the subject closure of an association. This is a denormalized  field
      used primarily in the SQL serialization of a knowledge graph via KGX.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: subject_closure
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  object closure:
    name: object closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the object closure of an association. This is a denormalized  field
      used primarily in the SQL serialization of a knowledge graph via KGX.
    examples:
    - value: '[''MONDO:0000167'', ''MONDO:0005395'']'
      description: 'The object closure of the association between the gene ''BRCA1''
        and the disease ''breast cancer'' is the set of all diseases that are ancestors
        of ''breast cancer'' in the MONDO ontology.  Note: typically the "subclass
        of" and "part of"  relations are used to construct the closure, but other
        relations may be used as well.'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: object_closure
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  subject category closure:
    name: subject category closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the subject category closure of an association. This
      is a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''biolink:Gene", "biolink:NamedThing'']'
      description: 'The subject category closure of the association between the gene
        ''BRCA1'' and the disease ''breast cancer'' is the set of all biolink classes
        that are ancestors of ''biolink:Gene'' in the biolink model.  Note: typically
        the "subclass of" and "part of"  relations are used to construct the closure,
        but other relations may be used as well.'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: subject_category_closure
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: ontology class
  object category closure:
    name: object category closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the object category closure of an association. This
      is a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''biolink:Disease", "biolink:NamedThing'']'
      description: 'The object category closure of the association between the gene
        ''BRCA1'' and the disease ''breast cancer'' is the set of all biolink classes
        that are ancestors of ''biolink:Disease'' in the biolink model.  Note: typically
        the "subclass of" and "part of"  relations are used to construct the closure,
        but other relations may be used as well.'
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: object_category_closure
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: ontology class
  subject namespace:
    name: subject namespace
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the subject namespace of an association. This is a denormalized  field
      used primarily in the SQL serialization of a knowledge graph via KGX.
    examples:
    - value: NCBIGene
      description: The subject namespace of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'NCBIGene'.
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - subject prefix
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: false
    alias: subject_namespace
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  object namespace:
    name: object namespace
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the object namespace of an association. This is a denormalized  field
      used primarily in the SQL serialization of a knowledge graph via KGX.
    examples:
    - value: MONDO
      description: The object namespace of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is 'MONDO'.
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - object prefix
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: false
    alias: object_namespace
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  subject label closure:
    name: subject label closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the subject label closure of an association. This is
      a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''BRACA1'']'
      description: The subject label closure of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is the set of all labels that are ancestors
        of 'BRCA1' in the biolink model.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: subject_label_closure
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  object label closure:
    name: object label closure
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: Used to hold the object label closure of an association. This is
      a denormalized  field used primarily in the SQL serialization of a knowledge
      graph via KGX.
    examples:
    - value: '[''breast cancer'', ''cancer'']'
      description: The object label closure of the association between the gene 'BRCA1'
        and the disease 'breast cancer' is the set of all labels that are ancestors
        of 'breast cancer' in the biolink model.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    multivalued: true
    alias: object_label_closure
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: string
  retrieval source ids:
    name: retrieval source ids
    description: A list of retrieval sources that served as a source of knowledge
      expressed in an Edge, or a source of data used to generate this knowledge.
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    multivalued: true
    alias: retrieval_source_ids
    owner: pairwise molecular interaction
    domain_of:
    - association
    range: retrieval source
  id:
    name: id
    description: identifier for the interaction. This may come from an interaction
      database such as IMEX.
    examples:
    - value: WB:WBInteraction000538741
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    values_from:
    - IMEX
    - BioGRID
    domain: entity
    identifier: true
    alias: id
    owner: pairwise molecular interaction
    domain_of:
    - genome assembly
    - ontology class
    - entity
    range: string
    required: true
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
    owner: pairwise molecular interaction
    domain_of:
    - attribute
    - entity
    range: iri type
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
    owner: pairwise molecular interaction
    domain_of:
    - entity
    is_class_field: true
    range: category type
    required: false
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    domain: entity
    slot_uri: rdf:type
    multivalued: true
    alias: type
    owner: pairwise molecular interaction
    domain_of:
    - entity
    range: string
  name:
    name: name
    description: A human-readable name for an attribute or entity.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    rank: 1000
    domain: entity
    slot_uri: rdfs:label
    alias: name
    owner: pairwise molecular interaction
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: label type
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
    owner: pairwise molecular interaction
    domain_of:
    - genome assembly
    - entity
    range: narrative text
  has attribute:
    name: has attribute
    description: connects any entity to an attribute
    in_subset:
    - samples
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - SIO:000008
    close_mappings:
    - OBI:0001927
    narrow_mappings:
    - OBAN:association_has_subject_property
    - OBAN:association_has_object_property
    - CPT:has_possibly_included_panel_element
    - DRUGBANK:category
    - EFO:is_executed_in
    - HANCESTRO:0301
    - LOINC:has_action_guidance
    - LOINC:has_adjustment
    - LOINC:has_aggregation_view
    - LOINC:has_approach_guidance
    - LOINC:has_divisor
    - LOINC:has_exam
    - LOINC:has_method
    - LOINC:has_modality_subtype
    - LOINC:has_object_guidance
    - LOINC:has_scale
    - LOINC:has_suffix
    - LOINC:has_time_aspect
    - LOINC:has_time_modifier
    - LOINC:has_timing_of
    - NCIT:R88
    - NCIT:eo_disease_has_property_or_attribute
    - NCIT:has_data_element
    - NCIT:has_pharmaceutical_administration_method
    - NCIT:has_pharmaceutical_basic_dose_form
    - NCIT:has_pharmaceutical_intended_site
    - NCIT:has_pharmaceutical_release_characteristics
    - NCIT:has_pharmaceutical_state_of_matter
    - NCIT:has_pharmaceutical_transformation
    - NCIT:is_qualified_by
    - NCIT:qualifier_applies_to
    - NCIT:role_has_domain
    - NCIT:role_has_range
    - INO:0000154
    - HANCESTRO:0308
    - OMIM:has_inheritance_type
    - orphanet:C016
    - orphanet:C017
    - RO:0000053
    - RO:0000086
    - RO:0000087
    - SNOMED:has_access
    - SNOMED:has_clinical_course
    - SNOMED:has_count_of_base_of_active_ingredient
    - SNOMED:has_dose_form_administration_method
    - SNOMED:has_dose_form_release_characteristic
    - SNOMED:has_dose_form_transformation
    - SNOMED:has_finding_context
    - SNOMED:has_finding_informer
    - SNOMED:has_inherent_attribute
    - SNOMED:has_intent
    - SNOMED:has_interpretation
    - SNOMED:has_laterality
    - SNOMED:has_measurement_method
    - SNOMED:has_method
    - SNOMED:has_priority
    - SNOMED:has_procedure_context
    - SNOMED:has_process_duration
    - SNOMED:has_property
    - SNOMED:has_revision_status
    - SNOMED:has_scale_type
    - SNOMED:has_severity
    - SNOMED:has_specimen
    - SNOMED:has_state_of_matter
    - SNOMED:has_subject_relationship_context
    - SNOMED:has_surgical_approach
    - SNOMED:has_technique
    - SNOMED:has_temporal_context
    - SNOMED:has_time_aspect
    - SNOMED:has_units
    - UMLS:has_structural_class
    - UMLS:has_supported_concept_property
    - UMLS:has_supported_concept_relationship
    - UMLS:may_be_qualified_by
    rank: 1000
    domain: entity
    multivalued: true
    alias: has_attribute
    owner: pairwise molecular interaction
    domain_of:
    - entity
    range: attribute
defining_slots:
- subject
- predicate
- object

```
</details>