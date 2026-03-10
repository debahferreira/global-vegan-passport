from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to GlobalVegan Passport!"}

@app.get("/viagens")
async def listar_viagens():
    return {
        "cidades_visitadas": ["Lisboa", "Barcelona", "Madrid"],
        "favorito_vegan": "Honest Greens"
    }
