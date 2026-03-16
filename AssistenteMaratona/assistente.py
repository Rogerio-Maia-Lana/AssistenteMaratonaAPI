import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


class AssistenteMaratona:

    def __init__(self):
        self.api_url = "http://www.omdbapi.com/"

    def buscar_serie(self, titulo):

        try:

            parametros = {
                "t": titulo,
                "apikey": API_KEY
            }

            resposta = requests.get(self.api_url, params=parametros)
            dados = resposta.json()

            if dados["Response"] == "False":
                return {
                    "titulo": titulo,
                    "erro": "Série não encontrada"
                }

            return {
                "titulo": dados["Title"],
                "ano": dados["Year"],
                "nota": dados["imdbRating"]
            }

        except Exception:
            return {
                "titulo": titulo,
                "erro": "Erro ao acessar API"
            }

    def buscar_lista_series(self):

        minha_lista = [
            "Breaking Bad",
            "Naruto",
            "SerieQueNaoExiste"
        ]

        resultados_finais = []

        for serie in minha_lista:
            resultado = self.buscar_serie(serie)
            resultados_finais.append(resultado)

        return resultados_finais