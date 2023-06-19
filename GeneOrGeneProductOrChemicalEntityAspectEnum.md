# Enum: GeneOrGeneProductOrChemicalEntityAspectEnum



URI: [GeneOrGeneProductOrChemicalEntityAspectEnum](GeneOrGeneProductOrChemicalEntityAspectEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| activity_or_abundance | None | Used in cases where the specificity of the relationship can not be determined... |
| abundance | None |  |
| activity | None |  |
| expression | None |  |
| synthesis | None |  |
| degradation | None |  |
| cleavage | None |  |
| hydrolysis | None |  |
| metabolic_processing | None |  |
| mutation_rate | None |  |
| stability | None |  |
| folding | None |  |
| localization | None |  |
| transport | None |  |
| secretion | None |  |
| uptake | None |  |
| molecular_modification | None |  |
| acetylation | None |  |
| acylation | None |  |
| alkylation | None |  |
| amination | None |  |
| carbamoylation | None |  |
| ethylation | None |  |
| glutathionylation | None |  |
| glycation | None |  |
| glycosylation | None |  |
| glucuronidation | None |  |
| n_linked_glycosylation | None |  |
| o_linked_glycosylation | None |  |
| hydroxylation | None |  |
| lipidation | None |  |
| farnesylation | None |  |
| geranoylation | None |  |
| myristoylation | None |  |
| palmitoylation | None |  |
| prenylation | None |  |
| methylation | None |  |
| nitrosation | None |  |
| nucleotidylation | None |  |
| phosphorylation | None |  |
| ribosylation | None |  |
| ADP-ribosylation | None |  |
| sulfation | None |  |
| sumoylation | None |  |
| ubiquitination | None |  |
| oxidation | None |  |
| reduction | None |  |
| carboxylation | None |  |




## Slots

| Name | Description |
| ---  | --- |
| [subject_aspect_qualifier](subject_aspect_qualifier.md) |  |






## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: GeneOrGeneProductOrChemicalEntityAspectEnum
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
permissible_values:
  activity_or_abundance:
    text: activity_or_abundance
    description: Used in cases where the specificity of the relationship can not be
      determined to be either activity  or abundance.  In general, a more specific
      value from this enumeration should be used.
  abundance:
    text: abundance
    is_a: activity_or_abundance
  activity:
    text: activity
    is_a: activity_or_abundance
  expression:
    text: expression
    is_a: abundance
  synthesis:
    text: synthesis
    is_a: abundance
  degradation:
    text: degradation
  cleavage:
    text: cleavage
    is_a: degradation
  hydrolysis:
    text: hydrolysis
    is_a: degradation
  metabolic_processing:
    text: metabolic_processing
  mutation_rate:
    text: mutation_rate
  stability:
    text: stability
  folding:
    text: folding
  localization:
    text: localization
  transport:
    text: transport
  secretion:
    text: secretion
    is_a: transport
  uptake:
    text: uptake
    is_a: transport
  molecular_modification:
    text: molecular_modification
  acetylation:
    text: acetylation
    is_a: molecular_modification
  acylation:
    text: acylation
    is_a: molecular_modification
  alkylation:
    text: alkylation
    is_a: molecular_modification
  amination:
    text: amination
    is_a: molecular_modification
  carbamoylation:
    text: carbamoylation
    is_a: molecular_modification
  ethylation:
    text: ethylation
    is_a: molecular_modification
  glutathionylation:
    text: glutathionylation
    is_a: molecular_modification
  glycation:
    text: glycation
    is_a: molecular_modification
  glycosylation:
    text: glycosylation
    is_a: molecular_modification
  glucuronidation:
    text: glucuronidation
    is_a: molecular_modification
  n_linked_glycosylation:
    text: n_linked_glycosylation
    is_a: molecular_modification
  o_linked_glycosylation:
    text: o_linked_glycosylation
    is_a: molecular_modification
  hydroxylation:
    text: hydroxylation
    is_a: molecular_modification
  lipidation:
    text: lipidation
    is_a: molecular_modification
  farnesylation:
    text: farnesylation
    is_a: molecular_modification
  geranoylation:
    text: geranoylation
    is_a: molecular_modification
  myristoylation:
    text: myristoylation
    is_a: molecular_modification
  palmitoylation:
    text: palmitoylation
    is_a: molecular_modification
  prenylation:
    text: prenylation
    is_a: molecular_modification
  methylation:
    text: methylation
    is_a: molecular_modification
  nitrosation:
    text: nitrosation
    is_a: molecular_modification
  nucleotidylation:
    text: nucleotidylation
    is_a: molecular_modification
  phosphorylation:
    text: phosphorylation
    is_a: molecular_modification
  ribosylation:
    text: ribosylation
    is_a: molecular_modification
  ADP-ribosylation:
    text: ADP-ribosylation
    is_a: molecular_modification
  sulfation:
    text: sulfation
    is_a: molecular_modification
  sumoylation:
    text: sumoylation
    is_a: molecular_modification
  ubiquitination:
    text: ubiquitination
    is_a: molecular_modification
  oxidation:
    text: oxidation
    is_a: molecular_modification
  reduction:
    text: reduction
    is_a: molecular_modification
  carboxylation:
    text: carboxylation
    is_a: molecular_modification

```
</details>
