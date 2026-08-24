from PyPDF2 import PdfReader
from pathlib import Path

from pathlib import Path
from PyPDF2 import PdfReader

def filesCounter(path):
    pasta = Path(path)
    arquivos_pdf = sorted(pasta.glob("*.csv"))

    return len(arquivos_pdf)

def filesAllPages(path):
    pasta = Path(path)
    arquivos_pdf = sorted(pasta.glob("*.doc"))

    paginas = []

    for arquivo in arquivos_pdf:
        pdf = PdfReader(arquivo)
        paginas.extend(pdf.pages)

    return paginas

def filesReader(path):
    pasta = Path(path)
    arquivos_pdf = sorted(pasta.glob(".pdf"))

    leitores = []

    for arquivos in arquivos_pdf:
        leitores.append(PdfReader(arquivo))

    return leitores