# Arquivo de configuração para o gerador de documentação do Sphinx.
#
# Este arquivo contém apenas uma seleção das opções mais comuns. Para uma lista completa, veja a documentação:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Configuração de caminhos --------------------------------------------------------------

# Se extensões (ou módulos a serem documentados com autodoc) estiverem em outro diretório,
# adicione esses diretórios ao sys.path aqui. Se o diretório for relativo à raiz da documentação,
# use os.path.abspath para torná-lo absoluto, como mostrado aqui.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Informações do projeto -----------------------------------------------------

project = 'Uppertools'
copyright = '2024, Uppertools'
author = 'Uppertools'

# A versão completa, incluindo tags alpha/beta/rc
release = '0.1'


# -- Configuração geral ---------------------------------------------------

# Adicione aqui os nomes dos módulos de extensão do Sphinx, como strings. Eles podem ser
# extensões que vêm com o Sphinx (nomeados 'sphinx.ext.*') ou suas próprias.
extensions = [
]

# Adicione aqui qualquer caminho que contenha templates, relativo a este diretório.
templates_path = ['_templates']

# O idioma para conteúdo gerado automaticamente pelo Sphinx. Consulte a documentação
# para uma lista de idiomas suportados.
#
# Isso também é usado se você fizer tradução de conteúdo via catálogos gettext.
# Normalmente, você define "language" a partir da linha de comando para esses casos.
language = 'pt_BR'

# Lista de padrões, relativos ao diretório de origem, que correspondem a arquivos e
# diretórios a serem ignorados ao procurar por arquivos de origem.
# Esse padrão também afeta html_static_path e html_extra_path.
exclude_patterns = []


# -- Opções para a saída HTML -------------------------------------------------

# O tema a ser usado para páginas HTML e HTML Help. Veja a documentação para
# uma lista de temas incorporados.
#
html_theme = 'sphinx_rtd_theme'

# Adicione aqui qualquer caminho que contenha arquivos estáticos personalizados (como folhas de estilo), relativo a este diretório.
# Eles são copiados após os arquivos estáticos incorporados, então um arquivo chamado "default.css" substituirá o "default.css" incorporado.
html_static_path = ['_static']

# Inclua o arquivo CSS personalizado
html_css_files = [
    'custom.css',
]

# Remoção do botão "Ver código-fonte da página" da documentação.
html_show_sourcelink = False

# Inclusão do favicon
html_favicon = '/var/www/html/img_logo/logo_grande/uppertools.ico'


# Diretório para arquivos estáticos
html_static_path = ['_static']

# Arquivos CSS que devem ser incluídos
html_css_files = [
    'css/custom.css',
]
