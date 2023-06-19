# Class: OrganismTaxon


_A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies._





URI: [bican:OrganismTaxon](https://identifiers.org/brain-bican/vocab/OrganismTaxon)



```mermaid
 classDiagram
    class OrganismTaxon
      NamedThing <|-- OrganismTaxon
      
      OrganismTaxon : category
        
      OrganismTaxon : description
        
      OrganismTaxon : full_name
        
      OrganismTaxon : has_attribute
        
          OrganismTaxon --|> attribute : has_attribute
        
      OrganismTaxon : id
        
      OrganismTaxon : iri
        
      OrganismTaxon : name
        
      OrganismTaxon : provided_by
        
      OrganismTaxon : type
        
      OrganismTaxon : xref
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * **OrganismTaxon**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
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





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneAnnotation](GeneAnnotation.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [GenomeAnnotation](GenomeAnnotation.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [PredicateMapping](PredicateMapping.md) | [species_context_qualifier](species_context_qualifier.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [StudyPopulation](StudyPopulation.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [ThingWithTaxon](ThingWithTaxon.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [BiologicalEntity](BiologicalEntity.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [RegulatoryRegion](RegulatoryRegion.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [AccessibleDnaRegion](AccessibleDnaRegion.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [TranscriptionFactorBindingSite](TranscriptionFactorBindingSite.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [MolecularActivity](MolecularActivity.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [BiologicalProcess](BiologicalProcess.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Pathway](Pathway.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Behavior](Behavior.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [GeneticInheritance](GeneticInheritance.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [OrganismalEntity](OrganismalEntity.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Bacterium](Bacterium.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Virus](Virus.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [CellularOrganism](CellularOrganism.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Mammal](Mammal.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Human](Human.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Plant](Plant.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Invertebrate](Invertebrate.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Vertebrate](Vertebrate.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Fungus](Fungus.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [LifeStage](LifeStage.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [IndividualOrganism](IndividualOrganism.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Disease](Disease.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [PhenotypicFeature](PhenotypicFeature.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [BehavioralFeature](BehavioralFeature.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [AnatomicalEntity](AnatomicalEntity.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [CellularComponent](CellularComponent.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Cell](Cell.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [CellLine](CellLine.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Gene](Gene.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [MacromolecularComplex](MacromolecularComplex.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [NucleosomeModification](NucleosomeModification.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Genome](Genome.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Exon](Exon.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Transcript](Transcript.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [CodingSequence](CodingSequence.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Polypeptide](Polypeptide.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Protein](Protein.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [ProteinIsoform](ProteinIsoform.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [ProteinDomain](ProteinDomain.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [PosttranslationalModification](PosttranslationalModification.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [ProteinFamily](ProteinFamily.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [RNAProduct](RNAProduct.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [RNAProductIsoform](RNAProductIsoform.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [MicroRNA](MicroRNA.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [SiRNA](SiRNA.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [GeneFamily](GeneFamily.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Genotype](Genotype.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Haplotype](Haplotype.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [SequenceVariant](SequenceVariant.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Snv](Snv.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [ClinicalFinding](ClinicalFinding.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Case](Case.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [Cohort](Cohort.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [PathologicalProcess](PathologicalProcess.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [in_taxon](in_taxon.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject](subject.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object](object.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject](subject.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object](object.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject](subject.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object](object.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject](subject.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object](object.md) | range | [OrganismTaxon](OrganismTaxon.md) |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject](subject.md) | range | [OrganismTaxon](OrganismTaxon.md) |




## Aliases


* taxon
* taxonomic classification



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* NCBITaxon

* MESH

* UMLS








### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:OrganismTaxon |
| native | bican:OrganismTaxon |
| exact | WIKIDATA:Q16521, STY:T001, bioschemas:Taxon |
| narrow | dcid:BiologicalSpecies |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: organism taxon
id_prefixes:
- NCBITaxon
- MESH
- UMLS
description: 'A classification of a set of organisms. Example instances: NCBITaxon:9606
  (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or
  subspecies.'
in_subset:
- model_organism_database
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- taxon
- taxonomic classification
exact_mappings:
- WIKIDATA:Q16521
- STY:T001
- bioschemas:Taxon
narrow_mappings:
- dcid:BiologicalSpecies
is_a: named thing
values_from:
- NCBITaxon
slot_usage:
  has taxonomic rank:
    name: has taxonomic rank
    mappings:
    - WIKIDATA:P105
    multivalued: false
    range: taxonomic rank

```
</details>

### Induced

<details>
```yaml
name: organism taxon
id_prefixes:
- NCBITaxon
- MESH
- UMLS
description: 'A classification of a set of organisms. Example instances: NCBITaxon:9606
  (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or
  subspecies.'
in_subset:
- model_organism_database
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- taxon
- taxonomic classification
exact_mappings:
- WIKIDATA:Q16521
- STY:T001
- bioschemas:Taxon
narrow_mappings:
- dcid:BiologicalSpecies
is_a: named thing
values_from:
- NCBITaxon
slot_usage:
  has taxonomic rank:
    name: has taxonomic rank
    mappings:
    - WIKIDATA:P105
    multivalued: false
    range: taxonomic rank
attributes:
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
    owner: organism taxon
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
    owner: organism taxon
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
    owner: organism taxon
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
    owner: organism taxon
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
    owner: organism taxon
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
    owner: organism taxon
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
    owner: organism taxon
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
    owner: organism taxon
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
    owner: organism taxon
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
    owner: organism taxon
    domain_of:
    - entity
    range: attribute

```
</details>