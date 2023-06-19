# Slot: qualified_predicate


_Predicate to be used in an association when subject and object qualifiers are present and the full reading of the statement requires a qualification to the predicate in use in order to refine or  increase the specificity of the full statement reading.  This qualifier holds a relationship to be used instead of that  expressed by the primary predicate, in a ‘full statement’ reading of the association, where qualifier-based  semantics are included.  This is necessary only in cases where the primary predicate does not work in a  full statement reading._



URI: [bican:qualified_predicate](https://identifiers.org/brain-bican/vocab/qualified_predicate)




## Inheritance

* [association_slot](association_slot.md)
    * [qualifier](qualifier.md)
        * **qualified_predicate**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[PredicateMapping](PredicateMapping.md) | A deprecated predicate mapping object contains the deprecated predicate and a... |  no  |
[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md) | Describes an effect that a chemical has on a gene or gene product (e |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: qualified predicate
description: Predicate to be used in an association when subject and object qualifiers
  are present and the full reading of the statement requires a qualification to the
  predicate in use in order to refine or  increase the specificity of the full statement
  reading.  This qualifier holds a relationship to be used instead of that  expressed
  by the primary predicate, in a ‘full statement’ reading of the association, where
  qualifier-based  semantics are included.  This is necessary only in cases where
  the primary predicate does not work in a  full statement reading.
notes:
- 'to express the statement that “Chemical X causes increased expression of Gene Y”,
  the core triple is read  using the fields subject:ChemX, predicate:affects, object:GeneY
  . . . and the full statement is read using  the fields subject:ChemX, qualified_predicate:causes,
  object:GeneY, object_aspect: expression,  object_direction:increased. The predicate
  ‘affects’ is needed for the core triple reading, but does not make  sense in the
  full statement reading  (because “Chemical X affects increased expression of Gene
  Y'''' is not  what we mean to say here: it causes increased expression of Gene Y)'
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: qualifier
domain: association
alias: qualified_predicate
domain_of:
- predicate mapping
- chemical affects gene association
range: string

```
</details>