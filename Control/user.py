import tkinter as tk
import subprocess
import os
PASTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_ICO = os.path.join(PASTA_BASE, "Img", "logo.ico")

def mostrar_janela(janela_principal, mensagem):
    janela = tk.Toplevel(janela_principal)
    janela.title("Wifi Information")
    janela.iconbitmap(CAMINHO_ICO)
    janela.geometry("300x120")
    janela.resizable(False, False)

    tk.Label(
        janela,
        text=mensagem,
        font=("Segoe UI", 11)
    ).pack(pady=20)

    tk.Button(
        janela,
        text="OK",
        command=janela.destroy
    ).pack()


def user(janela_principal):
    try:
        resultado = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True,
            stderr=subprocess.STDOUT
        ).decode("utf-8", errors="ignore")

        ssid = None

        for linha in resultado.split("\n"):
            if "SSID" in linha and "BSSID" not in linha:
                ssid = linha.split(":")[1].strip()
                break

        if ssid:
            mostrar_janela(
                janela_principal,
                f"Conectado à rede:{ssid}"
            )
        else:
            mostrar_janela(
                janela_principal,
                "Nenhuma rede Wi-Fi conectada."
            )

    except subprocess.CalledProcessError:
        mostrar_janela(
            janela_principal,
            "Nenhum adaptador Wi-Fi encontrado."
        )