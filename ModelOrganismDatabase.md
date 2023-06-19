# Subset: ModelOrganismDatabase


_Subset that is relevant for a typical Model Organism Database (MOD)_



URI: [ModelOrganismDatabase](ModelOrganismDatabase)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## Classes in subset

| Class | Description |
| --- | --- |
| [AnatomicalEntity](AnatomicalEntity.md) | A subcellular location, cell type or gross anatomical part |
| [Article](Article.md) | a piece of writing on a particular topic presented as a stand-alone  section ... |
| [Book](Book.md) | This class may rarely be instantiated except if use cases of a given knowledg... |
| [BookChapter](BookChapter.md) |  |
| [Disease](Disease.md) | A disorder of structure or function, especially one that produces specific  s... |
| [ExposureEvent](ExposureEvent.md) | A (possibly time bounded) incidence of a feature of the environment of an org... |
| [Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |
| [GeneFamily](GeneFamily.md) | any grouping of multiple genes or gene products related by common descent |
| [Genome](Genome.md) | A genome is the sum of genetic material within a cell or virion |
| [Genotype](Genotype.md) | An information content entity that describes a genome by specifying the total... |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | association between a named thing and a information content entity where the ... |
| [LifeStage](LifeStage.md) | A stage of development or growth of an organism, including post-natal adult s... |
| [MacromolecularComplex](MacromolecularComplex.md) | A stable assembly of two or more macromolecules, i |
| [MicroRNA](MicroRNA.md) |  |
| [NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |
| [OrganismTaxon](OrganismTaxon.md) | A classification of a set of organisms |
| [PhenotypicFeature](PhenotypicFeature.md) | A combination of entity and quality that makes up a phenotyping statement |
| [Polypeptide](Polypeptide.md) | A polypeptide is a molecular entity characterized by availability in protein ... |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | A collection of individuals from the same taxonomic class distinguished by on... |
| [Publication](Publication.md) | Any ‘published’ piece of information |
| [ReagentTargetedGene](ReagentTargetedGene.md) | A gene altered in its expression level in the context of some experiment as a... |
| [SequenceVariant](SequenceVariant.md) | A sequence_variant is a non exact copy of a sequence_feature or genome exhibi... |
| [Serial](Serial.md) | This class may rarely be instantiated except if use cases of a given knowledg... |
| [SiRNA](SiRNA.md) | A small RNA molecule that is the product of a longer exogenous or endogenous ... |
| [SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability i... |
| [Transcript](Transcript.md) | An RNA synthesized on a DNA or RNA template by an RNA polymerase |


### AnatomicalEntity

A subcellular location, cell type or gross anatomical part

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Article

a piece of writing on a particular topic presented as a stand-alone  section of a larger publication	  

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Book

This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### BookChapter

None

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Disease

A disorder of structure or function, especially one that produces specific  signs, phenotypes or symptoms or that affects a specific location and is not simply a  direct result of physical injury.  A disposition to undergo pathological processes that exists in an  organism because of one or more disorders in that organism.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### ExposureEvent

A (possibly time bounded) incidence of a feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Gene

A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### GeneFamily

any grouping of multiple genes or gene products related by common descent

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Genome

A genome is the sum of genetic material within a cell or virion.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Genotype

An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some established background

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### InformationContentEntityToNamedThingAssociation

association between a named thing and a information content entity where the specific context of the relationship between that named thing and the publication is unknown. For example, model organisms databases often capture the knowledge that a gene is found in a journal article, but not specifically the context in which that gene was documented in the article. In these cases, this association with the accompanying predicate 'mentions' could be used. Conversely, for more specific associations (like 'gene to disease association', the publication should be captured as an edge property).

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### LifeStage

A stage of development or growth of an organism, including post-natal adult stages

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### MacromolecularComplex

A stable assembly of two or more macromolecules, i.e. proteins, nucleic acids, carbohydrates or lipids, in which at least one component is a protein and the constituent parts function together.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### MicroRNA

None

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### NucleicAcidEntity

A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### OrganismTaxon

A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### PhenotypicFeature

A combination of entity and quality that makes up a phenotyping statement. An observable characteristic of an  individual resulting from the interaction of its genotype with its molecular and physical environment.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Polypeptide

A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### PopulationOfIndividualOrganisms

A collection of individuals from the same taxonomic class distinguished by one or more characteristics.  Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Publication

Any ‘published’ piece of information. Publications are considered broadly  to include any document or document part made available in print or on the  web - which may include scientific journal issues, individual articles, and  books - as well as things like pre-prints, white papers, patents, drug  labels, web pages, protocol documents,  and even a part of a publication if  of significant knowledge scope (e.g. a figure, figure legend, or section  highlighted by NLP). 

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### ReagentTargetedGene

A gene altered in its expression level in the context of some experiment as a result of being targeted by gene-knockdown reagent(s) such as a morpholino or RNAi.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### SequenceVariant

A sequence_variant is a non exact copy of a sequence_feature or genome exhibiting one or more sequence_alteration.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Serial

This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### SiRNA

A small RNA molecule that is the product of a longer exogenous or endogenous dsRNA, which is either a bimolecular duplex or very long hairpin, processed (via the Dicer pathway) such that numerous siRNAs accumulate from both strands of the dsRNA. SRNAs trigger the cleavage of their target molecules.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### SmallMolecule

A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion).

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Transcript

An RNA synthesized on a DNA or RNA template by an RNA polymerase.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |




## Slots in subset

| Slot | Description |
| --- | --- |


## Enumerations in subset

| Enumeration | Description |
| --- | --- |

