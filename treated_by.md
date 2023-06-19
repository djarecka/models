# Slot: treated_by


_holds between a disease or phenotypic feature and a therapeutic process or chemical entity that is used to treat the condition_



URI: [bican:treated_by](https://identifiers.org/brain-bican/vocab/treated_by)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affected_by](affected_by.md)
            * [is_ameliorated_by](is_ameliorated_by.md)
                * **treated_by**








## Properties

* Range: [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: treated by
description: holds between a disease or phenotypic feature and a therapeutic process
  or chemical entity that is used to treat the condition
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA_PROPERTY:P2176
- MONDO:disease_responds_to
narrow_mappings:
- RO:0002302
rank: 1000
is_a: is ameliorated by
domain: disease or phenotypic feature
multivalued: true
inherited: true
alias: treated_by
inverse: treats
range: chemical or drug or treatment

```
</details>