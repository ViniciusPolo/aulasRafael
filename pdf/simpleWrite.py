import copy
from PyPDF2 import PdfWriter, PdfReader, Transformation, Transformation
from filesCounter import filesCounter, filesReader

path = "pdf/samples"

total_files = filesCounter(path)
print("Número de arquivos:", total_files)

pdfs = filesReader(path)
try:
    watermark = PdfReader("pdf/Vinicius_Polo_Watermark.pdf")
    watermark_page = watermark.pages[0]
except FileNotFoundError:
    print("Arquivo de marca d'água não encontrado. Continuando sem marca d'água.")
    watermark_page = None


writer = PdfWriter()

print(f"Consolidando os PDFs em um único arquivo...\n\n")
newFileName = input("Digite o nome do arquivo consolidado (sem extensão): ")
print(input("Pressione Enter para iniciar a consolidação dos PDFs..."))

for i, pdf in enumerate(pdfs):
    print(f"Arquivo {i + 1}")
    print(f"Número de páginas: {len(pdf.pages)}")

    for page in pdf.pages:
        if watermark_page is not None:
            wm = copy.copy(watermark_page)
            wm.add_transformation(
                Transformation()
                .scale(0.15)
                .translate(5, 180) #(y=180 vertical, x=5 horizontal)
            )
            page.merge_page(wm)

        writer.add_page(page)

with open(f"{newFileName}.pdf", "wb") as output_file:
    writer.write(output_file)

print("PDF consolidado criado com sucesso!")