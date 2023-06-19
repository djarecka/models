# Slot: regulates


_A more specific form of affects, that implies the effect results from a biologically evolved control mechanism. Gene-affects-gene relationships will (almost) always involve regulation.  Exogenous/environmental chemical-affects-gene relationships  are not cases of regulation in this definition. Instead these would be captured using the 'affects' predicate, or possibly one of the 'interacts with' predicates depending on the nature of the interaction._



URI: [bican:regulates](https://identifiers.org/brain-bican/vocab/regulates)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **regulates** [ [interacts_with](interacts_with.md)]








## Properties

* Range: [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: regulates
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: A more specific form of affects, that implies the effect results from
  a biologically evolved control mechanism. Gene-affects-gene relationships will (almost)
  always involve regulation.  Exogenous/environmental chemical-affects-gene relationships  are
  not cases of regulation in this definition. Instead these would be captured using
  the 'affects' predicate, or possibly one of the 'interacts with' predicates depending
  on the nature of the interaction.
notes:
- The RO definition of 'directly regulates the activity of' is an exact_mapping here
  because  it describes genetic regulation from the point of view of one genetic entity
  regulating another, as opposed to "RO:0002211" which describes process to process
  regulation.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002448
broad_mappings:
- WIKIDATA_PROPERTY:P128
- CHEMBL.MECHANISM:modulator
- RO:0002295
- RO:0002332
- RO:0002448
rank: 1000
is_a: affects
mixins:
- interacts with
domain: physical essence or occurrent
multivalued: true
inherited: true
alias: regulates
range: physical essence or occurrent

```
</details>