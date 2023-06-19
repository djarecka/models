# Subset: TranslatorMinimal


_Minimum subset of translator work_



URI: [TranslatorMinimal](TranslatorMinimal)





## Identifier and Mapping Information







### Schema Source


* from schema: https://identifiers.org/brain-bican/kb-model




## Classes in subset

| Class | Description |
| --- | --- |
| [ChemicalEntity](ChemicalEntity.md) | A chemical entity is a physical entity that pertains to chemistry or biochemi... |
| [ChemicalMixture](ChemicalMixture.md) | A chemical mixture is a chemical entity composed of two or more molecular ent... |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | A complex molecular mixture is a chemical mixture composed of two or more mol... |
| [Disease](Disease.md) | A disorder of structure or function, especially one that produces specific  s... |
| [EpigenomicEntity](EpigenomicEntity.md) |  |
| [Gene](Gene.md) | A region (or regions) that includes all of the sequence elements necessary to... |
| [GenomicEntity](GenomicEntity.md) |  |
| [MolecularEntity](MolecularEntity.md) | A molecular entity is a chemical entity composed of individual or covalently ... |
| [MolecularMixture](MolecularMixture.md) | A molecular mixture is a chemical mixture composed of two or more molecular e... |
| [NucleicAcidEntity](NucleicAcidEntity.md) | A nucleic acid entity is a molecular entity characterized by availability in ... |
| [SmallMolecule](SmallMolecule.md) | A small molecule entity is a molecular entity characterized by availability i... |


### ChemicalEntity

A chemical entity is a physical entity that pertains to chemistry or biochemistry.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md)  | Name of the high level ontology class in which this entity is categorized   |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md)  | a human-readable description of an entity   |
| [id](id.md) | 1..1 <br/> [String](String.md)  | A unique identifier for an entity **identifier**  |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md)  | A human-readable name for an attribute or entity   |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md)  | A database cross reference or alternative identifier for a NamedThing or edge...   |


### ChemicalMixture

A chemical mixture is a chemical entity composed of two or more molecular entities.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md)  | Name of the high level ontology class in which this entity is categorized   |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md)  | a human-readable description of an entity   |
| [id](id.md) | 1..1 <br/> [String](String.md)  | A unique identifier for an entity **identifier**  |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md)  | A human-readable name for an attribute or entity   |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md)  | A database cross reference or alternative identifier for a NamedThing or edge...   |


### ComplexMolecularMixture

A complex molecular mixture is a chemical mixture composed of two or more molecular entities with unknown concentration and stoichiometry.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md)  | Name of the high level ontology class in which this entity is categorized   |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md)  | a human-readable description of an entity   |
| [id](id.md) | 1..1 <br/> [String](String.md)  | A unique identifier for an entity **identifier**  |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md)  | A human-readable name for an attribute or entity   |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md)  | A database cross reference or alternative identifier for a NamedThing or edge...   |


### Disease

A disorder of structure or function, especially one that produces specific  signs, phenotypes or symptoms or that affects a specific location and is not simply a  direct result of physical injury.  A disposition to undergo pathological processes that exists in an  organism because of one or more disorders in that organism.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md)  | Name of the high level ontology class in which this entity is categorized   |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md)  | a human-readable description of an entity   |
| [id](id.md) | 1..1 <br/> [String](String.md)  | A unique identifier for an entity **identifier**  |
| [in_taxon](in_taxon.md) | 0..* <br/> [OrganismTaxon](OrganismTaxon.md)  | connects an entity to its taxonomic classification   |
| [in_taxon_label](in_taxon_label.md) | 0..1 <br/> [LabelType](LabelType.md)  | The human readable scientific name for the taxon of the entity   |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md)  | A human-readable name for an attribute or entity   |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md)  | A database cross reference or alternative identifier for a NamedThing or edge...   |


### EpigenomicEntity

None

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### Gene

