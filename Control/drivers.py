import subprocess
import threading
import tkinter as tk
import os


def driver():
    interfaces = subprocess.check_output(
        "netsh interface show interface",
        shell=True
        ).decode("utf-8", errors="ignore")
    drivers = subprocess.check_output(
        "driverquery",
        shell=True
        ).decode("utf-8", errors="ignore")

    return interfaces + "\n" + drivers

PASTA_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAMINHO_ICO = os.path.join(PASTA_BASE, "Img", "icones", "logo.ico")


def abrir_janela_drivers(janela_pai):
    janela = tk.Toplevel(janela_pai)
    janela.title("Drivers")
    janela.geometry("600x500")

    janela.iconbitmap(CAMINHO_ICO)

    scrollbar = tk.Scrollbar(janela)
    scrollbar.pack(side="right", fill="y")

    caixa_texto = tk.Text(janela, wrap="none", yscrollcommand=scrollbar.set)
    caixa_texto.insert("1.0", "Carregando, aguarde...")
    caixa_texto.pack(fill="both", expand=True)

    scrollbar.config(command=caixa_texto.yview)

    def carregar():
        saida = driver()
        janela.after(0, atualizar_texto, saida)

    def atualizar_texto(saida):
        caixa_texto.delete("1.0", "end")
        caixa_texto.insert("1.0", saida)

    threading.Thread(target=carregar, daemon=True).start()