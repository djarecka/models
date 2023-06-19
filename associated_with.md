# Slot: associated_with


_Expresses a relationship between two named things where the relationship is typically generated statistically (though not in all cases), and is weaker than its child, 'correlated with', but stronger than its parent, 'related to'. This relationship holds between two concepts represented by variables for which a statistical  dependence is demonstrated.  E.g. the statement “Atrial Fibrillation (Afib) is associated with Myocardial  Infraction (MI)” asserts that having Afib is not statistically independent from whether a patient  will also have MI. Note that in Translator associations, the subject and object concepts may map exactly to  the statistical variables, or represent related entities for which the variables serve as proxies in an  Association (e.g. diseases, chemical entities or processes)._



URI: [bican:associated_with](https://identifiers.org/brain-bican/vocab/associated_with)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **associated_with**
            * [associated_with_likelihood_of](associated_with_likelihood_of.md)
            * [likelihood_associated_with](likelihood_associated_with.md)
            * [associated_with_sensitivity_to](associated_with_sensitivity_to.md)
            * [sensitivity_associated_with](sensitivity_associated_with.md)
            * [associated_with_resistance_to](associated_with_resistance_to.md)
            * [resistance_associated_with](resistance_associated_with.md)
            * [genetic_association](genetic_association.md)
            * [genetically_associated_with](genetically_associated_with.md)
            * [correlated_with](correlated_with.md)








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
name: associated with
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: Expresses a relationship between two named things where the relationship
  is typically generated statistically (though not in all cases), and is weaker than
  its child, 'correlated with', but stronger than its parent, 'related to'. This relationship
  holds between two concepts represented by variables for which a statistical  dependence
  is demonstrated.  E.g. the statement “Atrial Fibrillation (Afib) is associated with
  Myocardial  Infraction (MI)” asserts that having Afib is not statistically independent
  from whether a patient  will also have MI. Note that in Translator associations,
  the subject and object concepts may map exactly to  the statistical variables, or
  represent related entities for which the variables serve as proxies in an  Association
  (e.g. diseases, chemical entities or processes).
from_schema: https://identifiers.org/brain-bican/kb-model
narrow_mappings:
- RO:0004029
- SNOMEDCT:47429007
rank: 1000
is_a: related to at instance level
domain: named thing
multivalued: true
inherited: true
alias: associated_with
symmetric: true
range: named thing

```
</details>