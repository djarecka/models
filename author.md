# Slot: author


_an instance of one (co-)creator primarily responsible for a written work_



URI: [bican:author](https://identifiers.org/brain-bican/vocab/author)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contributor](contributor.md)
            * **author**








## Properties

* Range: [Publication](Publication.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: author
description: an instance of one (co-)creator primarily responsible for a written work
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- dct:creator
- WIKIDATA_PROPERTY:P50
rank: 1000
is_a: contributor
domain: agent
multivalued: true
inherited: true
alias: author
range: publication

```
</details>