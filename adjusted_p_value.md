# Slot: adjusted_p_value


_The adjusted p-value is the probability of obtaining test results at least as extreme as the results actually observed, under the assumption that the null hypothesis is correct, adjusted for multiple comparisons.   P is always italicized and capitalized. The actual P value* should be expressed (P=. 04)  rather than expressing a statement of inequality (P<. 05), unless P<._



URI: [bican:adjusted_p_value](https://identifiers.org/brain-bican/vocab/adjusted_p_value)




## Inheritance

* [association_slot](association_slot.md)
    * [p_value](p_value.md)
        * **adjusted_p_value**
            * [bonferonni_adjusted_p_value](bonferonni_adjusted_p_value.md)








## Properties

* Range: [Float](Float.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: adjusted p value
description: The adjusted p-value is the probability of obtaining test results at
  least as extreme as the results actually observed, under the assumption that the
  null hypothesis is correct, adjusted for multiple comparisons.   P is always italicized
  and capitalized. The actual P value* should be expressed (P=. 04)  rather than expressing
  a statement of inequality (P<. 05), unless P<.
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: p value
domain: association
alias: adjusted_p_value
range: float

```
</details>