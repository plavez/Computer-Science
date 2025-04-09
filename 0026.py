movie_list = ["Interstellar", "Inception",
              "The Prestige", "Insomnia",
              "Batman Begins"]
ratings_list = [1, 10, 10, 8, 6]

production_years = [2015, 1999, 2022, 1995, 2018]

movies_ratings = list(zip(movie_list, ratings_list))
movies_product_years = list(zip(movie_list, production_years))
movies_complete_info = list(zip(movie_list, production_years, ratings_list))
test = list(zip(movie_list, movies_product_years))
# print(type(movies_ratings[0]))
print(movies_ratings)
# print(movies_product_years)
# print(movies_complete_info)
print(movies_ratings[1][0])
