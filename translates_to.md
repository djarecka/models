# Slot: translates_to


_x (amino acid chain/polypeptide) is the ribosomal translation of y (transcript) if and only if a ribosome reads y (transcript) through a series of triplet codon-amino acid adaptor activities (GO:0030533) and produces x (amino acid chain/polypeptide)_



URI: [bican:translates_to](https://identifiers.org/brain-bican/vocab/translates_to)




## Inheritance

* [related_to](related_to.md)
    * [related_to_at_instance_level](related_to_at_instance_level.md)
        * **translates_to**








## Properties

* Range: [Protein](Protein.md)

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
name: translates to
annotations:
  canonical_predicate:
    tag: canonical_predicate
    value: 'True'
description: x (amino acid chain/polypeptide) is the ribosomal translation of y (transcript)
  if and only if a ribosome reads y (transcript) through a series of triplet codon-amino
  acid adaptor activities (GO:0030533) and produces x (amino acid chain/polypeptide)
from_schema: https://identifiers.org/brain-bican/kb-model
close_mappings:
- RO:0002513
- SIO:010082
rank: 1000
is_a: related to at instance level
domain: transcript
multivalued: true
inherited: true
alias: translates_to
inverse: translation of
range: protein

```
</details>