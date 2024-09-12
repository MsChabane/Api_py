from fastapi import FastAPI,HTTPException,status
from uvicorn import run
from .models import Movie
from .database.DB_server import get_all_movie,add_movie,update_movie,delete_movie,get_movie

app=FastAPI()

@app.get('/api/movies')
def get_movies_():
    movies =get_all_movie()
    return {"data": movies}


@app.get('/api/movies/{id}')
def get_movie_by_id_(id:int):
    movie = get_movie(id=id)
    if movie == None :
        return HTTPException(status_code=404,detail=f'movie of id {id} was not found')
    return {"data": movie}

@app.post('/api/movies')
def create_movie_(movie:Movie):
    movie_created = add_movie(movie=movie.dict())
    return movie_created


@app.put('/api/movies/{id}')
def update_movie_(id:int,movie:Movie):
    movie_updated = update_movie(id=id,movie=movie.dict())
    if movie_updated == None :
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='movie was not exist')
    return movie_updated

@app.delete('/api/movies/{id}')
def delete_movie_(id:int):
    movie = delete_movie(id=id)
    print(movie)
    if movie == None :
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="movie was not exist")
    return {"message":f"{movie} was deleted"}





  
    
    
    







































