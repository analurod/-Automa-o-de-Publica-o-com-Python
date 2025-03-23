# Automação de Publicação no Facebook Marketplace

## 📋 Descrição
Este projeto tem como objetivo automatizar a criação de anúncios no Facebook Marketplace através de automação de interface utilizando as bibliotecas **PyAutoGUI**, **PyTesseract**, **Keyboard**, **Tkinter**, e **Webbrowser**.

A automação:
- Verifica se o usuário está logado no Facebook.
- Entra no Marketplace.
- Cria anúncios automaticamente com base em variáveis pré-definidas e sem repetir as fotos.
- Adiciona fotos, título, preço, categoria, condição, cor, marca, descrição, tags, local e formas de entrega.

## 🎯 Motivação
A motivação para o desenvolvimento deste projeto surgiu a partir de uma necessidade real que encontrei enquanto realizava um trabalho freelance na área de vendas. Durante esse período, precisei fazer diversas publicações manuais no Facebook Marketplace e percebi o quanto o processo era repetitivo e cansativo. Com isso, surgiu a ideia de automatizar essas publicações, otimizando o tempo e tornando o processo mais eficiente. Além disso, estou atualmente aprendendo Python e estudando pelo livro Pense em Python, então o projeto também é uma oportunidade prática de aplicar o que venho aprendendo.

## ✅ Funcionalidades
- Verificação automática de login no Facebook utilizando OCR.
- Notificação via popup caso o login não esteja ativo.
- Criação automatizada de múltiplos anúncios.
- Inserção automática de imagens e preenchimento de campos.
- Configuração de local de venda e formas de entrega.

## 🛠 Tecnologias Utilizadas
- Python 3.11+
- PyAutoGUI
- PyTesseract
- Keyboard
- Tkinter
- Pillow
- Webbrowser

## 📂 Estrutura do Projeto
```
Automacao-com-python/
│
├─ controle_interface/
│   ├─ marketplace.png
│   ├─ novo.png
│   ├─ item.png
│   ├─ fotos.png
│   ├─ moveis.png
│   ├─ cond_novo.png
│
├─ publicar_marketplace.py  (script principal com automação)
├─ README.md
```

## ⚙️ Configuração Inicial
1. Clone ou baixe o repositório.
2. Certifique-se de ter o **Tesseract OCR** instalado e configurado no PATH.
3. Instale as dependências:
```bash
pip install pyautogui pytesseract keyboard pillow
```
4. No arquivo posicao.py, ajuste as variáveis de caminho e as imagens utilizadas de acordo com o seu ambiente local. **Importante:** o código está com caminhos genéricos e placeholders — é obrigatório alterá-los para refletirem seu próprio ambiente.
✅ Exemplo de configuração inicial no código:
```bash
# Caminho para pasta de imagens
caminho = r"C:/seu/caminho/para/imagens"

# Dados padrão do anúncio
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

```

## ▶️ Como usar
1. Execute o script `publicar_marketplace.py`.
2. O Facebook será aberto automaticamente.
3. O sistema verificará se você está logado. Caso não esteja, um popup será exibido e a automação tentará novamente após 1 minuto.
4. Uma vez logado, o processo de publicação será iniciado automaticamente.
5. O script publicará anúncios em sequência, conforme as informações configuradas.

## 📸 Observações Importantes
- As imagens de interface podem precisar ser atualizadas caso o layout do Facebook mude.
- Utilize a mesma resolução de tela usada na criação das imagens para evitar falhas na detecção.
- O sistema está preparado para até 5 tentativas de verificação de login antes de abortar.

## 👩‍💻 Autor
- Projeto criado por **Ana Luisa Rodrigues**.

## 💡 Contribuições
Contribuições são muito bem-vindas! Caso queira sugerir melhorias, abra uma issue ou envie um pull request.

---

> ⚠ **Atenção:** Esta automação é de uso pessoal. O uso comercial ou em desacordo com os termos de uso do Facebook é de total responsabilidade do usuário.

