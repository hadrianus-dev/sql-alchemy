from infra.repositories.film_repository import FilmRepository

repo = FilmRepository()
repo.insert("The Matrix Angolano", "Um filme de ação", "Ação", 1999)
repo.insert("Assalto Em Luanda", "Um filme de ação", "Ação", 2010)
print(repo.select())
print()

repo.update(9, "Ip Man", "Um filme de ação", "Ação", 2008)
print(repo.select())
print()

repo.delete(10)
print(repo.select())