A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md)  | Name of the high level ontology class in which this entity is categorized   |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md)  | a human-readable description of an entity   |
| [id](id.md) | 1..1 <br/> [String](String.md)  | A unique identifier for an entity **identifier**  |
| [in_taxon](in_taxon.md) | 0..* <br/> [OrganismTaxon](OrganismTaxon.md)  | connects an entity to its taxonomic classification   |
| [in_taxon_label](in_taxon_label.md) | 0..1 <br/> [LabelType](LabelType.md)  | The human readable scientific name for the taxon of the entity   |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [SymbolType](SymbolType.md)  | genes are typically designated by a short symbol and a full name   |
| [synonym](synonym.md) | 0..* <br/> [LabelType](LabelType.md)  | Alternate human-readable names for a thing   |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md)  | A database cross reference or alternative identifier for a NamedThing or edge...   |


### GenomicEntity

None

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |


### MolecularEntity

A molecular entity is a chemical entity composed of individual or covalently bonded atoms.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md)  | Name of the high level ontology class in which this entity is categorized   |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md)  | a human-readable description of an entity   |
| [id](id.md) | 1..1 <br/> [String](String.md)  | A unique identifier for an entity **identifier**  |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md)  | A human-readable name for an attribute or entity   |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md)  | A database cross reference or alternative identifier for a NamedThing or edge...   |


### MolecularMixture

A molecular mixture is a chemical mixture composed of two or more molecular entities with known concentration and stoichiometry.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md)  | Name of the high level ontology class in which this entity is categorized   |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md)  | a human-readable description of an entity   |
| [id](id.md) | 1..1 <br/> [String](String.md)  | A unique identifier for an entity **identifier**  |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md)  | A human-readable name for an attribute or entity   |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md)  | A database cross reference or alternative identifier for a NamedThing or edge...   |


### NucleicAcidEntity

A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md)  | Name of the high level ontology class in which this entity is categorized   |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md)  | a human-readable description of an entity   |
| [id](id.md) | 1..1 <br/> [String](String.md)  | A unique identifier for an entity **identifier**  |
| [in_taxon](in_taxon.md) | 0..* <br/> [OrganismTaxon](OrganismTaxon.md)  | connects an entity to its taxonomic classification   |
| [in_taxon_label](in_taxon_label.md) | 0..1 <br/> [LabelType](LabelType.md)  | The human readable scientific name for the taxon of the entity   |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md)  | A human-readable name for an attribute or entity   |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md)  | A database cross reference or alternative identifier for a NamedThing or edge...   |


### SmallMolecule

A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion).

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [category](category.md) | 1..* <br/> [CategoryType](CategoryType.md)  | Name of the high level ontology class in which this entity is categorized   |
| [description](description.md) | 0..1 <br/> [NarrativeText](NarrativeText.md)  | a human-readable description of an entity   |
| [id](id.md) | 1..1 <br/> [String](String.md)  | A unique identifier for an entity **identifier**  |
| [iri](iri.md) | 0..1 <br/> [IriType](IriType.md)  | An IRI for an entity   |
| [name](name.md) | 0..1 <br/> [LabelType](LabelType.md)  | A human-readable name for an attribute or entity   |
| [xref](xref.md) | 0..* <br/> [Uriorcurie](Uriorcurie.md)  | A database cross reference or alternative identifier for a NamedThing or edge...   |




## Slots in subset

