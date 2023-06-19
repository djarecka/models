# Slot: bonferonni_adjusted_p_value


_The Bonferroni correction is an adjustment made to P values when several dependent or independent  statistical tests are being performed simultaneously on a single data set. To perform a Bonferroni  correction, divide the critical P value (α) by the number of comparisons being made.  P is always italicized and  capitalized. The actual P value* should be expressed (P=. 04) rather than expressing a statement of inequality  (P<. 05), unless P<._



URI: [bican:bonferonni_adjusted_p_value](https://identifiers.org/brain-bican/vocab/bonferonni_adjusted_p_value)




## Inheritance

* [association_slot](association_slot.md)
    * [p_value](p_value.md)
        * [adjusted_p_value](adjusted_p_value.md)
            * **bonferonni_adjusted_p_value**








## Properties

* Range: [Float](Float.md)






## Examples

| Value |
| --- |
| 0.018 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## LinkML Source

<details>
```yaml
name: bonferonni adjusted p value
description: The Bonferroni correction is an adjustment made to P values when several
  dependent or independent  statistical tests are being performed simultaneously on
  a single data set. To perform a Bonferroni  correction, divide the critical P value
  (α) by the number of comparisons being made.  P is always italicized and  capitalized.
  The actual P value* should be expressed (P=. 04) rather than expressing a statement
  of inequality  (P<. 05), unless P<.
examples:
- value: '0.018'
from_schema: https://identifiers.org/brain-bican/kb-model
rank: 1000
is_a: adjusted p value
domain: association
alias: bonferonni_adjusted_p_value
range: float

```
</details>