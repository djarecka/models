# Slot: transcribed_from


_x is transcribed from y if and only if x is synthesized from template y_



URI: [bican:transcribed_from](https://identifiers.org/brain-bican/vocab/transcribed_from)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **transcribed_from**








## Properties

* Range: [Gene](Gene.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| canonical_predicate | True |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: transcribed from
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: x is transcribed from y if and only if x is synthesized from template
  y
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002510
- SIO:010081
rank: 1000
is_a: related to at instance level
domain: transcript
multivalued: true
inherited: true
alias: transcribed_from
inverse: transcribed to
range: gene

```
</details>