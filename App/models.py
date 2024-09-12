from pydantic import BaseModel




class Movie(BaseModel):
    title:str
    year_of_production:int
    rating:float
    
    
    
    

