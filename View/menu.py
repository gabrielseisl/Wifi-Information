import tkinter as tk
from Control.drivers import driver
from Control.user import user
from PIL import Image, ImageTk


def iniciar_menu():

    def abrir_drivers():
        driver()

    def abrir_user():
        user()

    janela = tk.Tk()
    janela.title("Wifi Information")
    janela.configure(bg="#FFFFFF")

    largura = 500
    altura = 600

    janela.geometry(f"{largura}x{altura}")

    janela.resizable(False, False)

    titulo = tk.Label(
        janela,
        text="Wifi Information",
        font=("Orbitron", 20),
        bg="#FFFFFF",
        fg="#0E0D0D"
    )

    titulo.pack(pady=(30,20))


    imagem_driver = Image.open("Img/wifi.png")
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


    imagem_user = Image.open("Img/pessoa.png")
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