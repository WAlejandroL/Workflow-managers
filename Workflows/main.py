import requests
from prefect import flow, task

@task
def obtener_posts():
    url = "https://jsonplaceholder.cypress.io/posts"
    response = requests.get(url)
    return response.json()

@task
def contar_posts(posts):
    total = len(posts)
    print(f"Total de posts: {total}")
    return total

@task
def guardar_resultado(total):
    with open("resultado.txt", "w") as f:
        f.write(f"Total de posts: {total}")

@flow
def flujo_posts():
    posts = obtener_posts()
    total = contar_posts(posts)
    guardar_resultado(total)

if __name__ == "__main__":
    flujo_posts()