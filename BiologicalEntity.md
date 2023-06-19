# Class: BiologicalEntity


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [bican:BiologicalEntity](https://identifiers.org/brain-bican/vocab/BiologicalEntity)



```mermaid
 classDiagram
    class BiologicalEntity
      ThingWithTaxon <|-- BiologicalEntity
      NamedThing <|-- BiologicalEntity
      

      BiologicalEntity <|-- RegulatoryRegion
      BiologicalEntity <|-- BiologicalProcessOrActivity
      BiologicalEntity <|-- GeneticInheritance
      BiologicalEntity <|-- OrganismalEntity
      BiologicalEntity <|-- DiseaseOrPhenotypicFeature
      BiologicalEntity <|-- Gene
      BiologicalEntity <|-- MacromolecularComplex
      BiologicalEntity <|-- NucleosomeModification
      BiologicalEntity <|-- Genome
      BiologicalEntity <|-- Polypeptide
      BiologicalEntity <|-- ProteinDomain
      BiologicalEntity <|-- PosttranslationalModification
      BiologicalEntity <|-- ProteinFamily
      BiologicalEntity <|-- NucleicAcidSequenceMotif
      BiologicalEntity <|-- GeneFamily
      BiologicalEntity <|-- Genotype
      BiologicalEntity <|-- Haplotype
      BiologicalEntity <|-- SequenceVariant
      BiologicalEntity <|-- ReagentTargetedGene
      
      
      BiologicalEntity : category
        
      BiologicalEntity : description
        
      BiologicalEntity : full_name
        
      BiologicalEntity : has_attribute
        
          BiologicalEntity --|> attribute : has_attribute
        
      BiologicalEntity : id
        
      BiologicalEntity : in_taxon
        
          BiologicalEntity --|> organism taxon : in_taxon
        
      BiologicalEntity : in_taxon_label
        
      BiologicalEntity : iri
        
      BiologicalEntity : name
        
      BiologicalEntity : provided_by
        
      BiologicalEntity : type
        
      BiologicalEntity : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * **BiologicalEntity** [ [ThingWithTaxon](ThingWithTaxon.md)]
            * [RegulatoryRegion](RegulatoryRegion.md) [ [GenomicEntity](GenomicEntity.md) [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) [PhysicalEssence](PhysicalEssence.md) [OntologyClass](OntologyClass.md)]
            * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) [ [Occurrent](Occurrent.md) [OntologyClass](OntologyClass.md)]
            * [GeneticInheritance](GeneticInheritance.md)
            * [OrganismalEntity](OrganismalEntity.md) [ [SubjectOfInvestigation](SubjectOfInvestigation.md)]
            * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
            * [Gene](Gene.md) [ [GeneOrGeneProduct](GeneOrGeneProduct.md) [GenomicEntity](GenomicEntity.md) [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) [PhysicalEssence](PhysicalEssence.md) [OntologyClass](OntologyClass.md)]
            * [MacromolecularComplex](MacromolecularComplex.md) [ [MacromolecularMachineMixin](MacromolecularMachineMixin.md)]
            * [NucleosomeModification](NucleosomeModification.md) [ [GeneProductIsoformMixin](GeneProductIsoformMixin.md) [GenomicEntity](GenomicEntity.md) [EpigenomicEntity](EpigenomicEntity.md)]
            * [Genome](Genome.md) [ [GenomicEntity](GenomicEntity.md) [PhysicalEssence](PhysicalEssence.md) [OntologyClass](OntologyClass.md)]
            * [Polypeptide](Polypeptide.md) [ [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) [ChemicalEntityOrProteinOrPolypeptide](ChemicalEntityOrProteinOrPolypeptide.md)]
            * [ProteinDomain](ProteinDomain.md) [ [GeneGroupingMixin](GeneGroupingMixin.md) [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)]
            * [PosttranslationalModification](PosttranslationalModification.md) [ [GeneProductIsoformMixin](GeneProductIsoformMixin.md)]
            * [ProteinFamily](ProteinFamily.md) [ [GeneGroupingMixin](GeneGroupingMixin.md) [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)]
            * [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md)
            * [GeneFamily](GeneFamily.md) [ [GeneGroupingMixin](GeneGroupingMixin.md) [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)]
            * [Genotype](Genotype.md) [ [PhysicalEssence](PhysicalEssence.md) [GenomicEntity](GenomicEntity.md) [OntologyClass](OntologyClass.md)]
            * [Haplotype](Haplotype.md) [ [GenomicEntity](GenomicEntity.md) [PhysicalEssence](PhysicalEssence.md) [OntologyClass](OntologyClass.md)]
            * [SequenceVariant](SequenceVariant.md) [ [GenomicEntity](GenomicEntity.md) [PhysicalEssence](PhysicalEssence.md) [OntologyClass](OntologyClass.md)]
            * [ReagentTargetedGene](ReagentTargetedGene.md) [ [GenomicEntity](GenomicEntity.md) [PhysicalEssence](PhysicalEssence.md) [OntologyClass](OntologyClass.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [in_taxon](in_taxon.md) | 0..* <br/> [OrganismTaxon](OrganismTaxon.md) | connects an entity to its taxonomic classification | [ThingWithTaxon](ThingWithTaxon.md) |
| [in_taxon_label](in_taxon_label.md) | 0..1 <br/> [LabelType](LabelType.md) | The human readable scientific name for the taxon of the entity | [ThingWithTaxon](ThingWithTaxon.md) |
| [provided_by](provided_by.md) | 0..* <br/> [String](String.md) | The value in this node property represents the knowledge provider that create... | [NamedThing](NamedThing.md) |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge... | [NamedThing](NamedThing.md) |
| [full_name](full_name.md) | 0..1 <br/> [LabelType](LabelType.md) | a long-form human readable name for a thing | [NamedThing](NamedThing.md) |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md) |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md) |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | 0..* <br/> [String](String.md) |  | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md) | A human-readable name for an attribute or entity | [Entity](Entity.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | 0..* <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |







## Aliases


* bioentity



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:BiologicalEntity |
| native | bican:BiologicalEntity |
| narrow | WIKIDATA:Q28845870, STY:T050, SIO:010046, STY:T129 |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: biological entity
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- bioentity
narrow_mappings:
- WIKIDATA:Q28845870
- STY:T050
- SIO:010046
- STY:T129
is_a: named thing
abstract: true
mixins:
- thing with taxon

```
</details>

### Induced

<details>
```yaml
name: biological entity
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- bioentity
narrow_mappings:
- WIKIDATA:Q28845870
- STY:T050
- SIO:010046
- STY:T129
is_a: named thing
abstract: true
mixins:
- thing with taxon
attributes:
  in taxon:
    name: in taxon
    annotations:
      canonical_predicate:
        tag: canonical_predicate
        value: 'True'
    description: connects an entity to its taxonomic classification. Only certain
      kinds of entities can be taxonomically classified; see 'thing with taxon'
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - instance of
    - is organism source of gene product
    - organism has gene
    - gene found in organism
    - gene product has organism source
    exact_mappings:
    - RO:0002162
    - WIKIDATA_PROPERTY:P703
    narrow_mappings:
    - RO:0002160
    rank: 1000
    is_a: related to at instance level
    domain: thing with taxon
    multivalued: true
    inherited: true
    alias: in_taxon
    owner: biological entity
    domain_of:
    - thing with taxon
    range: organism taxon
  in taxon label:
    name: in taxon label
    annotations:
      denormalized:
        tag: denormalized
        value: 'True'
    description: The human readable scientific name for the taxon of the entity.
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - WIKIDATA_PROPERTY:P225
    rank: 1000
    is_a: node property
    domain: thing with taxon
    slot_uri: rdfs:label
    alias: in_taxon_label
    owner: biological entity
    domain_of:
    - thing with taxon
    range: label type
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
    owner: biological entity
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
    owner: biological entity
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
    owner: biological entity
    domain_of:
    - named thing
    range: label type
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
    owner: biological entity
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
    owner: biological entity
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
    owner: biological entity
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
    owner: biological entity
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
    owner: biological entity
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
    owner: biological entity
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
    owner: biological entity
    domain_of:
    - entity
    range: attribute

```
</details>