

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}


# עבודה עם- set

#a הוספת איבר בודד לסט
oscar_winners.add("Emma Watson")
print("a", oscar_winners)

#b העתק הסט, מחקת איבר, ומחיקת בסט
copy_oscar_winners = oscar_winners.copy()
copy_oscar_winners.remove("Meryl Streep")
print("b", copy_oscar_winners.clear())

#c המשותף לשתי הסטים
result = titanic_actors.intersection(dark_knight_actors)
result_ = titanic_actors & dark_knight_actors
print("c", result)
print("c", result_)

#d המשותף לשתי הסטים
result = iron_man_actors.intersection(avengers_actors)
result_ = iron_man_actors & avengers_actors
print("d", result)
print("d", result_)

#e האם הסט הראשון נכלל בשני
result = actor_list.issubset(oscar_winners)
result_ = actor_list <= oscar_winners
print("e", result)
print("e", result_)

#f האם הסט הראשון נכלל בשני
result = avengers_actors.issubset(actor_list)
result_ = avengers_actors <= actor_list
print("f", result)
print("f", result_)

#g הסרת איבר אקראי מהקבוצה
print("g", movie_cast.pop())

#h הסרת איבר ללא שגיאה אם אינו נמצא
movie_cast.discard("Matt Damon")

#i אילו איברים מופיעים בקבוצה הראשונה אך לא בשניה
titanic_actors_not_winners = titanic_actors.difference(oscar_winners)
print("i", titanic_actors_not_winners)
print("i", titanic_actors - oscar_winners)

#j אילו איברים מופיעים רק באחת הקבוצות
print("j", titanic_actors.symmetric_difference(dark_knight_actors))
print("j", titanic_actors ^ dark_knight_actors)

#k הוספת כמה איברים לקבוצה
oscar_winners.update(["Cate Blanchett", "Daniel Lewis-Day"])
print("k", oscar_winners)

#l איחוד הקבוצות
print("l", titanic_actors.union(dark_knight_actors))
union_actor = titanic_actors | dark_knight_actors
print("l", union_actor)
