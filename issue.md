# Slot: issue


_issue of a newspaper, a scientific journal or magazine for reference purpose_



URI: [bican:issue](https://identifiers.org/brain-bican/vocab/issue)




## Inheritance

* [node_property](node_property.md)
    * **issue**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
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
name: issue
description: issue of a newspaper, a scientific journal or magazine for reference
  purpose
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA_PROPERTY:P433
rank: 1000
is_a: node property
domain: publication
alias: issue
domain_of:
- serial
- article
range: string

```
</details>