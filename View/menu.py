import tkinter as tk
from tkinter import messagebox
import ctypes

from Control.drivers import driver
from Control.user import user
from PIL import Image, ImageTk



#botão

def abrir_drivers():
    driver()

def abrir_user():
    user()


janela=tk.Tk()
janela.title("Wifi Information")
janela.configure(bg="#FFFFFF")

largura=500
altura=600

largura_tela = janela.winfo_screenheight()
altura_tela = janela.winfo_screenheight()
x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)

janela.geometry(f"{largura}x{altura}+{x}+{y}")

janela.resizable(False, False)


titulo=tk.Label(
    janela,
    text="Wifi Information",
    font=("Orbitron", 20),
    bg="#FFFFFF",
    fg="#0E0D0D"
)

titulo.pack(pady=(30, 20))


imagem_driver = Image.open("Img/wifi.png")
imagem_driver = imagem_driver.resize((25, 25))
icone = ImageTk.PhotoImage(imagem_driver)


botao_drivers = tk.Button(
    janela,
    text="Ver Drivers",
    image=icone,
    compound="left",
    font=("Segoe UI", 10, "bold"),
    bg="#000000",
    fg="white",
    relief="flat",
    cursor="hand2",
    command=abrir_drivers
)

botao_drivers.place(x=40, y=200, width=180, height=50)

imagem_driver = Image.open("Img/pessoa.png")
imagem_driver = imagem_driver.resize((25, 25))
icone2 = ImageTk.PhotoImage(imagem_driver)

botao_user = tk.Button(
    janela,
    text="Ver User",
    image=icone2,
    compound="left",
    font=("Segoe UI", 10, "bold"),
    bg="#000000",
    fg="white",
    relief="flat",
    cursor="hand2",
    command=abrir_user
)

botao_user.place(x=260, y=200, width=180, height=50)
janela.mainloop()