# Slot: volume


_volume of a book or music release in a collection/series or a published collection of journal issues in a serial publication_



URI: [bican:volume](https://identifiers.org/brain-bican/vocab/volume)




## Inheritance

* [node_property](node_property.md)
    * **volume**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[BookChapter](BookChapter.md) |  |  no  |
[Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
[Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone  section ... |  no  |
[JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published  in a... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: volume
description: volume of a book or music release in a collection/series or a published
  collection of journal issues in a serial publication
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA_PROPERTY:P478
rank: 1000
is_a: node property
domain: publication
alias: volume
domain_of:
- book chapter
- serial
- article
range: string

```
</details>