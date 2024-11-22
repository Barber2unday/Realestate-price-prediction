from pydantic import BaseModel

class realestatepricepredict(BaseModel):
    club_house: float
    school: float
    hospital: float
    mall: float
    park: float
    pool:float
    gym: float
    property_type: float
    property_area: float
    avg_price_by_subarea: float
    amenities_score: float
    avg_price_by_amenscore: float
    noun_count: float
    verb_count: float
    adjective_count: float
    boasts_elegant: float
    elegant_towers: float
    every_day: float
    great_community: float
    mantra_gold: float
    offering_bedroom: float
    quality_specification: float
    stories_offering: float
    towers_stories: float
    world_class: float