


current_movies = {'The grinch':'11:00am',
                  'Rudolph':'1:00pm',
                  'Frosty The Snowman':'3:00pm',
                  'Christmas Vacation':'5:00pm'}

print(' we are currently showing the following movies:')
for key in current_movies:
    print(key)

movie = input('What movie would you like to see the showtime for?\n')

show_time = current_movies.get(movie)
if show_time == None:
    print('requested movie is not playing.')
else:
    print(movie, 'is showing at', show_time)