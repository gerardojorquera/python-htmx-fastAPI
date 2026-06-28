from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional

app = FastAPI(
    title="Proyecto usando FastApi",
    description="Proyecto desarrollando usando HTMX+FastAPI y Jinja2Templates",
    version="1.0.0"
)
templates = Jinja2Templates(directory="templates")
app.mount("/static" , StaticFiles(directory="static"), name="static")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/usuarios")
async def get_usuarios(request: Request):
    return templates.TemplateResponse(
        request,
        "partials/tabla_usuarios.html",
        {"usuarios": USUARIOS},
    )

# Endpoint para buscar dentro de la lista de usuarios
@app.get("/buscar")
async def buscar(
    request: Request, 
    q: Optional[str] = ""):
    """Permite la busqueda dentro del listado de usuarios siempre que cumpla con el criterio establecido
    - **q**: Parametro opcional con el criterio establecido
    """
    resultados = [
        usuario for usuario in USUARIOS
        if q.lower() in usuario["nombre"].lower() or q.lower() in usuario["rol"].lower()
    ]
    return templates.TemplateResponse(
        request,
        "partials/tabla_usuarios.html",
        {"usuarios": resultados},
    )

# Datos de ejemplo
USUARIOS = [
  {
    "id": 1,
    "nombre": "Angel Gomez",
    "rol": "Administrador"
  },
  {
    "id": 2,
    "nombre": "Olivia Sanchez",
    "rol": "Editor"
  },
  {
    "id": 3,
    "nombre": "Tomas Lopez",
    "rol": "Administrador"
  },
  {
    "id": 4,
    "nombre": "Clara Vargas",
    "rol": "Soporte Técnico"
  },
  {
    "id": 5,
    "nombre": "Camila Ruiz",
    "rol": "Visualizador"
  },
  {
    "id": 6,
    "nombre": "Elena Gonzalez",
    "rol": "Moderador"
  },
  {
    "id": 7,
    "nombre": "Diego Rivera",
    "rol": "Soporte Técnico"
  },
  {
    "id": 8,
    "nombre": "Andres Rivera",
    "rol": "Soporte Técnico"
  },
  {
    "id": 9,
    "nombre": "Luis Ramirez",
    "rol": "Soporte Técnico"
  },
  {
    "id": 10,
    "nombre": "Daniela Rodriguez",
    "rol": "Visualizador"
  },
  {
    "id": 11,
    "nombre": "Mateo Garcia",
    "rol": "Administrador"
  },
  {
    "id": 12,
    "nombre": "Lucas Castro",
    "rol": "Editor"
  },
  {
    "id": 13,
    "nombre": "Sara Ramirez",
    "rol": "Visualizador"
  },
  {
    "id": 14,
    "nombre": "Juan Salazar",
    "rol": "Editor"
  },
  {
    "id": 15,
    "nombre": "David Flores",
    "rol": "Editor"
  },
  {
    "id": 16,
    "nombre": "Gabriela Flores",
    "rol": "Administrador"
  },
  {
    "id": 17,
    "nombre": "Matias Contreras",
    "rol": "Moderador"
  },
  {
    "id": 18,
    "nombre": "Mateo Lopez",
    "rol": "Moderador"
  },
  {
    "id": 19,
    "nombre": "David Ruiz",
    "rol": "Editor"
  },
  {
    "id": 20,
    "nombre": "Luis Medina",
    "rol": "Visualizador"
  },
  {
    "id": 21,
    "nombre": "Martin Gomez",
    "rol": "Moderador"
  },
  {
    "id": 22,
    "nombre": "Diego Rivera",
    "rol": "Soporte Técnico"
  },
  {
    "id": 23,
    "nombre": "Tomas Ortiz",
    "rol": "Moderador"
  },
  {
    "id": 24,
    "nombre": "Benjamin Salazar",
    "rol": "Moderador"
  },
  {
    "id": 25,
    "nombre": "Diego Morales",
    "rol": "Visualizador"
  },
  {
    "id": 26,
    "nombre": "Felipe Vargas",
    "rol": "Moderador"
  },
  {
    "id": 27,
    "nombre": "Paula Ruiz",
    "rol": "Editor"
  },
  {
    "id": 28,
    "nombre": "Felipe Lopez",
    "rol": "Administrador"
  },
  {
    "id": 29,
    "nombre": "Juana Ruiz",
    "rol": "Administrador"
  },
  {
    "id": 30,
    "nombre": "Sofia Diaz",
    "rol": "Soporte Técnico"
  },
  {
    "id": 31,
    "nombre": "Mariana Flores",
    "rol": "Moderador"
  },
  {
    "id": 32,
    "nombre": "David Guzman",
    "rol": "Moderador"
  },
  {
    "id": 33,
    "nombre": "David Ramirez",
    "rol": "Editor"
  },
  {
    "id": 34,
    "nombre": "Matias Diaz",
    "rol": "Soporte Técnico"
  },
  {
    "id": 35,
    "nombre": "Samuel Garcia",
    "rol": "Moderador"
  },
  {
    "id": 36,
    "nombre": "Sebastian Ramirez",
    "rol": "Visualizador"
  },
  {
    "id": 37,
    "nombre": "Gabriel Martinez",
    "rol": "Soporte Técnico"
  },
  {
    "id": 38,
    "nombre": "Martina Guzman",
    "rol": "Soporte Técnico"
  },
  {
    "id": 39,
    "nombre": "Gabriel Salazar",
    "rol": "Soporte Técnico"
  },
  {
    "id": 40,
    "nombre": "Catalina Diaz",
    "rol": "Editor"
  },
  {
    "id": 41,
    "nombre": "Luis Alvarez",
    "rol": "Administrador"
  },
  {
    "id": 42,
    "nombre": "David Medina",
    "rol": "Soporte Técnico"
  },
  {
    "id": 43,
    "nombre": "Sebastian Gonzalez",
    "rol": "Visualizador"
  },
  {
    "id": 44,
    "nombre": "Nicolas Torres",
    "rol": "Visualizador"
  },
  {
    "id": 45,
    "nombre": "Clara Castro",
    "rol": "Moderador"
  },
  {
    "id": 46,
    "nombre": "Tomas Gomez",
    "rol": "Administrador"
  },
  {
    "id": 47,
    "nombre": "Elena Gonzalez",
    "rol": "Administrador"
  },
  {
    "id": 48,
    "nombre": "Gabriel Gomez",
    "rol": "Visualizador"
  },
  {
    "id": 49,
    "nombre": "Olivia Gomez",
    "rol": "Administrador"
  },
  {
    "id": 50,
    "nombre": "Martin Ramirez",
    "rol": "Visualizador"
  },
  {
    "id": 51,
    "nombre": "Diego Contreras",
    "rol": "Soporte Técnico"
  },
  {
    "id": 52,
    "nombre": "Valeria Silva",
    "rol": "Editor"
  },
  {
    "id": 53,
    "nombre": "Julian Gomez",
    "rol": "Moderador"
  },
  {
    "id": 54,
    "nombre": "Jose Torres",
    "rol": "Moderador"
  },
  {
    "id": 55,
    "nombre": "Felipe Vargas",
    "rol": "Visualizador"
  },
  {
    "id": 56,
    "nombre": "Alba Castro",
    "rol": "Moderador"
  },
  {
    "id": 57,
    "nombre": "Julian Gonzalez",
    "rol": "Administrador"
  },
  {
    "id": 58,
    "nombre": "Mateo Medina",
    "rol": "Soporte Técnico"
  },
  {
    "id": 59,
    "nombre": "Leonardo Muñoz",
    "rol": "Visualizador"
  },
  {
    "id": 60,
    "nombre": "Andres Rivera",
    "rol": "Moderador"
  },
  {
    "id": 61,
    "nombre": "Emiliano Alvarez",
    "rol": "Moderador"
  },
  {
    "id": 62,
    "nombre": "Valeria Muñoz",
    "rol": "Moderador"
  },
  {
    "id": 63,
    "nombre": "Santiago Flores",
    "rol": "Soporte Técnico"
  },
  {
    "id": 64,
    "nombre": "Matias Herrera",
    "rol": "Editor"
  },
  {
    "id": 65,
    "nombre": "Lucas Castro",
    "rol": "Administrador"
  },
  {
    "id": 66,
    "nombre": "Mariana Alvarez",
    "rol": "Soporte Técnico"
  },
  {
    "id": 67,
    "nombre": "Daniela Rodriguez",
    "rol": "Moderador"
  },
  {
    "id": 68,
    "nombre": "Santiago Gomez",
    "rol": "Visualizador"
  },
  {
    "id": 69,
    "nombre": "Felipe Castro",
    "rol": "Soporte Técnico"
  },
  {
    "id": 70,
    "nombre": "Catalina Diaz",
    "rol": "Visualizador"
  },
  {
    "id": 71,
    "nombre": "Mateo Garcia",
    "rol": "Administrador"
  },
  {
    "id": 72,
    "nombre": "Martin Salazar",
    "rol": "Editor"
  },
  {
    "id": 73,
    "nombre": "Diego Gomez",
    "rol": "Moderador"
  },
  {
    "id": 74,
    "nombre": "Felipe Herrera",
    "rol": "Administrador"
  },
  {
    "id": 75,
    "nombre": "Fernanda Vargas",
    "rol": "Soporte Técnico"
  },
  {
    "id": 76,
    "nombre": "Jose Castro",
    "rol": "Soporte Técnico"
  },
  {
    "id": 77,
    "nombre": "Martin Lopez",
    "rol": "Soporte Técnico"
  },
  {
    "id": 78,
    "nombre": "Valentina Ortiz",
    "rol": "Editor"
  },
  {
    "id": 79,
    "nombre": "Matias Alvarez",
    "rol": "Visualizador"
  },
  {
    "id": 80,
    "nombre": "Andres Rios",
    "rol": "Visualizador"
  },
  {
    "id": 81,
    "nombre": "Sofia Gomez",
    "rol": "Moderador"
  },
  {
    "id": 82,
    "nombre": "Jose Vargas",
    "rol": "Visualizador"
  },
  {
    "id": 83,
    "nombre": "Felipe Salazar",
    "rol": "Administrador"
  },
  {
    "id": 84,
    "nombre": "Lucia Morales",
    "rol": "Moderador"
  },
  {
    "id": 85,
    "nombre": "David Diaz",
    "rol": "Administrador"
  },
  {
    "id": 86,
    "nombre": "Luis Alvarez",
    "rol": "Moderador"
  },
  {
    "id": 87,
    "nombre": "Diego Rivera",
    "rol": "Editor"
  },
  {
    "id": 88,
    "nombre": "Juan Ortiz",
    "rol": "Moderador"
  },
  {
    "id": 89,
    "nombre": "Isabella Ortiz",
    "rol": "Soporte Técnico"
  },
  {
    "id": 90,
    "nombre": "Felipe Morales",
    "rol": "Visualizador"
  },
  {
    "id": 91,
    "nombre": "Alba Morales",
    "rol": "Editor"
  },
  {
    "id": 92,
    "nombre": "Mateo Medina",
    "rol": "Moderador"
  },
  {
    "id": 93,
    "nombre": "Santiago Gomez",
    "rol": "Soporte Técnico"
  },
  {
    "id": 94,
    "nombre": "Felipe Morales",
    "rol": "Moderador"
  },
  {
    "id": 95,
    "nombre": "Diego Flores",
    "rol": "Soporte Técnico"
  },
  {
    "id": 96,
    "nombre": "Sofia Rojas",
    "rol": "Administrador"
  },
  {
    "id": 97,
    "nombre": "Clara Rodriguez",
    "rol": "Soporte Técnico"
  },
  {
    "id": 98,
    "nombre": "Alba Castro",
    "rol": "Soporte Técnico"
  },
  {
    "id": 99,
    "nombre": "Tomas Flores",
    "rol": "Moderador"
  },
  {
    "id": 100,
    "nombre": "Sebastian Lopez",
    "rol": "Editor"
  }
]