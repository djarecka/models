from __future__ import annotations
from datetime import datetime, date
from enum import Enum

from decimal import Decimal
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict,  Field, field_validator
import re
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra = 'forbid',
        arbitrary_types_allowed=True,
        use_enum_values = True)

    pass

        

class EntityView(ConfiguredBaseModel):
    """
    view of a specific entity
    """
    main_box: SummaryBox = Field(..., description="""summary of the box""")
    donor_box: Optional[DonorBox] = Field(None, description="""donor information""")
    species_box: Optional[SpeciesBox] = Field(None, description="""species information""")
    
    

class LAEntityView(EntityView):
    """
    view of a library aliquot
    """
    main_box: SummaryBox = Field(..., description="""summary of the box""")
    donor_box: DonorBox = Field(..., description="""donor information""")
    species_box: SpeciesBox = Field(..., description="""species information""")
    
    

class Box(ConfiguredBaseModel):
    """
    a general box
    """
    box_header: str = Field(..., description="""header of the box""")
    box_description: str = Field(..., description="""description of the box""")
    box_additional_info: Optional[AdditionalInfo] = Field(None, description="""additional information""")
    box_footer: Optional[str] = Field(None, description="""footer of the box""")
    
    

class SummaryBox(Box):
    """
    a summary box
    """
    local_name: Optional[str] = Field(None, description="""local name of teh entity""")
    category: Optional[str] = Field(None, description="""category of the entity""")
    box_header: str = Field(..., description="""it should be ID entity""")
    box_description: str = Field(..., description="""description of the box""")
    box_additional_info: Optional[AdditionalInfo] = Field(None, description="""additional information""")
    box_footer: Optional[str] = Field(None, description="""footer of the box""")
    
    

class DonorBox(Box):
    """
    donor information box
    """
    age_of_death_description: str = Field(...)
    age_of_death_point: str = Field(...)
    box_header: str = Field(..., description="""it should be donor id""")
    box_description: str = Field(..., description="""description of the box""")
    box_additional_info: Optional[AdditionalInfo] = Field(None, description="""additional information""")
    box_footer: Optional[str] = Field(None, description="""footer of the box""")
    
    

class SpeciesBox(Box):
    """
    species information box
    """
    local_species_name: str = Field(...)
    full_species_name: str = Field(...)
    species_taxonomy_id: str = Field(...)
    box_header: str = Field(..., description="""it should be species id""")
    box_description: str = Field(..., description="""description of the box""")
    box_additional_info: Optional[AdditionalInfo] = Field(None, description="""additional information""")
    box_footer: Optional[str] = Field(None, description="""footer of the box""")
    
    

class AdditionalInfo(ConfiguredBaseModel):
    """
    additional information
    """
    header: Optional[str] = Field(None)
    key_value_pairs: Optional[List[KeyValuePairs]] = Field(default_factory=list)
    
    

class KeyValuePairs(ConfiguredBaseModel):
    """
    key value pairs
    """
    key: str = Field(...)
    value: str = Field(...)
    
    


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
EntityView.model_rebuild()
LAEntityView.model_rebuild()
Box.model_rebuild()
SummaryBox.model_rebuild()
DonorBox.model_rebuild()
SpeciesBox.model_rebuild()
AdditionalInfo.model_rebuild()
KeyValuePairs.model_rebuild()

