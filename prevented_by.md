# Slot: prevented_by


_holds between a potential outcome of which the likelihood was reduced by the application or use of an entity._



URI: [bican:prevented_by](https://identifiers.org/brain-bican/vocab/prevented_by)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [risk_affected_by](risk_affected_by.md)
            * **prevented_by**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| opposite_of | enabled by |



### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: prevented by
annotations:
  opposite_of:
    tag: opposite_of
    value: enabled by
description: holds between a potential outcome of which the likelihood was reduced
  by the application or use of an entity.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: risk affected by
domain: named thing
multivalued: true
inherited: true
alias: prevented_by
inverse: prevents
range: named thing

```
</details>