# Slot: iso_abbreviation


_Standard abbreviation for periodicals in the International Organization for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/. If the 'published in' property is set, then the iso abbreviation pertains to the broader publication context (the journal) within which the given publication node is embedded, not the publication itself._



URI: [bican:iso_abbreviation](https://identifiers.org/brain-bican/vocab/iso_abbreviation)




## Inheritance

* [node_property](node_property.md)
    * **iso_abbreviation**





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |  no  |
[Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone  section ... |  yes  |
[JournalArticle](JournalArticle.md) | an article, typically presenting results of research, that is published  in a... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: iso abbreviation
description: Standard abbreviation for periodicals in the International Organization
  for Standardization (ISO) 4 system See https://www.issn.org/services/online-services/access-to-the-ltwa/.
  If the 'published in' property is set, then the iso abbreviation pertains to the
  broader publication context (the journal) within which the given publication node
  is embedded, not the publication itself.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- WIKIDATA_PROPERTY:P1160
rank: 1000
is_a: node property
domain: publication
alias: iso_abbreviation
domain_of:
- serial
- article
range: string

```
</details>