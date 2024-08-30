current_movies = {"The Grinch": "11:00am",
                  "Elf": "1:00pm",
                  "Point Break": "3:30pm",
                  "Annie": "7:00pm"}

print("We're showing the following cool movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")
else:
    print(movie, "is playing at", showtime)