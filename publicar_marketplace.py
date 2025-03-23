import webbrowser as w
import pytesseract as pt
import pyautogui as pa
import keyboard as k
import time as t
import tkinter as tk
import os


def exibir_popup():
    # Cria a janela principal
    root = tk.Tk()

    # Define o título da janela
    root.title("Erro - Conta não logada!")

    # Configura o tamanho e as cores da janela
    root.geometry("550x200")  # Tamanho da janela
    root.configure(bg="white")  # Cor de fundo da janela

    # Centraliza a janela na tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()
    largura_janela = 550
    altura_janela = 200
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2
    root.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

    # Adiciona um texto ao popup
    label = tk.Label(root, text="Não é possível prosseguir pois a conta não está logada.\nPor favor faça o login da conta para continuar. Nova verificação em 1 minuto.",
                     bg="white", font=("Arial", 13))
    label.pack(pady=20)

    # Adiciona um botão para fechar
    botao_fechar = tk.Button(
        root, text="Fechar", command=root.destroy, bg="red", fg="white")
    botao_fechar.pack(pady=10)

    # Exibe a janela
    root.mainloop()


def verificar_facebook_logado():
    t.sleep(5)
    """Verifica se o facebook está logado no perfil antes de continuar"""
    tentativas = 0

    while True:
        imagem_tela = pa.screenshot()  # Tira print da tela

        texto = pt.image_to_string(imagem_tela)  # Extrai o que está escrito

        # Converte para texto com pytesseract
        texto = pt.image_to_string(imagem_tela)

        # Exibe o texto extraído no console - Usado para depuração
        # print(f"Texto extraído: {texto}")

        # Verifica se o texto específico está presente
        if "pensando" or 'Perfil Profissional' or 'Marketplace' or 'Grupos' or 'Feeds' in texto:
            print(f'Perfil está logado. Prosseguindo...')
            break
        else:
            print(
                f'Perfil não logado. Tentando novamente... ({tentativas + 1})')
            exibir_popup()
            t.sleep(60)  # Espera 60 segundos antes de tentar novamente
            tentativas += 1

            # Limite de tentativas para evitar loop infinito
            if tentativas >= 5:
                print(
                    "Erro: Não conseguiu verificar o login após 5 tentativas. Abortando.")
                break


def clicar_em(cx, cy):
    pa.click(x=cx, y=cy)


def encontrar_e_clicar(arquivo):
    t.sleep(2)
    botao = pa.locateOnScreen(arquivo, confidence=0.8)
    if botao:
        x, y = pa.center(botao)
        clicar_em(x, y)
        print(f"{arquivo} encontrado e clicado. {x},{y}")
        return True
    else:
        print(f"[ERRO] {arquivo} não encontrado!")
        return False


def entrar_marketplace():
    # Abre o Facebook no navegador padrão
    w.open("https://www.facebook.com")

    # Verifica se está logado
    verificar_facebook_logado()

    # Entrar no Marketplace
    t.sleep(2)  # Aguarda carregamento da página
    encontrar_e_clicar(
        r"C:/caminho/para/imagens/marketplace.png")  # Alterar caminho


def criar_classficado(i, caminho, titulo, preco, cores, marca, descricao, locais, retirada, entrega):
    # Criar Classificado
    encontrar_e_clicar(
        r"C:/caminho/para/imagens/novo.png")  # Alterar caminho
    encontrar_e_clicar(
        r"C:/caminho/para/imagens/item.png")  # Alterar caminho
    t.sleep(10)

    """Adicionar Fotos"""
    encontrar_e_clicar(
        r"C:/caminho/para/imagens/fotos.png")  # Alterar caminho

    # Clica na barra de pesquisa
    clicar_em(497, 530)

    img = caminho + '/imagem' + str(i)

    t.sleep(3)
    pa.write(img, interval=0.25)
    pa.press('enter')

    """Adicionar Título"""
    clicar_em(367, 484)
    t.sleep(3)
    pa.press('tab', 5, 1)
    pa.write(titulo)

    """Adicionar Preço"""
    t.sleep(1)
    pa.press('tab')
    pa.write(preco)

    """Adicionar Categoria"""
    t.sleep(1)
    pa.press('tab')
    pa.press('enter')
    encontrar_e_clicar(
        r"C:/caminho/para/imagens/moveis.png")  # Alterar caminho

    """Adicionar Condição"""
    t.sleep(1)
    pa.press('tab')
    pa.press('enter')
    encontrar_e_clicar(
        r"C:/caminho/para/imagens/cond_novo.png")  # Alterar caminho

    """Adicionar cor"""
    t.sleep(1)
    pa.press('tab', 4, 1)
    pa.write(cores)

    """Adicionar marca"""
    t.sleep(1)
    pa.press('tab')
    pa.write(marca)

    """Adicionar descrição"""
    t.sleep(1)
    pa.press('tab')
    k.write(descricao)
    t.sleep(10)

    """Adicionar tags"""
    t.sleep(1)
    pa.press('tab', 2, 1)
    pa.write('Beliche')
    pa.press('enter')
    pa.write('Treliche')
    pa.press('enter')
    pa.write('Cama')
    pa.press('enter')

    """Adicionar Locais"""
    pa.press('tab', 3, 1)
    k.write(locais[i])
    t.sleep(2)
    pa.press('down')
    pa.press('enter')

    """Adicionar Formas de Entrega"""
    if retirada:
        pa.press('tab', 4, 1)
        pa.press('enter')
    elif entrega:
        pa.press('tab', 5, 1)
        pa.press('enter')
    elif retirada and entrega:
        pa.press('tab', 4, 1)
        pa.press('enter')
        pa.press('tab')
        pa.press('enter')
    else:
        """Clicar em Avançar"""
        pa.press('tab', 12, 1)


# Variáveis Gerais - Ajuste de Caminho
caminho = r"C:/caminho/para/imagens"  # Alterar caminho
titulo = 'Seu título personalizado aqui'
preco = 'Valor do preço'
cores = 'Cores disponíveis'
marca = 'Sua marca'
descricao = 'Descrição detalhada do produto'

# Lista de locais de publicação
locais = ['Lista de cidades']

# Configurações adicionais
retirada = True
entrega = True
iniciar_em = 0
maximo_post = 10
tempo_espera = 20  # tempo entre cada publicação

entrar_marketplace()

for i in range(iniciar_em, maximo_post):
    criar_classficado(i, caminho, titulo, preco, cores, marca,
                      descricao, locais, retirada, entrega)

    # Publicar
    encontrar_e_clicar(
        r"C:/caminho/para/imagens/publicar.png")  # Alterar caminho

    """Aguardar antes de postar o próximo"""
    t.sleep(tempo_espera)
