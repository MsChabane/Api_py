from  json import load,dump
from os.path import join


def read_data():
    file =open(join('App','database','data.json'),'r')
    movies=load(file)['movies']
    file.close()
    return movies
def write_data(movies):
    data ={'movies':movies}
    file =open(join('App','database','data.json'),'w')
    dump(data,file,skipkeys=True)
    file.close() 

def get_all_movie():
    return read_data()     
    
def add_movie(movie):
    movies =read_data()
    movie['id']=len(movies)
    movies.append(movie)
    write_data(movies)
   
   
def find_movie(id,movies):
    for i,movie in enumerate(movies):
        if movie['id']== id :
            return i
        
def delete_movie(id):
    movies =read_data()
    index = find_movie(id,movies)
    if index != None :
        movie = movies.pop(index)
        write_data(movies)
        return movie      



def update_movie(movie,id):
    movies = read_data()
    print(movies)
    index = find_movie(id,movies)
    if index !=None:
        movie['id']=id
        movies[index]=movie
        write_data(movies)  
        return movie


def get_movie(id):
    movies = read_data()
    index = find_movie(id,movies)
    if index != None :
        return movies[index]
