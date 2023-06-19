# Slot: opposite_of


_x is the opposite of y if there exists some distance metric M, and there exists no z such as M(x,z) <= M(x,y) or M(y,z) <= M(y,x). (This description is from RO. Needs to be rephrased)._



URI: [bican:opposite_of](https://identifiers.org/brain-bican/vocab/opposite_of)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **opposite_of**








## Properties

* Range: [NamedThing](NamedThing.md)

* Multivalued: True





## See Also

* [https://doi.org/10.1101/108977](https://doi.org/10.1101/108977)
* [https://github.com/biolink/biolink-model/issues/657](https://github.com/biolink/biolink-model/issues/657)

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
name: opposite of
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: x is the opposite of y if there exists some distance metric M, and there
  exists no z such as M(x,z) <= M(x,y) or M(y,z) <= M(y,x). (This description is from
  RO. Needs to be rephrased).
from_schema: https://identifiers.org/brain-bican/kb-model
see_also:
- https://doi.org/10.1101/108977
- https://github.com/biolink/biolink-model/issues/657
exact_mappings:
- RO:0002604
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: opposite_of
symmetric: true
range: named thing

```
</details>