# Slot: has_adverse_event


_An untoward medical occurrence in a patient or clinical investigation subject that happens during treatment  with a therapeutic agent. Adverse events may be caused by something  other than the drug or therapy being given and may include abnormal laboratory finding, symptoms, or  diseases temporally associated with the treatment, whether or not considered related to the treatment.  Adverse events are unintended effects that occur when a medication is administered correctly._



URI: [bican:has_adverse_event](https://identifiers.org/brain-bican/vocab/has_adverse_event)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * [affects](affects.md)
            * **has_adverse_event**








## Properties

* Range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

* Multivalued: True



## Aliases


* adverse effect



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
name: has adverse event
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: An untoward medical occurrence in a patient or clinical investigation
  subject that happens during treatment  with a therapeutic agent. Adverse events
  may be caused by something  other than the drug or therapy being given and may include
  abnormal laboratory finding, symptoms, or  diseases temporally associated with the
  treatment, whether or not considered related to the treatment.  Adverse events are
  unintended effects that occur when a medication is administered correctly.
from_schema: https://identifiers.org/brain-bican/kb-model
aliases:
- adverse effect
rank: 1000
is_a: affects
domain: chemical or drug or treatment
multivalued: true
inherited: true
alias: has_adverse_event
range: disease or phenotypic feature

```
</details>