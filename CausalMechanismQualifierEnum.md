# Enum: CausalMechanismQualifierEnum



URI: [CausalMechanismQualifierEnum](CausalMechanismQualifierEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| binding | None | A causal mechanism mediated by the direct contact between effector and target... |
| inhibition | None | A causal mechanism in which the effector binds to the target and negatively e... |
| antibody_inhibition | None | A causal mechanism in which an antibody specifically binds to and interferes ... |
| antagonism | None | A causal mechanism in which the effector binds to a receptor and prevents act... |
| molecular_channel_blockage | None | A causal mechanism in which the effector binds to a molecular channel and pre... |
| inverse_agonism | None | A causal mechanism in which the effector binds to the same receptor-binding s... |
| negative_allosteric_modulation | None | A causal mechanism in which the effector reduces or prevents the action of th... |
| agonism | None | A causal mechanism in which the effector binds and activates a receptor to mi... |
| molecular_channel_opening | None | A causal mechanism in which the effector binds to a molecular channel and fac... |
| positive_allosteric_modulation | None | A causal mechanism in which the effector enhances the action of the endogenou... |
| potentiation | None | A causal mechanism in which the effector  binds to and enhances or intensifie... |
| activation | None | A causal mechanism in which the effector binds to and positively affects the ... |
| inducer | None | A causal mechanism in which the effector binds to and increases the activity/... |
| transcriptional_regulation | None | A causal mechanism mediated by through the control of target gene transcripti... |
| signaling_mediated_control | None | A causal mechanism mediated by the activation or control of signaling events ... |
| stabilization | None |  |
| stimulation | None |  |
| releasing_activity | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | A statement qualifier representing a type of molecular control mechanism thro... |
| [causal_mechanism_qualifier](causal_mechanism_qualifier.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: CausalMechanismQualifierEnum
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
permissible_values:
  binding:
    text: binding
    description: A causal mechanism mediated by the direct contact between effector
      and target chemical or  biomolecular entity, which form a stable physical interaction.
  inhibition:
    text: inhibition
    description: A causal mechanism in which the effector binds to the target and
      negatively effects its normal function,  e.g. prevention of enzymatic reaction
      or activation of downstream pathway.
    is_a: binding
    close_mappings:
    - DGIdb:inhibitor
    - SEMMEDDB:INHIBITS
    narrow_mappings:
    - DGIdb:blocker
    - DGIdb:channel_blocker
    - DGIdb:gating_inhibitor
    - CHEMBL.MECHANISM:antisense_inhibitor
    - CHEMBL.MECHANISM:blocker
    - CHEMBL.MECHANISM:inhibitor
    - CHEMBL.MECHANISM:negative_allosteric_modulator
    - CHEMBL.MECHANISM:negative_modulator
    - DGIdb:negative_modulator
  antibody_inhibition:
    text: antibody_inhibition
    description: A causal mechanism in which an antibody specifically binds to and
      interferes with the target.
    is_a: inhibition
  antagonism:
    text: antagonism
    description: A causal mechanism in which the effector binds to a receptor and
      prevents activation by an agonist  through competing for the binding site.
    is_a: inhibition
    close_mappings:
    - DGIdb:antagonist
    - CHEMBL.MECHANISM:antagonist
    narrow_mappings:
    - CHEMBL.MECHANISM:allosteric_antagonist
  molecular_channel_blockage:
    text: molecular_channel_blockage
    description: A causal mechanism in which the effector binds to a molecular channel
      and prevents or reduces  transport of ions through it.
    is_a: inhibition
  inverse_agonism:
    text: inverse_agonism
    description: A causal mechanism in which the effector binds to the same receptor-binding
      site as an agonist and antagonizes its effects, often exerting the opposite
      effect of the agonist by suppressing spontaneous receptor signaling.
    is_a: inhibition
    close_mappings:
    - CHEMBL.MECHANISM:inverse_agonist
    - DGIdb:inverse_agonist
  negative_allosteric_modulation:
    text: negative_allosteric_modulation
    description: A causal mechanism in which the effector reduces or prevents the
      action of the endogenous ligand of a  receptor by binding to a site distinct
      from that ligand (i.e. non-competitive inhibition)
    is_a: inhibition
    close_mappings:
    - CHEMBL.MECHANISM:negative_allosteric_modulator
    - DGIdb:inhibitory_allosteric_modulator
    narrow_mappings:
    - DGIdb:negative_modulator
  agonism:
    text: agonism
    description: A causal mechanism in which the effector binds and activates a receptor
      to mimic the effect of an  endogenous ligand.
    is_a: activation
    close_mappings:
    - CHEMBL.MECHANISM:agonist
    - DGIdb:agonist
    narrow_mappings:
    - CHEMBL.MECHANISM:partial_agonist
    - DGIdb:partial_agonist
  molecular_channel_opening:
    text: molecular_channel_opening
    description: A causal mechanism in which the effector binds to a molecular channel
      and facilitates transport of  ions through it.
    is_a: activation
    close_mappings:
    - CHEMBL.MECHANISM:opener
  positive_allosteric_modulation:
    text: positive_allosteric_modulation
    description: A causal mechanism in which the effector enhances the action of the
      endogenous ligand of a receptor by  binding to a site distinct from that ligand
      (i.e. non-competitive inhibition)
    is_a: activation
    close_mappings:
    - CHEMBL.MECHANISM:positive_allosteric_modulator
    - CHEMBL.MECHANISM:positive_modulator
    - DGIdb:positive_allosteric_modulator
    broad_mappings:
    - DGIdb:modulator
    - DGIdb:allosteric_modulator
  potentiation:
    text: potentiation
    description: A causal mechanism in which the effector  binds to and enhances or
      intensifies the effect of some  other chemical or drug on its target.
    is_a: binding
  activation:
    text: activation
    description: A causal mechanism in which the effector binds to and positively
      affects the normal functioning of its target.
    is_a: binding
    close_mappings:
    - CHEMBL.MECHANISM:activator
    - DGIdb:activator
  inducer:
    text: inducer
    description: A causal mechanism in which the effector binds to and increases the
      activity/rate of an enzyme that  processes drugs in the body.
    is_a: binding
    close_mappings:
    - DGIdb:inducer
  transcriptional_regulation:
    text: transcriptional_regulation
    description: A causal mechanism mediated by through the control of target gene
      transcription
  signaling_mediated_control:
    text: signaling_mediated_control
    description: A causal mechanism mediated by the activation or control of signaling
      events that influence the some aspect  of the target entity (e.g. its activity,
      processing, transport, etc)
  stabilization:
    text: stabilization
    is_a: activation
    close_mappings:
    - CHEMBL.MECHANISM:stabiliser
  stimulation:
    text: stimulation
    is_a: activation
    close_mappings:
    - DGIdb:stimulator
    - SEMMEDDB:STIMULATES
    - DGIdb:stimulator
  releasing_activity:
    text: releasing_activity
    is_a: activation
    close_mappings:
    - CHEMBL:MECHANISM:releasing_agent

```
</details>
