# Passo a Passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Repetir o processo de cadastro até acabar

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

# Passo 2: Fazer login

pyautogui.click(x=563, y=377)
pyautogui.write("emaildeteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.click(x=798, y=539)
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto

for linha in tabela.index:

    pyautogui.click(x=612, y=262)

    # Código do Produto
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    # Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # Preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    # Enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)