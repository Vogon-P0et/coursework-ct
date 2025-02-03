# module 2 lesson 1 Sets & lesson 2 Tuples

"""Create a list of your favorite hobbies, making sure to repeat a few of them.
Convert the list into a set to automatically remove the duplicates.
Print both the original list and the set to compare."""

# hobbies = ["reading", "gaming", "hiking", "gaming", "swimming", "hiking"]
# set_hobbies = set(hobbies)
# test_set = set()
# print(type(test_set))
# # test_set.add("driving")
# # print(test_set)
# test_set.add("running")
# print(test_set)

# print(hobbies)
# print(set_hobbies)

#----

# movies = ["Interstellar", "Half Baked", "The Matrix", "Fight Club", "Terminator", "The Professional", "The Princess Bride", "The Shining", "Pulp Fiction", "Dazed and Confused"]
# movie_set = set(movies)
# print(movie_set)

# print("The Matrix" in movie_set)

# print(movie_set)
# movie_set.add("Star Wars")
# print(movie_set)

# if "Pulp Fiction" in movie_set:
#     print("Pulp Fiction" in movie_set)
    
# movies = {"Interstellar", "Half Baked", "The Matrix", "Fight Club", "Terminator", "The Professional", "The Princess Bride", "The Shining", "Pulp Fiction", "Dazed and Confused"}

# movies_2 = {"Half Baked", "The Matrix", "Fight Club", "The Princess Bride", "The Shining", "Pulp Fiction", "Dazed and Confused"}

# print(movies.issubset(movies_2))
# print(movies.issuperset(movies_2))

# print(movies_2.issubset(movies))

# print("Interstellar" in movies)
# print("The Matrix" in movies)
# print("interstellar" in movies) #make sure use case sensitive chars

# movies.add("Back To The Future")
# print("Back To The Future" in movies)
# print(movies)
# print("-" * 30)

# print(movies.intersection(movies_2)) 
# print("-" * 30)

# print(movies.union(movies_2))
# print("-" * 30)

# print(movies.difference(movies_2))
# print("-" * 30)


# print("-" * 30)

# Final challenge
# fairytale race
# tuple_1 = ("john doe", "jane doe", "humpty dumpty", "little red riding hood", "shrek", "donkey")

# print(tuple_1[2])
# print(tuple_1[4])

# print(tuple_1[1:5])

# print(tuple_1.count("shrek"))
# print("-" * 30)
# first, second, third, *honorable_mention = tuple_1
# print(first)
# print(second)
# print(third)
# print(honorable_mention)

# ----------------------------------------------------------------

# module 2 lesson 3 Dictionaries

# book = {
#     "title": "The Hitchhikers Guide To The Galaxy",
#     "author": "Douglas Adams",
#     "year": 1979,
#     "genre": "Comic Sci-Fi"
# }

# book["Publisher"]= "Pan Books"
# print(book)

# print("-" * 30)

# book["year"]= 1942
# print(book)

# ----

# lesson 3 final challenge
# Write a program that takes a dictionary of students 👨‍🎓 and their grades, then prints 🖨️ each student's name and whether they passed ✅ or failed ❌ (consider passing as a grade ≥ 50).


students = {
    'Alice': 85,
    'Bob': 42,
    'Charlie': 68,
    'David': 49
}

for name, grade in students.items():
    if grade < 50:
        print(f"{name} has failed the course with a grade of {grade}.")
    else:
        print(f"{name} has passed the course with a grade of {grade}.")
        