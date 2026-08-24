from PyPDF2 import PdfReader

# pdf = PdfReader("pdf/hinoNacionalCompleto2.pdf")
pdf = PdfReader("pdf/teste.pdf")

print("Número de páginas:", len(pdf.pages))

texto = ""
print("Texto extraído do PDF:\n")
for pagina in pdf.pages:
    texto += pagina.extract_text().lower() # .lower() is a Python method, not JavaScript, for js is to use .toLowerCase(), and java is to use .toLowerCase() as well, and php use strtolower() to convert a string to lowercase.

palavra = input("Digite uma palavra para buscar no texto extraído: ").lower()
if palavra in texto:
    posicao = texto.find(palavra)
    print(f"A palavra '{palavra}' foi encontrada na posição: {posicao}")
