from tkinter import *
from tkinter import filedialog, messagebox
import PyPDF2


def selecionar_pdf():
    # Abrir o diálogo para selecionar o arquivo PDF
    arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos PDF", "*.pdf")],
        title="Selecione o arquivo PDF"
    )
    if arquivo:
        # Abrir e ler o arquivo PDF
        with open(arquivo, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            texto_pdf = ""
            for page_num in range(len(pdf_reader.pages)):
                pagina = pdf_reader.pages[page_num]
                texto_pdf += pagina.extract_text()

        # Mostrar o texto extraído em uma nova janela ou no console
        mostrar_texto(texto_pdf)


def mostrar_texto(texto):
    # Criar uma nova janela para mostrar o texto
    nova_janela = Toplevel(janela)
    nova_janela.title("Texto do PDF")
    nova_janela.geometry("650x400")
    nova_janela.resizable(False, False)
    texto_widget = Text(nova_janela, wrap="word")
    texto_widget.insert(1.0, texto)
    texto_widget.pack(expand=True, fill='both')
    texto_widget.config(state=DISABLED)


# Configurar a janela principal
janela = Tk()
janela.title("PDF em Texto")
janela.geometry("300x150")
janela.resizable(False, False)

# Exibir saudação
def messagem():
    messagebox.showinfo("   Agora o Pix!", "Pix 73991507437")

# Configurar o layout centralizado
frame = Frame(janela)
frame.pack(expand=True)

texto = Label(frame, text="Clique no botão para selecionar o PDF")
texto.pack(pady=10)

botao = Button(frame, text="Selecionar", command=selecionar_pdf)
botao.pack(pady=10)
botao = Button(frame, text="Sobre", command=messagem)
botao.pack(pady=10)

# Iniciar o loop da janela
janela.mainloop()
