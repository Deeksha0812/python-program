import json
from collections import Counter
file= open("C:/Users/Darsh/OneDrive/Desktop/intern/movie.json","r")
x=file.read()
finaldata=json.loads(x)
for i in finaldata:
    print(i['title'])
print('-----------------------------')

for i in finaldata:
    if i['director']['first_name']=="Christopher" and i['director']['last_name']=="Nolan":
        print(i['title'])
print('---------------------------------')

movies_after_2000 = [i['title'] for i in finaldata if i['year'] > 2000]
print(movies_after_2000)
print('-----------------------------------')


genres = {genres for i in finaldata for genres in i['genres']}         
print(genres)
print('-------------------------------------')

directors = [i['director']['first_name']+" "+i['director']['last_name'] for i in finaldata]
print(directors)
print('------------------------------------')

movie_cast = {i['title']: [member['actor'] for member in i['cast']] for i in finaldata}
print(movie_cast)
print('--------------------------------------')

genre_count = Counter(genre for i in finaldata for genre in i['genres'])
print(genre_count)
print('--------------------------------------')

multi_genre_movies = [i['title'] for i in finaldata if len(i['genres']) > 1]
print(multi_genre_movies)
print('--------------------------------------')

actor_roles = {i['title']: [(member['actor'], member['role']) for member in i['cast']] for i in finaldata}
print(actor_roles)
print('--------------------------------------')

movies_90s = [i['title'] for i in finaldata if 1990 <= i['year'] <= 1999]
print(movies_90s)
print('--------------------------------------')

drama_movies = [i['title'] for i in finaldata if 'Drama' in i['genres']]
print(drama_movies)
print('--------------------------------------')


movies_with_years = [(i['title'], i['year']) for i in finaldata]
print(movies_with_years)
print('--------------------------------------')

