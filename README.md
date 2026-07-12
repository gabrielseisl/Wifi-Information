WiFi Information
Esse projeto foi feito em Python pra treinar criação de interface gráfica, consulta de comandos do Windows em segundo plano e manipulação de ícones.

O que ele faz
Mostra informações da rede Wi-Fi conectada (como o SSID)

Lista as interfaces de rede e drivers instalados no computador

Carrega os dados dos drivers usando threads pra interface não travar

Interface feita com Tkinter e estilizada para Windows

Como rodar:
Primeiro instala as dependências:

Bash
python -m pip install pillow
Depois é só executar:

Bash
python View/main.py
Organização do projeto
Control → onde ficam as funções de busca de drivers e dados do Wi-Fi (drivers.py e user.py)

View → onde fica a interface do aplicativo (main.py)

Img → onde ficam os ícones e a logo (logo.ico, wifi.png, pessoa.png)

Sobre
Projeto feito pra estudo de Python, Tkinter, comandos nativos do sistema (netsh, driverquery) e threads
