# Slot: preceded_by


_holds between two processes, where the other is completed before the one begins_



URI: [bican:preceded_by](https://identifiers.org/brain-bican/vocab/preceded_by)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [temporally_related_to](temporally_related_to.md)
            * **preceded_by**








## Properties

* Range: [Occurrent](Occurrent.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: preceded by
description: holds between two processes, where the other is completed before the
  one begins
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- BFO:0000062
narrow_mappings:
- FMA:transforms_from
- RO:0002087
- RO:0002285
broad_mappings:
- GENEPIO:0001739
rank: 1000
is_a: temporally related to
domain: occurrent
multivalued: true
inherited: true
alias: preceded_by
inverse: precedes
range: occurrent

```
</details>