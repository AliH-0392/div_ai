# "title", "director", "year", and "genre".

movie = {
    "title" : "The Batman 1989",
    "director" : "Tim Burton",
    "year" : 1989,
    "genre" : "Action"
}

movie["rating"] = 8.5
movie.pop("genre")
print(movie)