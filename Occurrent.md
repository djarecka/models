# Class: Occurrent


_A processual entity._





URI: [bican:Occurrent](https://identifiers.org/brain-bican/vocab/Occurrent)



```mermaid
 classDiagram
    class Occurrent
      PhysicalEssenceOrOccurrent <|-- Occurrent
      

      Occurrent <|-- ActivityAndBehavior
      Occurrent <|-- Phenomenon
      Occurrent <|-- EnvironmentalProcess
      Occurrent <|-- BiologicalProcessOrActivity
      Occurrent <|-- MolecularActivity
      Occurrent <|-- BiologicalProcess
      
      
      
```





## Inheritance
* [PhysicalEssenceOrOccurrent](PhysicalEssenceOrOccurrent.md)
    * **Occurrent**
        * [ActivityAndBehavior](ActivityAndBehavior.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |



## Mixin Usage

| mixed into | description |
| --- | --- |
| [Phenomenon](Phenomenon.md) | a fact or situation that is observed to exist or happen, especially one whose... |
| [EnvironmentalProcess](EnvironmentalProcess.md) |  |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | Either an individual molecular activity, or a collection of causally connecte... |
| [MolecularActivity](MolecularActivity.md) | An execution of a molecular function carried out by a gene product or macromo... |
| [BiologicalProcess](BiologicalProcess.md) | One or more causally connected executions of molecular functions |








## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bican:Occurrent |
| native | bican:Occurrent |
| exact | BFO:0000003 |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: occurrent
description: A processual entity.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- BFO:0000003
is_a: physical essence or occurrent
mixin: true

```
</details>

### Induced

<details>
```yaml
name: occurrent
description: A processual entity.
from_schema: https://identifiers.org/brain-bican/kb-model
exact_mappings:
- BFO:0000003
is_a: physical essence or occurrent
mixin: true

```
</details>