# Class: ChemicalAffectsGeneAssociation


_Describes an effect that a chemical has on a gene or gene product (e.g. an impact of on its abundance, activity, localization, processing, expression, etc.)_





URI: [bican:ChemicalAffectsGeneAssociation](https://identifiers.org/brain-bican/vocab/ChemicalAffectsGeneAssociation)



```mermaid
 classDiagram
    class ChemicalAffectsGeneAssociation
      Association <|-- ChemicalAffectsGeneAssociation
      
      ChemicalAffectsGeneAssociation : aggregator_knowledge_source
        
      ChemicalAffectsGeneAssociation : anatomical_context_qualifier
        
          ChemicalAffectsGeneAssociation --|> anatomical entity : anatomical_context_qualifier
        
      ChemicalAffectsGeneAssociation : category
        
      ChemicalAffectsGeneAssociation : causal_mechanism_qualifier
        
          ChemicalAffectsGeneAssociation --|> CausalMechanismQualifierEnum : causal_mechanism_qualifier
        
      ChemicalAffectsGeneAssociation : description
        
      ChemicalAffectsGeneAssociation : has_attribute
        
          ChemicalAffectsGeneAssociation --|> attribute : has_attribute
        
      ChemicalAffectsGeneAssociation : has_evidence
        
          ChemicalAffectsGeneAssociation --|> evidence type : has_evidence
        
      ChemicalAffectsGeneAssociation : id
        
      ChemicalAffectsGeneAssociation : iri
        
      ChemicalAffectsGeneAssociation : knowledge_source
        
      ChemicalAffectsGeneAssociation : name
        
      ChemicalAffectsGeneAssociation : negated
        
      ChemicalAffectsGeneAssociation : object
        
          ChemicalAffectsGeneAssociation --|> gene or gene product : object
        
      ChemicalAffectsGeneAssociation : object_aspect_qualifier
        
          ChemicalAffectsGeneAssociation --|> GeneOrGeneProductOrChemicalPartQualifierEnum : object_aspect_qualifier
        
      ChemicalAffectsGeneAssociation : object_category
        
          ChemicalAffectsGeneAssociation --|> ontology class : object_category
        
      ChemicalAffectsGeneAssociation : object_category_closure
        
          ChemicalAffectsGeneAssociation --|> ontology class : object_category_closure
        
      ChemicalAffectsGeneAssociation : object_closure
        
      ChemicalAffectsGeneAssociation : object_context_qualifier
        
          ChemicalAffectsGeneAssociation --|> anatomical entity : object_context_qualifier
        
      ChemicalAffectsGeneAssociation : object_form_or_variant_qualifier
        
          ChemicalAffectsGeneAssociation --|> ChemicalOrGeneOrGeneProductFormOrVariantEnum : object_form_or_variant_qualifier
        
      ChemicalAffectsGeneAssociation : object_label_closure
        
      ChemicalAffectsGeneAssociation : object_namespace
        
      ChemicalAffectsGeneAssociation : object_part_qualifier
        
          ChemicalAffectsGeneAssociation --|> GeneOrGeneProductOrChemicalPartQualifierEnum : object_part_qualifier
        
      ChemicalAffectsGeneAssociation : original_object
        
      ChemicalAffectsGeneAssociation : original_predicate
        
      ChemicalAffectsGeneAssociation : original_subject
        
      ChemicalAffectsGeneAssociation : predicate
        
      ChemicalAffectsGeneAssociation : primary_knowledge_source
        
      ChemicalAffectsGeneAssociation : publications
        
          ChemicalAffectsGeneAssociation --|> publication : publications
        
      ChemicalAffectsGeneAssociation : qualified_predicate
        
      ChemicalAffectsGeneAssociation : qualifiers
        
          ChemicalAffectsGeneAssociation --|> ontology class : qualifiers
        
      ChemicalAffectsGeneAssociation : retrieval_source_ids
        
          ChemicalAffectsGeneAssociation --|> retrieval source : retrieval_source_ids
        
      ChemicalAffectsGeneAssociation : subject
        
          ChemicalAffectsGeneAssociation --|> chemical entity : subject
        
      ChemicalAffectsGeneAssociation : subject_aspect_qualifier
        
          ChemicalAffectsGeneAssociation --|> GeneOrGeneProductOrChemicalPartQualifierEnum : subject_aspect_qualifier
        
      ChemicalAffectsGeneAssociation : subject_category
        
          ChemicalAffectsGeneAssociation --|> ontology class : subject_category
        
      ChemicalAffectsGeneAssociation : subject_category_closure
        
          ChemicalAffectsGeneAssociation --|> ontology class : subject_category_closure
        
      ChemicalAffectsGeneAssociation : subject_closure
        
      ChemicalAffectsGeneAssociation : subject_context_qualifier
        
          ChemicalAffectsGeneAssociation --|> anatomical entity : subject_context_qualifier
        
      ChemicalAffectsGeneAssociation : subject_derivative_qualifier
        
          ChemicalAffectsGeneAssociation --|> ChemicalEntityDerivativeEnum : subject_derivative_qualifier
        
      ChemicalAffectsGeneAssociation : subject_direction_qualifier
        
          ChemicalAffectsGeneAssociation --|> DirectionQualifierEnum : subject_direction_qualifier
        
      ChemicalAffectsGeneAssociation : subject_form_or_variant_qualifier
        
          ChemicalAffectsGeneAssociation --|> ChemicalOrGeneOrGeneProductFormOrVariantEnum : subject_form_or_variant_qualifier
        
      ChemicalAffectsGeneAssociation : subject_label_closure
        
      ChemicalAffectsGeneAssociation : subject_namespace
        
      ChemicalAffectsGeneAssociation : subject_part_qualifier
        
          ChemicalAffectsGeneAssociation --|> GeneOrGeneProductOrChemicalPartQualifierEnum : subject_part_qualifier
        
      ChemicalAffectsGeneAssociation : timepoint
        
      ChemicalAffectsGeneAssociation : type
        
      
```





## Inheritance
* [Entity](Entity.md)
    * [Association](Association.md)
        * **ChemicalAffectsGeneAssociation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) | 0..1 <br/> [ChemicalOrGeneOrGeneProductFormOrVariantEnum](ChemicalOrGeneOrGeneProductFormOrVariantEnum.md) |  | direct |
