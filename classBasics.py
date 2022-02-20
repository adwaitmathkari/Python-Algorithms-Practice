class Movie(object):
    def __init__(self, name, actors, director):
        self.name = name
        self.actors = actors
        self.director = director
        self.noOfRatings = 0
        self.rating = 0

    def addRating(self, newRating):
        if(newRating>=0 and newRating<=5):
            self.noOfRatings += 1
            self.rating = round((self.rating*(self.noOfRatings-1)+ newRating)/self.noOfRatings, 2)
        else:
            print("rating needs to be between 0 to 5")


pk = Movie("pk", ["amir", "anushka", "sushant"], "raju hirani")

pk.addRating(3)
pk.addRating(4)
pk.addRating(4)
pk.addRating(2)
pk.addRating(5)
pk.addRating(5)
pk.addRating(5)
pk.addRating(7)
print(pk.rating, pk.name, pk.actors)