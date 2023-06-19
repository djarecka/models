# Slot: editor


_editor of a compiled work such as a book or a periodical (newspaper or an academic journal). Note that in the case of publications which have a containing "published in" node property, the editor association may not be attached directly to the embedded child publication, but only made in between the parent's publication node and the editorial agent of the encompassing publication (e.g. only from the Book referenced by the 'published_in' property of a book chapter Publication node)._



URI: [bican:editor](https://identifiers.org/brain-bican/vocab/editor)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [contributor](contributor.md)
            * **editor**








## Properties

* Range: [Publication](Publication.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: editor
description: editor of a compiled work such as a book or a periodical (newspaper or
  an academic journal). Note that in the case of publications which have a containing
  "published in" node property, the editor association may not be attached directly
  to the embedded child publication, but only made in between the parent's publication
  node and the editorial agent of the encompassing publication (e.g. only from the
  Book referenced by the 'published_in' property of a book chapter Publication node).
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA_PROPERTY:P98
rank: 1000
is_a: contributor
domain: agent
multivalued: true
inherited: true
alias: editor
range: publication

```
</details>