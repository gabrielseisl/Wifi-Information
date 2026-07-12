# WiFi Information

![Tela do aplicativo](Img/logo.ico)

## Sobre o projeto

O **WiFi Information** é uma aplicação desenvolvida em Python com foco em aprendizado de desenvolvimento desktop, interfaces gráficas e integração com comandos nativos do Windows.

O projeto permite visualizar informações da rede Wi-Fi e consultar detalhes sobre interfaces e drivers de rede instalados no computador, utilizando uma interface simples e intuitiva construída com Tkinter.

## Funcionalidades

* Exibe informações da rede Wi-Fi conectada, como o SSID.
* Lista as interfaces de rede disponíveis no sistema.
* Exibe os drivers instalados no computador.
* Executa consultas em segundo plano utilizando **threads**, evitando o travamento da interface.
* Interface gráfica desenvolvida com **Tkinter** e adaptada para o ambiente Windows.

## Tecnologias utilizadas
* Tkinter
* Pillow (PIL)
* Threading
* Comandos nativos do Windows (`netsh` e `driverquery`)


<div style="display: flex; align-items: center;">
  <img src="Img/py.png" width="300">
  <div style="margin-left: 20px;">
    <h1>WiFi Information</h1>
    <p>
      Aplicação desenvolvida em Python para consultar informações de rede e drivers do sistema.
    </p>
  </div>
</div>

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Wifi-Information.git
```

Instale as dependências:

```bash
python -m pip install pillow
```

## Como executar

```bash
python View/main.py
```

## Estrutura do projeto

```text
Wifi-Information/
├── Control/
│   ├── drivers.py
│   └── user.py
├── View/
│   └── main.py
├── Img/
│   ├── logo.ico
│   ├── wifi.png
│   ├── pessoa.png
│   └── screenshot.png
└── README.md
```

## Objetivo

Este projeto foi desenvolvido com fins educacionais para praticar:

* Desenvolvimento de interfaces gráficas com Tkinter;
* Manipulação de imagens e ícones;
* Execução de comandos do sistema operacional;
* Programação com threads;
* Organização de projetos em Python.

---

Desenvolvido por Gabriel Seisl.
