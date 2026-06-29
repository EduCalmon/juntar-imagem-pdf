from fpdf import FPDF # Biblioteca que usei para criar o PDF
import os # Biblioteca para manipular arquivos do Sistema

pdf = FPDF() #Cria um PDF em branco essa função
pdf.set_auto_page_break(0)

imagens_pasta = os.listdir('img')

print("Gerando arquivo...")
for imagem in imagens_pasta:
    pdf.add_page()
    pdf.image('img\\' + imagem)
    

print("Salvando arquivo...")
nome_final = input("Digite o nome do arquivo final: ")    
if not nome_final.endswith(".pdf"):
    nome_final += ".pdf"

pdf.output(nome_final)

pdf.close() # Fecha o mesclador para liberar memória RAM

print("PDF Salvo!")