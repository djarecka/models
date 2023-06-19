# Slot: pages


_page number of source referenced for statement or publication_



URI: [bican:pages](https://identifiers.org/brain-bican/vocab/pages)




## Inheritance

* [node_property](node_property.md)
    * **pages**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Publication](Publication.md) | Any ‘published’ piece of information |  yes  |
[Book](Book.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
[BookChapter](BookChapter.md) |  |  no  |
[Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
[Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone  section ... |  no  |
[JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published  in a... |  no  |
[Patent](Patent.md) | a legal document granted by a patent issuing authority which confers upon  th... |  no  |
[WebPage](WebPage.md) | a document that is published according to World Wide Web standards, which  ma... |  no  |
[PreprintPublication](PreprintPublication.md) | a document reresenting an early version of an author's original scholarly wor... |  no  |
[DrugLabel](DrugLabel.md) | a document accompanying a drug or its container that provides written, printe... |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: pages
description: page number of source referenced for statement or publication
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA_PROPERTY:P304
rank: 1000
is_a: node property
domain: publication
multivalued: true
alias: pages
domain_of:
- publication
range: string

```
</details>