| [subject_part_qualifier](subject_part_qualifier.md) | 0..1 <br/> [GeneOrGeneProductOrChemicalPartQualifierEnum](GeneOrGeneProductOrChemicalPartQualifierEnum.md) |  | direct |
| [subject_derivative_qualifier](subject_derivative_qualifier.md) | 0..1 <br/> [ChemicalEntityDerivativeEnum](ChemicalEntityDerivativeEnum.md) |  | direct |
| [subject_aspect_qualifier](subject_aspect_qualifier.md) | 0..1 <br/> [GeneOrGeneProductOrChemicalPartQualifierEnum](GeneOrGeneProductOrChemicalPartQualifierEnum.md) |  | direct |
| [subject_context_qualifier](subject_context_qualifier.md) | 0..1 <br/> [AnatomicalEntity](AnatomicalEntity.md) |  | direct |
| [subject_direction_qualifier](subject_direction_qualifier.md) | 0..1 <br/> [DirectionQualifierEnum](DirectionQualifierEnum.md) |  | direct |
| [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) | 0..1 <br/> [ChemicalOrGeneOrGeneProductFormOrVariantEnum](ChemicalOrGeneOrGeneProductFormOrVariantEnum.md) |  | direct |
| [object_part_qualifier](object_part_qualifier.md) | 0..1 <br/> [GeneOrGeneProductOrChemicalPartQualifierEnum](GeneOrGeneProductOrChemicalPartQualifierEnum.md) |  | direct |
| [object_aspect_qualifier](object_aspect_qualifier.md) | 0..1 <br/> [GeneOrGeneProductOrChemicalPartQualifierEnum](GeneOrGeneProductOrChemicalPartQualifierEnum.md) |  | direct |
| [object_context_qualifier](object_context_qualifier.md) | 0..1 <br/> [AnatomicalEntity](AnatomicalEntity.md) |  | direct |
| [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | 0..1 <br/> [CausalMechanismQualifierEnum](CausalMechanismQualifierEnum.md) | A statement qualifier representing a type of molecular control mechanism thro... | direct |
| [anatomical_context_qualifier](anatomical_context_qualifier.md) | 0..1 <br/> [AnatomicalEntity](AnatomicalEntity.md) | A statement qualifier representing an anatomical location where an relationsh... | direct |
| [qualified_predicate](qualified_predicate.md) | 0..1 <br/> [String](String.md) | Predicate to be used in an association when subject and object qualifiers are... | direct |
| [subject](subject.md) | 1..1 <br/> [ChemicalEntity](ChemicalEntity.md) | connects an association to the subject of the association | [Association](Association.md) |
| [predicate](predicate.md) | 1..1 <br/> [PredicateType](PredicateType.md) | A high-level grouping for the relationship type | [Association](Association.md) |
| [object](object.md) | 1..1 <br/> [GeneOrGeneProduct](GeneOrGeneProduct.md) | connects an association to the object of the association | [Association](Association.md) |
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
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for an entity | [Entity](Entity.md) |
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
| self | bican:ChemicalAffectsGeneAssociation |
| native | bican:ChemicalAffectsGeneAssociation |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: chemical affects gene association
description: Describes an effect that a chemical has on a gene or gene product (e.g.
  an impact of on its abundance, activity, localization, processing, expression, etc.)
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: association
slots:
- subject form or variant qualifier
- subject part qualifier
- subject derivative qualifier
- subject aspect qualifier
- subject context qualifier
- subject direction qualifier
- object form or variant qualifier
- object part qualifier
- object aspect qualifier
- object context qualifier
- causal mechanism qualifier
- anatomical context qualifier
- qualified predicate
slot_usage:
  subject:
    name: subject
    domain_of:
    - association
    range: chemical entity
  subject form or variant qualifier:
    name: subject form or variant qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    - gene has variant that contributes to disease association
    range: ChemicalOrGeneOrGeneProductFormOrVariantEnum
  subject part qualifier:
    name: subject part qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  subject derivative qualifier:
    name: subject derivative qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: ChemicalEntityDerivativeEnum
  subject aspect qualifier:
    name: subject aspect qualifier
    domain_of:
    - predicate mapping
    - chemical affects gene association
    - gene to disease or phenotypic feature association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  subject context qualifier:
    name: subject context qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: anatomical entity
  subject direction qualifier:
    name: subject direction qualifier
    domain_of:
    - predicate mapping
    - chemical affects gene association
    range: DirectionQualifierEnum
  predicate:
    name: predicate
    domain_of:
    - predicate mapping
    - association
    subproperty_of: affects
  qualified predicate:
    name: qualified predicate
    domain_of:
    - predicate mapping
    - chemical affects gene association
    subproperty_of: causes
  object:
    name: object
    domain_of:
    - association
    range: gene or gene product
  object form or variant qualifier:
    name: object form or variant qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: ChemicalOrGeneOrGeneProductFormOrVariantEnum
  object part qualifier:
    name: object part qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  object aspect qualifier:
    name: object aspect qualifier
    domain_of:
    - predicate mapping
    - chemical affects gene association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  object context qualifier:
    name: object context qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: anatomical entity
  object direction qualifier:
    name: object direction qualifier
    range: DirectionQualifierEnum
  causal mechanism qualifier:
    name: causal mechanism qualifier
    domain_of:
    - predicate mapping
    - chemical affects gene association
    range: CausalMechanismQualifierEnum
  anatomical context qualifier:
    name: anatomical context qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: anatomical entity
  species context qualifier:
    name: species context qualifier
    range: organism taxon

```
</details>

### Induced

<details>
```yaml
name: chemical affects gene association
description: Describes an effect that a chemical has on a gene or gene product (e.g.
  an impact of on its abundance, activity, localization, processing, expression, etc.)
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: association
slot_usage:
  subject:
    name: subject
    domain_of:
    - association
    range: chemical entity
  subject form or variant qualifier:
    name: subject form or variant qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    - gene has variant that contributes to disease association
    range: ChemicalOrGeneOrGeneProductFormOrVariantEnum
  subject part qualifier:
    name: subject part qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  subject derivative qualifier:
    name: subject derivative qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: ChemicalEntityDerivativeEnum
  subject aspect qualifier:
    name: subject aspect qualifier
    domain_of:
    - predicate mapping
    - chemical affects gene association
    - gene to disease or phenotypic feature association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  subject context qualifier:
    name: subject context qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: anatomical entity
  subject direction qualifier:
    name: subject direction qualifier
    domain_of:
    - predicate mapping
    - chemical affects gene association
    range: DirectionQualifierEnum
  predicate:
    name: predicate
    domain_of:
    - predicate mapping
    - association
    subproperty_of: affects
  qualified predicate:
    name: qualified predicate
    domain_of:
    - predicate mapping
    - chemical affects gene association
    subproperty_of: causes
  object:
    name: object
    domain_of:
    - association
    range: gene or gene product
  object form or variant qualifier:
    name: object form or variant qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: ChemicalOrGeneOrGeneProductFormOrVariantEnum
  object part qualifier:
    name: object part qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  object aspect qualifier:
    name: object aspect qualifier
    domain_of:
    - predicate mapping
    - chemical affects gene association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  object context qualifier:
    name: object context qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: anatomical entity
  object direction qualifier:
    name: object direction qualifier
    range: DirectionQualifierEnum
  causal mechanism qualifier:
    name: causal mechanism qualifier
    domain_of:
    - predicate mapping
    - chemical affects gene association
    range: CausalMechanismQualifierEnum
  anatomical context qualifier:
    name: anatomical context qualifier
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: anatomical entity
  species context qualifier:
    name: species context qualifier
    range: organism taxon
attributes:
  subject form or variant qualifier:
    name: subject form or variant qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: form or variant qualifier
    domain: association
    alias: subject_form_or_variant_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    - gene has variant that contributes to disease association
    range: ChemicalOrGeneOrGeneProductFormOrVariantEnum
  subject part qualifier:
    name: subject part qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: part qualifier
    domain: association
    alias: subject_part_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  subject derivative qualifier:
    name: subject derivative qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: derivative qualifier
    domain: association
    alias: subject_derivative_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: ChemicalEntityDerivativeEnum
  subject aspect qualifier:
    name: subject aspect qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: aspect qualifier
    domain: association
    alias: subject_aspect_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical affects gene association
    - gene to disease or phenotypic feature association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  subject context qualifier:
    name: subject context qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: context qualifier
    domain: association
    alias: subject_context_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: anatomical entity
  subject direction qualifier:
    name: subject direction qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: direction qualifier
    domain: association
    alias: subject_direction_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical affects gene association
    range: DirectionQualifierEnum
  object form or variant qualifier:
    name: object form or variant qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: form or variant qualifier
    domain: association
    alias: object_form_or_variant_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: ChemicalOrGeneOrGeneProductFormOrVariantEnum
  object part qualifier:
    name: object part qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: part qualifier
    domain: association
    alias: object_part_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  object aspect qualifier:
    name: object aspect qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: aspect qualifier
    domain: association
    alias: object_aspect_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical affects gene association
    range: GeneOrGeneProductOrChemicalPartQualifierEnum
  object context qualifier:
    name: object context qualifier
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: context qualifier
    domain: association
    alias: object_context_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: anatomical entity
  causal mechanism qualifier:
    name: causal mechanism qualifier
    description: A statement qualifier representing a type of molecular control mechanism
      through which an effect of a chemical on a gene or gene product is mediated
      (e.g. 'agonism', 'inhibition', 'allosteric modulation', 'channel blocker')
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: statement qualifier
    domain: association
    alias: causal_mechanism_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical affects gene association
    range: CausalMechanismQualifierEnum
  anatomical context qualifier:
    name: anatomical context qualifier
    description: A statement qualifier representing an anatomical location where an
      relationship expressed in an association took place (can be a tissue, cell type,
      or sub-cellular location).
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: statement qualifier
    domain: association
    alias: anatomical_context_qualifier
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical gene interaction association
    - chemical affects gene association
    range: anatomical entity
  qualified predicate:
    name: qualified predicate
    description: Predicate to be used in an association when subject and object qualifiers
      are present and the full reading of the statement requires a qualification to
      the predicate in use in order to refine or  increase the specificity of the
      full statement reading.  This qualifier holds a relationship to be used instead
      of that  expressed by the primary predicate, in a ‘full statement’ reading of
      the association, where qualifier-based  semantics are included.  This is necessary
      only in cases where the primary predicate does not work in a  full statement
      reading.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: qualifier
    domain: association
    alias: qualified_predicate
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - chemical affects gene association
    subproperty_of: causes
    range: string
  subject:
    name: subject
    description: connects an association to the subject of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    alias: subject
    owner: chemical affects gene association
    domain_of:
    - association
    range: chemical entity
    required: true
  predicate:
    name: predicate
    description: A high-level grouping for the relationship type. AKA minimal predicate.
      This is analogous to category for nodes.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:predicate
    alias: predicate
    owner: chemical affects gene association
    domain_of:
    - predicate mapping
    - association
    subproperty_of: affects
    range: predicate type
    required: true
  object:
    name: object
    description: connects an association to the object of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    slot_uri: rdf:object
    alias: object
    owner: chemical affects gene association
    domain_of:
    - association
    range: gene or gene product
    required: true
  negated:
    name: negated
    description: if set to true, then the association is negated i.e. is not true
    from_schema: https://identifiers.org/brain-bican/kb-model
    rank: 1000
    is_a: association slot
    domain: association
    alias: negated
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
    domain_of:
    - association
    range: retrieval source
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
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
    owner: chemical affects gene association
    domain_of:
    - entity
    range: attribute

```
</details>