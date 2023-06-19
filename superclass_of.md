# Slot: superclass_of


_holds between two classes where the domain class is a super class of the range class_



URI: [bican:superclass_of](https://identifiers.org/brain-bican/vocab/superclass_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_concept_level](related_to_at_concept_level.md)
        * **superclass_of**








## Properties

* Range: [OntologyClass](OntologyClass.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: superclass of
description: holds between two classes where the domain class is a super class of
  the range class
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA:Q66088480
- CHEMBL.MECHANISM:superset_of
- GO:inverse_isa
- RXNORM:inverse_isa
- MESH:inverse_isa
- VANDF:inverse_isa
narrow_mappings:
- NCIT:cdrh_parent_of
- NCIT:ctcae_5_parent_of
- NCIT:subset_includes_concept
- OMIM:has_manifestation
- SNOMED:has_basic_dose_form
- UMLS:RB
rank: 1000
is_a: related to at concept level
domain: ontology class
multivalued: true
inherited: true
alias: superclass_of
range: ontology class

```
</details>