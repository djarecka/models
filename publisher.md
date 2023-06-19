# Slot: publisher


_organization or person responsible for publishing books, periodicals, podcasts, games or software. Note that in the case of publications which have a containing "published in" node property, the publisher association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the publisher agent of the encompassing publication (e.g. only from the Journal referenced by the 'published_in' property of an journal article Publication node)._



URI: [bican:publisher](https://identifiers.org/brain-bican/vocab/publisher)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contributor](contributor.md)
            * **publisher**








## Properties

* Range: [Publication](Publication.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: publisher
description: organization or person responsible for publishing books, periodicals,
  podcasts, games or software. Note that in the case of publications which have a
  containing "published in" node property, the publisher association may not be attached
  directly to the embedded child publication, but only made in between the parent's
  publication node and the publisher agent of the encompassing publication (e.g. only
  from the Journal referenced by the 'published_in' property of an journal article
  Publication node).
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- dct:publisher
- WIKIDATA_PROPERTY:P123
rank: 1000
is_a: contributor
domain: agent
multivalued: true
inherited: true
alias: publisher
range: publication

```
</details>