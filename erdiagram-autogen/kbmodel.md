```mermaid
erDiagram
MappingCollection {

}
PredicateMapping {
    string mapped_predicate  
    string subject_aspect_qualifier  
    DirectionQualifierEnum subject_direction_qualifier  
    string subject_form_or_variant_qualifier  
    string subject_part_qualifier  
    string subject_derivative_qualifier  
    string subject_context_qualifier  
    predicate type predicate  
    string qualified_predicate  
    string object_aspect_qualifier  
    DirectionQualifierEnum object_direction_qualifier  
    string object_form_or_variant_qualifier  
    string object_part_qualifier  
    string object_derivative_qualifier  
    string object_context_qualifier  
    CausalMechanismQualifierEnum causal_mechanism_qualifier  
    string anatomical_context_qualifier  
}
NamedThing {
    stringList provided_by  
    uriorcurieList xref  
    string id  
    iri type iri  
    category typeList category  
    stringList type  
    label type name  
    narrative text description  
}
Attribute {
    label type name  
    iri type iri  
    string id  
    stringList provided_by  
    uriorcurieList xref  
    category typeList category  
    stringList type  
    narrative text description  
}
QuantityValue {
    unit has_unit  
    double has_numeric_value  
}
OntologyClass {
    string id  
}
OrganismTaxon {
    stringList provided_by  
    uriorcurieList xref  
    string id  
    iri type iri  
    category typeList category  
    stringList type  
    label type name  
    narrative text description  
}
AnnotationCollection {

}
GenomeAssembly {
    string id  
    string taxon  
    string version  
    string label  
    string description  
}
GenomeAnnotation {
    uriorcurie reference_assembly  
    string version  
    stringList content_url  
    biological sequence has_biological_sequence  
    string id  
    label type in_taxon_label  
    stringList provided_by  
    uriorcurieList xref  
    iri type iri  
    category typeList category  
    stringList type  
    label type name  
    narrative text description  
}
Checksum {
    DigestType checksum_algorithm  
    string value  
    string id  
    iri type iri  
    category typeList category  
    stringList type  
    label type name  
    narrative text description  
}
GeneAnnotation {
    BioType molecular_type  
    string symbol  
    label typeList synonym  
    uriorcurieList xref  
    biological sequence has_biological_sequence  
    string id  
    label type in_taxon_label  
    stringList provided_by  
    iri type iri  
    category typeList category  
    stringList type  
    symbol type name  
    narrative text description  
}

MappingCollection ||--}o PredicateMapping : "predicate mappings"
PredicateMapping ||--|o OrganismTaxon : "species context qualifier"
PredicateMapping ||--}o NamedThing : "exact match"
PredicateMapping ||--}o NamedThing : "narrow match"
PredicateMapping ||--}o NamedThing : "broad match"
NamedThing ||--}o Attribute : "has attribute"
Attribute ||--|| OntologyClass : "has attribute type"
Attribute ||--}o QuantityValue : "has quantitative value"
Attribute ||--|o NamedThing : "has qualitative value"
Attribute ||--}o Attribute : "has attribute"
OrganismTaxon ||--}o Attribute : "has attribute"
AnnotationCollection ||--}o GeneAnnotation : "annotations"
AnnotationCollection ||--}o GenomeAnnotation : "genome_annotations"
AnnotationCollection ||--}o GenomeAssembly : "genome_assemblies"
GenomeAnnotation ||--}| Checksum : "digest"
GenomeAnnotation ||--}o OrganismTaxon : "in taxon"
GenomeAnnotation ||--}o Attribute : "has attribute"
Checksum ||--}o Attribute : "has attribute"
GeneAnnotation ||--|o GenomeAnnotation : "referenced in"
GeneAnnotation ||--}o OrganismTaxon : "in taxon"
GeneAnnotation ||--}o Attribute : "has attribute"

```