| Slot | Description |
| --- | --- |
| [actively_involved_in](actively_involved_in.md) | holds between a continuant and a process or function, where the continuant ac... |
| [actively_involves](actively_involves.md) |  |
| [affects](affects.md) | describes an entity that has a direct affect on the state or quality of anoth... |
| [affects_response_to](affects_response_to.md) |  |
| [affects_risk_for](affects_risk_for.md) | holds between two entities where exposure to one entity alters the chance of ... |
| [anatomical_context_qualifier](anatomical_context_qualifier.md) | A statement qualifier representing an anatomical location where an relationsh... |
| [aspect_qualifier](aspect_qualifier.md) | Composes with the core concept to describe new concepts of a different ontolo... |
| [biomarker_for](biomarker_for.md) | holds between a measurable chemical entity and a disease or phenotypic featur... |
| [broad_match](broad_match.md) | a list of terms from different schemas or terminology systems that have a bro... |
| [capable_of](capable_of.md) | holds between a physical entity and process or function, where the continuant... |
| [category](category.md) | Name of the high level ontology class in which this entity is categorized |
| [causal_mechanism_qualifier](causal_mechanism_qualifier.md) | A statement qualifier representing a type of molecular control mechanism thro... |
| [caused_by](caused_by.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [causes](causes.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [chemically_similar_to](chemically_similar_to.md) | holds between one small molecule entity and another that it approximates for ... |
| [close_match](close_match.md) | a list of terms from different schemas or terminology systems that have a sem... |
| [coexists_with](coexists_with.md) | holds between two entities that are co-located in the same aggregate object, ... |
| [colocalizes_with](colocalizes_with.md) | holds between two entities that are observed to be located in the same place |
| [composed_primarily_of](composed_primarily_of.md) | x composed_primarily_of_y if:more than half of the mass of x is made from par... |
| [condition_associated_with_gene](condition_associated_with_gene.md) | holds between a gene and a disease or phenotypic feature that may be influenc... |
| [context_qualifier](context_qualifier.md) | Restricts the setting/context/location where the core concept (or qualified c... |
| [contributes_to](contributes_to.md) | holds between two entities where the occurrence, existence, or activity of on... |
| [contribution_from](contribution_from.md) |  |
| [correlated_with](correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [decreases_response_to](decreases_response_to.md) | holds between two chemical entities where the action or effect of one decreas... |
| [derivative_qualifier](derivative_qualifier.md) | A qualifier that composes with a core subject/object  concept to describe som... |
| [derives_from](derives_from.md) | holds between two distinct material entities, the new entity and the old enti... |
| [derives_into](derives_into.md) | holds between two distinct material entities, the old entity and the new enti... |
| [description](description.md) | a human-readable description of an entity |
| [direction_qualifier](direction_qualifier.md) | Composes with the core concept (+ aspect if provided) to describe a change in... |
| [disrupts](disrupts.md) | describes a relationship where one entity degrades or interferes with the str... |
| [enabled_by](enabled_by.md) | holds between a process and a physical entity, where the physical entity exec... |
| [enables](enables.md) | holds between a physical entity and a process, where the physical entity exec... |
| [exact_match](exact_match.md) | holds between two entities that have strictly equivalent meanings, with a hig... |
| [expressed_in](expressed_in.md) | holds between a gene or gene product and an anatomical entity in which it is ... |
| [expresses](expresses.md) | holds between an anatomical entity and gene or gene product that is expressed... |
| [food_component_of](food_component_of.md) | holds between a one or more chemical entities present in food, irrespective o... |
| [form_or_variant_qualifier](form_or_variant_qualifier.md) | A qualifier that composes with a core subject/object concept to define a spec... |
| [frequency_qualifier](frequency_qualifier.md) | a qualifier used in a phenotypic association to state how frequent the phenot... |
| [gene_associated_with_condition](gene_associated_with_condition.md) | holds between a gene and a disease or phenotypic feature that the gene or its... |
| [gene_product_of](gene_product_of.md) | definition x has gene product of y if and only if y is a gene (SO:0000704) th... |
| [gene_fusion_with](gene_fusion_with.md) | holds between two independent genes that have fused through  translocation, i... |
| [genetic_neighborhood_of](genetic_neighborhood_of.md) | holds between two genes located nearby one another on a chromosome |
| [genetically_associated_with](genetically_associated_with.md) |  |
| [genetically_interacts_with](genetically_interacts_with.md) | holds between two genes whose phenotypic effects are dependent on each other ... |
| [has_active_ingredient](has_active_ingredient.md) | holds between a drug and a molecular entity in which the latter is a part of ... |
| [has_biomarker](has_biomarker.md) | holds between a disease or phenotypic feature and a measurable chemical entit... |
| [has_excipient](has_excipient.md) | holds between a drug and a molecular entities in which the latter is a part o... |
| [has_food_component](has_food_component.md) | holds between food and one or more chemical entities composing it, irrespecti... |
| [has_gene_product](has_gene_product.md) | holds between a gene and a transcribed and/or translated product generated fr... |
| [has_input](has_input.md) | holds between a process and a continuant, where the continuant is an input in... |
| [has_member](has_member.md) | Defines a mereological relation between a collection and an item |
| [has_metabolite](has_metabolite.md) | holds between two molecular entities in which the second one is derived from ... |
| [has_mode_of_inheritance](has_mode_of_inheritance.md) | Relates a disease or phenotypic feature to its observed genetic segregation a... |
| [has_nutrient](has_nutrient.md) | one or more nutrients which are growth factors for a living organism |
| [has_output](has_output.md) | holds between a process and a continuant, where the continuant is an output o... |
| [has_part](has_part.md) | holds between wholes and their parts (material entities or processes) |
| [has_participant](has_participant.md) | holds between a process and a continuant, where the continuant is somehow inv... |
| [has_phenotype](has_phenotype.md) | holds between a biological entity and a phenotype, where a phenotype is const... |
| [has_plasma_membrane_part](has_plasma_membrane_part.md) | Holds between a cell c and a protein complex or protein p if and only if that... |
| [has_predisposing_factor](has_predisposing_factor.md) |  |
| [homologous_to](homologous_to.md) | holds between two biological entities that have common evolutionary origin |
| [id](id.md) | A unique identifier for an entity |
| [in_cell_population_with](in_cell_population_with.md) | holds between two genes or gene products that are expressed in the same cell ... |
| [in_complex_with](in_complex_with.md) | holds between two genes or gene products that are part of (or code for produc... |
| [in_pathway_with](in_pathway_with.md) | holds between two genes or gene products that are part of in the same biologi... |
| [in_taxon](in_taxon.md) | connects an entity to its taxonomic classification |
| [in_taxon_label](in_taxon_label.md) | The human readable scientific name for the taxon of the entity |
| [increases_response_to](increases_response_to.md) | holds between two chemical entities where the action or effect of one increas... |
| [interacts_with](interacts_with.md) | holds between any two entities that directly or indirectly interact with each... |
| [iri](iri.md) | An IRI for an entity |
| [is_active_ingredient_of](is_active_ingredient_of.md) | holds between a molecular entity and a drug, in which the former is a part of... |
| [is_exacerbated_by](is_exacerbated_by.md) |  |
| [is_excipient_of](is_excipient_of.md) | holds between a molecular entity and a drug in which the former is a part of ... |
| [is_input_of](is_input_of.md) |  |
| [is_metabolite_of](is_metabolite_of.md) | holds between two molecular entities in which the first one is derived from t... |
| [is_output_of](is_output_of.md) |  |
| [located_in](located_in.md) | holds between a material entity and a material entity or site within which it... |
| [location_of](location_of.md) | holds between material entity or site and a material entity that is located w... |
| [manifestation_of](manifestation_of.md) | that part of a phenomenon which is directly observable or visibly expressed, ... |
| [member_of](member_of.md) | Defines a mereological relation between a item and a collection |
| [model_of](model_of.md) | holds between a thing and some other thing it approximates for purposes of sc... |
| [name](name.md) | A human-readable name for an attribute or entity |
| [narrow_match](narrow_match.md) | a list of terms from different schemas or terminology systems that have a nar... |
| [negatively_correlated_with](negatively_correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [nutrient_of](nutrient_of.md) | holds between a one or more chemical entities present in food, irrespective o... |
| [object_aspect_qualifier](object_aspect_qualifier.md) |  |
| [object_context_qualifier](object_context_qualifier.md) |  |
| [object_derivative_qualifier](object_derivative_qualifier.md) |  |
| [object_direction_qualifier](object_direction_qualifier.md) |  |
| [object_form_or_variant_qualifier](object_form_or_variant_qualifier.md) |  |
| [object_part_qualifier](object_part_qualifier.md) |  |
| [occurs_in](occurs_in.md) | holds between a process and a material entity or site within which the proces... |
| [occurs_together_in_literature_with](occurs_together_in_literature_with.md) | holds between two entities where their co-occurrence is correlated by counts ... |
| [onset_qualifier](onset_qualifier.md) | a qualifier used in a phenotypic association to state when the phenotype appe... |
| [orthologous_to](orthologous_to.md) | a homology relationship between entities (typically genes) that diverged afte... |
| [overlaps](overlaps.md) | holds between entities that overlap in their extents (materials or processes) |
| [paralogous_to](paralogous_to.md) | a homology relationship that holds between entities (typically genes) that di... |
| [part_of](part_of.md) | holds between parts and wholes (material entities or processes) |
| [part_qualifier](part_qualifier.md) | defines a specific part/component of the core concept (used in cases there th... |
| [participates_in](participates_in.md) | holds between a continuant and a process, where the continuant is somehow inv... |
| [physically_interacts_with](physically_interacts_with.md) | holds between two entities that make physical contact as part of some interac... |
| [positively_correlated_with](positively_correlated_with.md) | A relationship that holds between two concepts represented by variables for w... |
| [preceded_by](preceded_by.md) | holds between two processes, where the other is completed before the one begi... |
| [precedes](precedes.md) | holds between two processes, where one completes before the other begins |
| [predisposes](predisposes.md) | holds between two entities where exposure to one entity increases the chance ... |
| [prevents](prevents.md) | holds between an entity whose application or use reduces the likelihood of a ... |
| [produces](produces.md) | holds between a material entity and a product that is generated through the i... |
| [qualifier](qualifier.md) | grouping slot for all qualifiers on an edge |
| [resource_id](resource_id.md) | The CURIE for an Information Resource that served as a source of knowledge ex... |
| [resource_role](resource_role.md) | The role played by the InformationResource in serving as a source for an Edge |
| [response_affected_by](response_affected_by.md) | holds between two chemical entities where the susceptibility of a biological ... |
| [response_decreased_by](response_decreased_by.md) |  |
| [response_increased_by](response_increased_by.md) |  |
| [retrieval_source_ids](retrieval_source_ids.md) | A list of retrieval sources that served as a source of knowledge expressed in... |
| [same_as](same_as.md) | holds between two entities that are considered equivalent to each other |
| [severity_qualifier](severity_qualifier.md) | a qualifier used in a phenotypic association to state how severe the phenotyp... |
| [sex_qualifier](sex_qualifier.md) | a qualifier used in a phenotypic association to state whether the association... |
| [similar_to](similar_to.md) | holds between an entity and some other entity with similar features |
| [species_context_qualifier](species_context_qualifier.md) | A statement qualifier representing a taxonomic category of species in which a... |
| [stage_qualifier](stage_qualifier.md) | stage during which gene or protein expression of takes place |
| [statement_qualifier](statement_qualifier.md) |  |
| [subclass_of](subclass_of.md) | holds between two classes where the domain class is a specialization of the r... |
| [subject_aspect_qualifier](subject_aspect_qualifier.md) |  |
| [subject_context_qualifier](subject_context_qualifier.md) |  |
| [subject_derivative_qualifier](subject_derivative_qualifier.md) |  |
| [subject_direction_qualifier](subject_direction_qualifier.md) |  |
| [subject_form_or_variant_qualifier](subject_form_or_variant_qualifier.md) |  |
| [subject_part_qualifier](subject_part_qualifier.md) |  |
| [superclass_of](superclass_of.md) | holds between two classes where the domain class is a super class of the rang... |
| [support_graphs](support_graphs.md) | A list of knowledge graphs that support the existence of this node |
| [synonym](synonym.md) | Alternate human-readable names for a thing |
| [treated_by](treated_by.md) | holds between a disease or phenotypic feature and a therapeutic process or ch... |
| [treats](treats.md) | holds between a therapeutic procedure or chemical entity and a disease or phe... |
| [xenologous_to](xenologous_to.md) | a homology relationship characterized by an interspecies (horizontal) transfe... |
| [xref](xref.md) | A database cross reference or alternative identifier for a NamedThing or edge... |


## Enumerations in subset

| Enumeration | Description |
| --- | --- |
| [ResourceRoleEnum](ResourceRoleEnum.md) | The role played by the information reource in serving as a source for an edge... |

