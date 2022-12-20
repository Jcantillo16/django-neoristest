import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from src.titulo_bancario.models import TituloBancario


def cargar_titulos():
    titulos = [
        {
            "idtitulo": "USD",
            "titulo": "DOLAR",
            "clasificacion": "DIV",
            "valor": 500000000,
            "fecha_creacion": "2022-03-14",
            "fecha_vencimiento": "2023-03-15",
            "pagocuota": "y"
        },
        {
            "idtitulo": "TRPV",
            "titulo": "TÍTULO DE PARTICIPACIÓN RENTA VARIABLE",
            "clasificacion": "DIV",
            "valor": 256000000,
            "fecha_creacion": "2022-08-25",
            "fecha_vencimiento": "2023-08-26",
            "pagocuota": "y"
        },
        {
            "idtitulo": "TP",
            "titulo": "TITULO DE PARTICIPACIÓN",
            "clasificacion": "DIV",
            "valor": 360000000,
            "fecha_creacion": "2022-02-16",
            "fecha_vencimiento": "2023-02-17",
            "pagocuota": "y"
        }
    ]
    for titulo in titulos:
        if not TituloBancario.objects.filter(idtitulo=titulo["idtitulo"]).exists():
            TituloBancario.objects.create(**titulo)
            print("Titulo creado: ", titulo["idtitulo"])
        else:
            print("El titulo ya existe")


if __name__ == "__main__":
    cargar_titulos()
