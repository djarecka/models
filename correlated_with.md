# Slot: correlated_with


_A relationship that holds between two concepts represented by variables for which a statistical dependence is  demonstrated using a correlation analysis method._



URI: [bican:correlated_with](https://identifiers.org/brain-bican/vocab/correlated_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [associated_with](associated_with.md)
            * **correlated_with**
                * [positively_correlated_with](positively_correlated_with.md)
                * [negatively_correlated_with](negatively_correlated_with.md)
                * [occurs_together_in_literature_with](occurs_together_in_literature_with.md)
                * [coexpressed_with](coexpressed_with.md)
                * [has_biomarker](has_biomarker.md)
                * [biomarker_for](biomarker_for.md)








## Properties

* Range: [NamedThing](NamedThing.md)

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
name: correlated with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: A relationship that holds between two concepts represented by variables
  for which a statistical dependence is  demonstrated using a correlation analysis
  method.
notes:
- These concepts may map exactly to the statistical variables, or represent related
  entities for which the  variables serve as proxies in an Association (e.g. diseases,
  chemical entities or processes).
in_subset:
- translator_minimal
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- RO:0002610
- PATO:correlates_with
rank: 1000
is_a: associated with
domain: named thing
multivalued: true
inherited: true
alias: correlated_with
symmetric: true
range: named thing

```
</details>