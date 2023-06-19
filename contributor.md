# Slot: contributor

URI: [bican:contributor](https://identifiers.org/brain-bican/vocab/contributor)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **contributor**
            * [provider](provider.md)
            * [publisher](publisher.md)
            * [editor](editor.md)
            * [author](author.md)








## Properties

* Range: [InformationContentEntity](InformationContentEntity.md)

* Multivalued: True





## Comments

* This is a grouping for predicates relating entities to their associated contributors realizing them

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: contributor
comments:
- This is a grouping for predicates relating entities to their associated contributors
  realizing them
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- dct:contributor
rank: 1000
is_a: related to at instance level
abstract: true
domain: agent
multivalued: true
inherited: true
alias: contributor
range: information content entity

```
</details>