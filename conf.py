# -- Configuração do projeto -----------------------------------------------------
project = 'Uppertools'
copyright = '2024, Uppertools'
author = 'Uppertools'
release = '0.1'

# -- Configuração de Caminhos ---------------------------------------------------
# Se necessário, adicione aqui os diretórios de módulos, como mostrado abaixo:
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Configuração geral -------------------------------------------------------
extensions = []

# Diretório de templates (se houver)
templates_path = ['_templates']

# Idioma da documentação
language = 'pt_BR'

# Arquivos e diretórios a serem ignorados
exclude_patterns = []

# -- Configuração para a saída HTML -------------------------------------------

# Tema para a documentação HTML
html_theme = 'sphinx_rtd_theme'

# Caminho para arquivos estáticos (como imagens, CSS, etc.)
html_static_path = ['_static']

# Arquivos CSS personalizados
html_css_files = [
    'css/custom.css',  # Certifique-se de que o arquivo custom.css exista
]

# Remover o link de "Fonte" nas páginas
html_show_sourcelink = False

# Favicon configurado corretamente
html_favicon = 'img_logo/logo_grande/uppertools.ico'  # Verifique se o arquivo está no diretório _static
