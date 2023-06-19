# Class: Gene


_A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions._





URI: [bican:Gene](https://identifiers.org/brain-bican/vocab/Gene)



```mermaid
 classDiagram
    class Gene
      GeneOrGeneProduct <|-- Gene
      GenomicEntity <|-- Gene
      ChemicalEntityOrGeneOrGeneProduct <|-- Gene
      PhysicalEssence <|-- Gene
      OntologyClass <|-- Gene
      BiologicalEntity <|-- Gene
      

      Gene <|-- GeneAnnotation
      
      
      Gene : category
        
      Gene : description
        
      Gene : full_name
        
      Gene : has_attribute
        
          Gene --|> attribute : has_attribute
        
      Gene : has_biological_sequence
        
      Gene : id
        
      Gene : in_taxon
        
          Gene --|> organism taxon : in_taxon
        
      Gene : in_taxon_label
        
      Gene : iri
        
      Gene : name
        
      Gene : provided_by
        
      Gene : symbol
        
      Gene : synonym
        
      Gene : type
        
      Gene : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [BiologicalEntity](BiologicalEntity.md) [ [ThingWithTaxon](ThingWithTaxon.md)]
            * **Gene** [ [GeneOrGeneProduct](GeneOrGeneProduct.md) [GenomicEntity](GenomicEntity.md) [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) [PhysicalEssence](PhysicalEssence.md) [OntologyClass](OntologyClass.md)]
                * [GeneAnnotation](GeneAnnotation.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [symbol](symbol.md) | 0..1 <br/> [String](String.md) | Symbol for a particular thing | direct |
| [synonym](synonym.md) | 0..* <br/> [LabelType](LabelType.md) | Alternate human-readable names for a thing | direct |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md) | A database cross reference or alternative identifier for a NamedThing or edge... | direct |
| [has_biological_sequence](has_biological_sequence.md) | 0..1 <br/> [BiologicalSequence](BiologicalSequence.md) | connects a genomic feature to its sequence | [GenomicEntity](GenomicEntity.md) |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md), [OntologyClass](OntologyClass.md) |
| [in_taxon](in_taxon.md) | 0..* <br/> [OrganismTaxon](OrganismTaxon.md) | connects an entity to its taxonomic classification | [ThingWithTaxon](ThingWithTaxon.md) |
| [in_taxon_label](in_taxon_label.md) | 0..1 <br/> [LabelType](LabelType.md) | The human readable scientific name for the taxon of the entity | [ThingWithTaxon](ThingWithTaxon.md) |
| [provided_by](provided_by.md) | 0..* <br/> [String](String.md) | The value in this node property represents the knowledge provider that create... | [NamedThing](NamedThing.md) |
| [full_name](full_name.md) | 0..1 <br/> [LabelType](LabelType.md) | a long-form human readable name for a thing | [NamedThing](NamedThing.md) |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md) | An IRI for an entity | [Entity](Entity.md) |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md) | Name of the high level ontology class in which this entity is categorized | [Entity](Entity.md) |
| [type](type.md) | 0..* <br/> [String](String.md) |  | [Entity](Entity.md) |
| [name](name.md) | 0..1 <br/> [SymbolType](SymbolType.md) | genes are typically designated by a short symbol and a full name | [Entity](Entity.md), [MacromolecularMachineMixin](MacromolecularMachineMixin.md) |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md) | a human-readable description of an entity | [Entity](Entity.md) |
| [has_attribute](has_attribute.md) | 0..* <br/> [Attribute](Attribute.md) | connects any entity to an attribute | [Entity](Entity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ProteinDomain](ProteinDomain.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [ProteinFamily](ProteinFamily.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [GeneGroupingMixin](GeneGroupingMixin.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [GeneFamily](GeneFamily.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [SequenceVariant](SequenceVariant.md) | [has_gene](has_gene.md) | range | [Gene](Gene.md) |
| [Snv](Snv.md) | [has_gene](has_gene.md) | range | [Gene](Gene.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | range | [Gene](Gene.md) |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object](object.md) | range | [Gene](Gene.md) |
| [GeneToGeneFamilyAssociation](GeneToGeneFamilyAssociation.md) | [subject](subject.md) | range | [Gene](Gene.md) |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object](object.md) | range | [Gene](Gene.md) |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object](object.md) | range | [Gene](Gene.md) |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject](subject.md) | range | [Gene](Gene.md) |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object](object.md) | range | [Gene](Gene.md) |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject](subject.md) | range | [Gene](Gene.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* NCBIGene

* ENSEMBL

* HGNC

* MGI

* ZFIN

* dictyBase

* WB

* WormBase

* FB

* RGD

* SGD

* PomBase

* OMIM

* KEGG.GENES

* UMLS

* Xenbase

* AspGD

* PHARMGKB.GENE








### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:Gene |
| native | bican:Gene |
| exact | SO:0000704, SIO:010035, WIKIDATA:Q7187, dcid:Gene |
| narrow | bioschemas:gene |
| broad | NCIT:C45822 |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene
id_prefixes:
- NCBIGene
- ENSEMBL
- HGNC
- MGI
- ZFIN
- dictyBase
- WB
- WormBase
- FB
- RGD
- SGD
- PomBase
- OMIM
- KEGG.GENES
- UMLS
- Xenbase
- AspGD
- PHARMGKB.GENE
description: A region (or regions) that includes all of the sequence elements necessary
  to encode a functional transcript. A gene locus may include regulatory regions,
  transcribed regions and/or other functional sequence regions.
in_subset:
- translator_minimal
- model_organism_database
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SO:0000704
- SIO:010035
- WIKIDATA:Q7187
- dcid:Gene
narrow_mappings:
- bioschemas:gene
broad_mappings:
- NCIT:C45822
is_a: biological entity
mixins:
- gene or gene product
- genomic entity
- chemical entity or gene or gene product
- physical essence
- ontology class
slots:
- symbol
- synonym
- xref

```
</details>

### Induced

<details>
```yaml
name: gene
id_prefixes:
- NCBIGene
- ENSEMBL
- HGNC
- MGI
- ZFIN
- dictyBase
- WB
- WormBase
- FB
- RGD
- SGD
- PomBase
- OMIM
- KEGG.GENES
- UMLS
- Xenbase
- AspGD
- PHARMGKB.GENE
description: A region (or regions) that includes all of the sequence elements necessary
  to encode a functional transcript. A gene locus may include regulatory regions,
  transcribed regions and/or other functional sequence regions.
in_subset:
- translator_minimal
- model_organism_database
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- SO:0000704
- SIO:010035
- WIKIDATA:Q7187
- dcid:Gene
narrow_mappings:
- bioschemas:gene
broad_mappings:
- NCIT:C45822
is_a: biological entity
mixins:
- gene or gene product
- genomic entity
- chemical entity or gene or gene product
- physical essence
- ontology class
attributes:
  symbol:
    name: symbol
    description: Symbol for a particular thing
    from_schema: https://identifiers.org/brain-bican/kb-model
    exact_mappings:
    - AGRKB:symbol
    - gpi:DB_Object_Symbol
    rank: 1000
    is_a: node property
    domain: named thing
    alias: symbol
    owner: gene
    domain_of:
    - gene
    range: string
  synonym:
    name: synonym
    description: Alternate human-readable names for a thing
    in_subset:
    - translator_minimal
    from_schema: https://identifiers.org/brain-bican/kb-model
    aliases:
    - alias
    narrow_mappings:
    - skos:altLabel
    - gff3:Alias
    - AGRKB:synonyms
    - gpi:DB_Object_Synonyms
    - HANCESTRO:0330
    - IAO:0000136
    - RXNORM:has_tradename
    rank: 1000
    is_a: node property
    domain: named thing
    multivalued: true
    alias: synonym
    owner: gene
    domain_of:
    - gene
    - gene product mixin
    range: label type
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
    owner: gene
    domain_of:
    - named thing
    - publication
    - retrieval source
    - gene
    - gene product mixin
    range: uriorcurie
  has biological sequence:
    name: has biological sequence
    description: connects a genomic feature to its sequence
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: node property
    domain: named thing
    alias: has_biological_sequence
    owner: gene
    domain_of:
    - genomic entity
    - epigenomic entity
    range: biological sequence
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
    owner: gene
    domain_of:
    - genome assembly
    - ontology class
    - entity
    range: string
    required: true
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
    owner: gene
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
    owner: gene
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
    owner: gene
    domain_of:
    - named thing
    range: string
  full name:
    name: full name
    description: a long-form human readable name for a thing
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: node property
    domain: named thing
    alias: full_name
    owner: gene
    domain_of:
    - named thing
    range: label type
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
    owner: gene
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
    owner: gene
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
    owner: gene
    domain_of:
    - entity
    range: string
  name:
    name: name
    description: genes are typically designated by a short symbol and a full name.
      We map the symbol to the default display name and use an additional slot for
      full name
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    domain: entity
    slot_uri: rdfs:label
    alias: name
    owner: gene
    domain_of:
    - attribute
    - entity
    - macromolecular machine mixin
    range: symbol type
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
    owner: gene
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
    owner: gene
    domain_of:
    - entity
    range: attribute

```
</details>