from PyPDF2 import PdfReader

pdf = PdfReader("pdf/teste.pdf")

print("Número de páginas:", len(pdf.pages))

texto = ""
print("Texto extraído do PDF:\n")
for pagina in pdf.pages:
    texto += pagina.extract_text()
palavra = input("Digite uma palavra para buscar no texto extraído: ")
if palavra in texto:
    posicao = texto.find(palavra)
    print(f"A palavra '{palavra}' foi encontrada na posição: {posicao}")
