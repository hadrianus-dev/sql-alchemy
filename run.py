from infra.repositories.film_repository import FilmRepository

repo = FilmRepository()
print(repo.select())
print()

repo.delete(10)
print(repo.select())
