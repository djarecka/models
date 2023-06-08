# CCN2



URI: CCN2

Name: CCN2



## Classes

| Class | Description |
| --- | --- |
| [CellSetAccessionToCellMapping](CellSetAccessionToCellMapping.md) | None |
| [CrossTaxonomyMapping](CrossTaxonomyMapping.md) | None |
| [LocationMapping](LocationMapping.md) | None |
| [Taxonomy](Taxonomy.md) | None |



## Slots

| Slot | Description |
| --- | --- |
| [cell_accessions](cell_accessions.md) | List of cell set accession identifiers |
| [cell_set_accession](cell_set_accession.md) | Primary identifier for cell set |
| [cell_type_name](cell_type_name.md) | The primary name/symbol to be used for the cell type defined by this cell set |
| [classification_comment](classification_comment.md) | A free text comment describing the evidence for this classification |
| [classification_provenance](classification_provenance.md) | Either the DOI(s) of a supporting publication (in the form the form doi:10 |
| [classifying_ontology_term_id](classifying_ontology_term_id.md) | The ID of an ontology term that classifies the cell type defined by this node |
| [classifying_ontology_term_name](classifying_ontology_term_name.md) | The name of the ontology term in the classification_id column |
| [description](description.md) | Optional free text description of the cluster |
| [evidence_comment](evidence_comment.md) | A free text description of the evidence |
| [location_ontology_term_id](location_ontology_term_id.md) | The ID of an ontology term that refers to a brain region that this cell type ... |
| [location_ontology_term_name](location_ontology_term_name.md) | Name of the term whose ID is recorded in the ontology_term_id field |
| [mapped_cell_set_accession](mapped_cell_set_accession.md) | The accession (ID) of a cell set in a second taxonomy that this cell set maps... |
| [mapped_cell_type_name](mapped_cell_type_name.md) | The name of the cell type corresponding to the mapped_cell_set_accession |
| [parent_cell_set_accession](parent_cell_set_accession.md) | The cell set accession of the parent cell set in the taxonomy |
| [provenance](provenance.md) | ORCID of the person doing the mapping using the syntax ORCID:0123-4567-890 |
| [rank](rank.md) | Algorithmically generated hierarchical taxonomies can be complex, with many n... |
| [sample](sample.md) | Cell sample identifier |
| [similarity_score](similarity_score.md) | A score recording the similarity between mapped nodes |
| [supporting_data](supporting_data.md) | A link to data supporting this location mapping |
| [synonym_provenance](synonym_provenance.md) | Each entry in the synonyms field should have a corresponding entry here, eith... |
| [synonyms](synonyms.md) | A list of alternative names for this cell type |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [Rank](Rank.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
