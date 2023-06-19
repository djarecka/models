# Class: PathognomonicityQuantifier


_A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease_





URI: [bican:PathognomonicityQuantifier](https://identifiers.org/brain-bican/vocab/PathognomonicityQuantifier)



```mermaid
 classDiagram
    class PathognomonicityQuantifier
      SpecificityQuantifier <|-- PathognomonicityQuantifier
      
      
```





## Inheritance
* [RelationshipQuantifier](RelationshipQuantifier.md)
    * [SpecificityQuantifier](SpecificityQuantifier.md)
        * **PathognomonicityQuantifier**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:PathognomonicityQuantifier |
| native | bican:PathognomonicityQuantifier |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: pathognomonicity quantifier
description: A relationship quantifier between a variant or symptom and a disease,
  which is high when the presence of the feature implies the existence of the disease
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: specificity quantifier
mixin: true

```
</details>

### Induced

<details>
```yaml
name: pathognomonicity quantifier
description: A relationship quantifier between a variant or symptom and a disease,
  which is high when the presence of the feature implies the existence of the disease
from_schema: https://identifiers.org/brain-bican/kb-model
is_a: specificity quantifier
mixin: true

```
</details>