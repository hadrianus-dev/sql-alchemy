from src.infra.repositories import FilmRepository

repo = FilmRepository()
print(repo.select())
print()

repo.delete(10)
print(repo.select())
