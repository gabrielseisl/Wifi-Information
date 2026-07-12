import tkinter as tk
import ctypes
import os
from Control.drivers import abrir_janela_drivers
from Control.user import user
from PIL import Image, ImageTk

# Caminho absoluto: sobe da pasta View até a raiz do projeto, onde fica Img
PASTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_ICO = os.path.join(PASTA_BASE, "Img", "logo.ico")

try:
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Wifi Information")
except Exception:
    pass


def iniciar_menu():
    def abrir_drivers():
        abrir_janela_drivers(janela)
    def abrir_user():
        user()

    janela = tk.Tk()

    if not os.path.exists(CAMINHO_ICO):
        print(f"[AVISO] Ícone não encontrado em: {CAMINHO_ICO}")
    else:
        try:
            janela.iconbitmap(CAMINHO_ICO)
        except tk.TclError as e:
            print(f"[ERRO] Falha ao carregar .ico: {e}")

    janela.title("Wifi Information")
    janela.configure(bg="#FFFFFF")
    largura = 500
    altura = 600
    janela.geometry(f"{largura}x{altura}")
    janela.resizable(False, False)

    # Logo dentro da janela
    imagem_logo = Image.open(CAMINHO_ICO)
    imagem_logo = imagem_logo.resize((80, 80))
    logo_icone = ImageTk.PhotoImage(imagem_logo)
    logo_label = tk.Label(janela, image=logo_icone, bg="#FFFFFF")
    logo_label.image = logo_icone
    logo_label.pack(pady=(20, 0))

    titulo = tk.Label(
        janela,
        text="Wifi Information",
        font=("Orbitron", 20),
        bg="#FFFFFF",
        fg="#0E0D0D"
    )
    titulo.pack(pady=(10,20))
    imagem_driver = Image.open(os.path.join(PASTA_BASE, "Img", "wifi.png"))
    imagem_driver = imagem_driver.resize((25,25))
    icone = ImageTk.PhotoImage(imagem_driver)
    botao_drivers = tk.Button(
        janela,
        text="Ver Drivers",
        image=icone,
        compound="left",
        bg="#000000",
        fg="white",
        command=abrir_drivers
    )
    botao_drivers.image = icone
    botao_drivers.place(x=40,y=200,width=180,height=50)
    imagem_user = Image.open(os.path.join(PASTA_BASE, "Img", "pessoa.png"))
    imagem_user = imagem_user.resize((25,25))
    icone2 = ImageTk.PhotoImage(imagem_user)
    botao_user = tk.Button(
        janela,
        text="Ver User",
        image=icone2,
        compound="left",
        bg="#000000",
        fg="white",
        command=abrir_user
    )
    botao_user.image = icone2
    botao_user.place(x=260,y=200,width=180,height=50)
    janela.mainloop()