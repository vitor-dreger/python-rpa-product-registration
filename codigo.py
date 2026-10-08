# Passo 1: Entrar no sistema/site da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui = biblioteca de automatização de tarefas
# time = biblioteca para controle de tempo de tarefas em diferentes momentos
# pandas = biblioteca para trabalho com bases de dados
# python-dotenv = biblioteca para carregar credenciais de um arquivo .env (fora do código)
import os
import pyautogui
import time
import pandas
from dotenv import load_dotenv

load_dotenv()
LOGIN_EMAIL = os.environ["AUTOMACAO_LOGIN_EMAIL"]
LOGIN_SENHA = os.environ["AUTOMACAO_LOGIN_SENHA"]

# pyautogui.write -> escrever texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho de teclado (Ctrl, C)
# pyautogui.PAUSE -> Tempo de pausa declarado a cada comando

pyautogui.PAUSE = 0.4
# abrir o navegador
# apertar tecla windows
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# pausa EXCLUSIVA de 1.7 segundos
time.sleep(1.7)

# click na barra de login
pyautogui.click(x=739, y=510)
# Passo 2: Fazer Login
pyautogui.write(LOGIN_EMAIL)
pyautogui.press("tab")
pyautogui.write(LOGIN_SENHA)
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
linha = 0
# para cada linha da tabela
for linha in tabela.index:

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.click(x=652, y=356)
    pyautogui.write(str(codigo))

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.press("tab")
    pyautogui.write(str(marca))

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.press("tab")
    pyautogui.write(str(tipo))

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.press("tab")
    pyautogui.write(str(categoria))

    # preco unitario
    precoUnitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.press("tab")
    pyautogui.write(str(precoUnitario))

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.press("tab")
    pyautogui.write(str(custo))

    # obs
    obs = tabela.loc[linha, "obs"]
    pyautogui.press("tab")
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # clicar em enviar
    pyautogui.press("enter")
    pyautogui.press("home")
