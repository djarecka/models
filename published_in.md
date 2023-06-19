# Slot: published_in


_CURIE identifier of a broader publication context within which the publication may be placed, e.g. a specified book or journal._



URI: [bican:published_in](https://identifiers.org/brain-bican/vocab/published_in)




## Inheritance

* [node_property](node_property.md)
    * **published_in**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BookChapter](BookChapter.md) |  |  yes  |
[Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone  section ... |  yes  |
[JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published  in a... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: published in
description: CURIE identifier of a broader publication context within which the publication
  may be placed, e.g. a specified book or journal.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA_PROPERTY:P1433
rank: 1000
is_a: node property
values_from:
- NLMID
- issn
- isbn
domain: publication
alias: published_in
domain_of:
- book chapter
- article
range: uriorcurie

```
</details>