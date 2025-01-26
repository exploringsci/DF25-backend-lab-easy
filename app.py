from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from pymongo import MongoClient
app = FastAPI()

# MongoDB client and database setup
client = MongoClient("mongodb://localhost:27017/")
db = client["movie_database"]
movies_collection = db["movies"]

# Movie model
class Movie(BaseModel):
    title: str
    year: int
    producer: str

# Test endpoint
@app.get("/test")
async def test_endpoint():
    return {"message": "200 OK - The server is up and running."}

# Authentication model
class AuthRequest(BaseModel):
    username: str
    password: str

# Authentication endpoint
@app.post("/authenticate")
async def authenticate(auth_request: AuthRequest):
    # Replace with your desired username and password values
    VALID_USERNAME = "testuser"
    VALID_PASSWORD = "testpassword"

    if auth_request.username == VALID_USERNAME and auth_request.password == VALID_PASSWORD:
        return {"authenticated": True}
    else:
        return {"authenticated": False}

# Add movie
@app.post("/add_movie")
async def add_movie(movie: Movie):
    movie_data = movie.dict()
    result = movies_collection.insert_one(movie_data)
    if result.acknowledged:
        return {"message": "Movie added successfully.", "movie_id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Failed to add the movie.")

# Get movie
@app.get("/get_movie")
async def get_movie(title: str = Query(..., description="movie title")):
    movie = movies_collection.find_one({"title": title})
    if movie:
        movie.pop("_id", None) # This isn't relevant
        return movie
    else:
        raise HTTPException(status_code=404, detail="Movie not found.")