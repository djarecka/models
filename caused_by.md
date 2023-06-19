# Slot: caused_by


_holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or generation of the other_



URI: [bican:caused_by](https://identifiers.org/brain-bican/vocab/caused_by)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contribution_from](contribution_from.md)
            * **caused_by**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True



## Aliases


* disease caused by disruption of
* disease has basis in dysfunction of
* realized in response to
* realized in response to stimulus



## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: caused by
description: holds between two entities where the occurrence, existence, or activity
  of one is caused by the occurrence or generation of the other
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- disease caused by disruption of
- disease has basis in dysfunction of
- realized in response to
- realized in response to stimulus
exact_mappings:
- WIKIDATA_PROPERTY:P828
narrow_mappings:
- RO:0001022
- RO:0002608
- RO:0004019
- RO:0004020
- RO:0004028
- RO:0009501
rank: 1000
is_a: contribution from
domain: named thing
multivalued: true
inherited: true
alias: caused_by
inverse: causes
range: named thing

```
</details>