# Flujo de Posts con Prefect

Este proyecto contiene un flujo de trabajo (workflow) implementado en Python usando la librería [Prefect](https://www.prefect.io/). El flujo principal se encuentra en el archivo `main.py` dentro de la carpeta `Workflows`.

## Descripción

El flujo realiza las siguientes tareas:

1. **Obtener posts:** Descarga una lista de posts desde la API pública https://jsonplaceholder.cypress.io/posts.
2. **Contar posts:** Cuenta el número total de posts obtenidos.
3. **Guardar resultado:** Escribe el total de posts en el archivo `resultado.txt` en la raíz del proyecto.

## Estructura del flujo

- `obtener_posts()`: Tarea Prefect que realiza una petición HTTP para obtener los posts.
- `contar_posts(posts)`: Tarea Prefect que cuenta la cantidad de posts recibidos.
- `guardar_resultado(total)`: Tarea Prefect que guarda el resultado en un archivo de texto.
- `flujo_posts()`: Define el flujo de Prefect que orquesta las tareas anteriores.

## Ejecución

1. Instala las dependencias necesarias:
   ```bash
   pip install prefect requests
   ```
2. Ejecuta el flujo desde la carpeta `Workflows`:
   ```bash
   python main.py
   ```
3. El resultado se guardará en el archivo `resultado.txt` en la raíz del proyecto.

## Notas
- El flujo utiliza Prefect 2.x (API moderna).
- El archivo `resultado.txt` se sobrescribe en cada ejecución.
- Puedes modificar la URL o las tareas según tus necesidades.

---

Autor: [Tu Nombre]
Fecha: Marzo 2026
