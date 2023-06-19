# Slot: related_to_at_instance_level


_Represents a relationship held between two instances of a data classes.  Much like an assertion component, in an ABox, these represent facts associated with the conceptual model._



URI: [bican:related_to_at_instance_level](https://identifiers.org/brain-bican/vocab/related_to_at_instance_level)




## Inheritance

* [related_to](related_to.md)
    * **related_to_at_instance_level**
        * [associated_with](associated_with.md)
        * [opposite_of](opposite_of.md)
        * [target_for](target_for.md)
        * [has_target](has_target.md)
        * [active_in](active_in.md)
        * [has_active_component](has_active_component.md)
        * [acts_upstream_of](acts_upstream_of.md)
        * [has_upstream_actor](has_upstream_actor.md)
        * [mentions](mentions.md)
        * [mentioned_by](mentioned_by.md)
        * [contributor](contributor.md)
        * [has_contributor](has_contributor.md)
        * [assesses](assesses.md)
        * [is_assessed_by](is_assessed_by.md)
        * [interacts_with](interacts_with.md)
        * [affects](affects.md)
        * [affected_by](affected_by.md)
        * [diagnoses](diagnoses.md)
        * [is_diagnosed_by](is_diagnosed_by.md)
        * [increases_amount_or_activity_of](increases_amount_or_activity_of.md)
        * [amount_or_activity_increased_by](amount_or_activity_increased_by.md)
        * [decreases_amount_or_activity_of](decreases_amount_or_activity_of.md)
        * [amount_or_activity_decreased_by](amount_or_activity_decreased_by.md)
        * [gene_product_of](gene_product_of.md)
        * [has_gene_product](has_gene_product.md)
        * [transcribed_to](transcribed_to.md)
        * [transcribed_from](transcribed_from.md)
        * [translates_to](translates_to.md)
        * [translation_of](translation_of.md)
        * [coexists_with](coexists_with.md)
        * [affects_risk_for](affects_risk_for.md)
        * [risk_affected_by](risk_affected_by.md)
        * [contributes_to](contributes_to.md)
        * [contribution_from](contribution_from.md)
        * [has_phenotype](has_phenotype.md)
        * [phenotype_of](phenotype_of.md)
        * [occurs_in](occurs_in.md)
        * [contains_process](contains_process.md)
        * [located_in](located_in.md)
        * [location_of](location_of.md)
        * [similar_to](similar_to.md)
        * [has_sequence_location](has_sequence_location.md)
        * [sequence_location_of](sequence_location_of.md)
        * [model_of](model_of.md)
        * [models](models.md)
        * [overlaps](overlaps.md)
        * [has_participant](has_participant.md)
        * [participates_in](participates_in.md)
        * [derives_into](derives_into.md)
        * [derives_from](derives_from.md)
        * [manifestation_of](manifestation_of.md)
        * [has_manifestation](has_manifestation.md)
        * [produces](produces.md)
        * [produced_by](produced_by.md)
        * [temporally_related_to](temporally_related_to.md)
        * [related_condition](related_condition.md)
        * [is_sequence_variant_of](is_sequence_variant_of.md)
        * [has_sequence_variant](has_sequence_variant.md)
        * [disease_has_basis_in](disease_has_basis_in.md)
        * [occurs_in_disease](occurs_in_disease.md)
        * [contraindicated_for](contraindicated_for.md)
        * [has_contraindication](has_contraindication.md)
        * [has_not_completed](has_not_completed.md)
        * [not_completed_by](not_completed_by.md)
        * [has_completed](has_completed.md)
        * [completed_by](completed_by.md)
        * [in_linkage_disequilibrium_with](in_linkage_disequilibrium_with.md)
        * [has_increased_amount](has_increased_amount.md)
        * [increased_amount_of](increased_amount_of.md)
        * [has_decreased_amount](has_decreased_amount.md)
        * [decreased_amount_in](decreased_amount_in.md)
        * [lacks_part](lacks_part.md)
        * [missing_from](missing_from.md)
        * [develops_from](develops_from.md)
        * [develops_into](develops_into.md)
        * [in_taxon](in_taxon.md)
        * [taxon_of](taxon_of.md)
        * [has_molecular_consequence](has_molecular_consequence.md)
        * [is_molecular_consequence_of](is_molecular_consequence_of.md)








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
name: related to at instance level
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: Represents a relationship held between two instances of a data classes.  Much
  like an assertion component, in an ABox, these represent facts associated with the
  conceptual model.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: related to
domain: named thing
multivalued: true
inherited: true
alias: related_to_at_instance_level
symmetric: true
range: named thing

```
</details>