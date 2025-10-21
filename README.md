# Relatorio-de-Atividades---Python-Notion
# Relatório de Atividades - Python + Notion

Este projeto em **Python** se conecta a uma base de dados do **Notion**, obtém as tarefas organizadas por prioridade e envia um **relatório diário por e-mail**.

---

## Funcionalidades

- Consulta uma base de dados do **Notion** usando a Notion API.
- Gera uma lista de tarefas com nome e categoria.
- Renderiza um relatório em HTML usando **Jinja2**.
- Envia o relatório por e-mail via **SMTP (Gmail)**.

---

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

EMAIL_SENHA=senha_do_email
NOTION_KEY=chave_de_api_do_notion
DATABASE_ID=id_da_base_de_dados
EMAIL_REMETENTE=seu_email@gmail.com
DESTINO=email_de_destino@gmail.com

---

## Instalação

1. Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

2. Instale as dependências:
pip install -r requirements.txt

---

## Execução

Execute o script principal:
python main.py ou python3 main.py

---

## Observação

- Use uma **senha de app** do Gmail, não a senha normal da conta.
- As tarefas devem estar organizadas no Notion com os campos:
  <img width="1054" height="262" alt="image" src="https://github.com/user-attachments/assets/dfb8007c-107f-40eb-9586-0031e931f8d0" />


---

## Autor

Feito por **xxxBIELxxx** 🇧🇷  
Estudante de Ciência da Computação.
