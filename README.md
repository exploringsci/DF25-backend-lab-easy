# DF25-backend-lab-easy

## MongoDB Setup Steps (macOS): 
1. Install homebrew (if not already installed): https://brew.sh/

2. Install and start MongoDB service:
```
brew install mongodb-community
brew services start mongodb/brew/mongodb-community
```

3. Start MongoDB server:

`user@mac path % mongod`

4. Enter MongoDB shell:

`user@mac path % mongosh`

5. Create database, collection, and sample document

```
use movie_database

db.createCollection("movies")

db.movies.insertOne({
    title: "Upper West Side Story",
    year: 1337,
    producer: "DevFest 2025"
})
```
