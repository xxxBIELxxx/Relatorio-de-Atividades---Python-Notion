import requests
import os
from datetime import datetime
from pprint import pprint
from notion_client import Client
import smtplib
from email.message import EmailMessage
from jinja2 import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from dotenv import load_dotenv

load_dotenv()

EMAIL_SENHA = os.getenv('EMAIL_SENHA')
NOTION_KEY = os.getenv('NOTION_KEY')
DATABASE_ID = os.getenv('DATABASE_ID')
EMAIL_REMETENTE = os.getenv('EMAIL_REMETENTE')
DESTINO = os.getenv('DESTINO')

notion = Client(auth=NOTION_KEY)

def get_pages():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    headers = {
        "Authorization": f"Bearer {NOTION_KEY}",
        "Notion-Version": "2022-06-28",
        "accept": "application/json"
    }

    response = requests.post(url, headers=headers)
    if response.status_code != 200:
        print(f"Erro ao acessar a API do Notion: {response.status_code}")
        print(response.text)
        return []
    data = response.json()

    lista_tarefas = []
    
    for i in range(len(data.get("results"))):
        try: 
            nome_tarefa = data.get("results")[i].get("properties").get("Nome da tarefa").get("title")[0].get("text").get("content")

            categoria = data.get("results")[i].get("properties").get("Categoria").get("formula").get("string")

            tarefa = {
                "Tarefa" : f'{nome_tarefa}',
                "Categoria" : f'{categoria}' 
            }

            lista_tarefas.append(tarefa)
        except AttributeError:
            continue  
            
    return lista_tarefas



def send_email(dados):
    with open("template/index.html", encoding="utf-8") as f:
        template = Template(f.read())

        html_content = template.render(dados=dados)

    # --- Monta o e-mail ---
    msg = MIMEMultipart("alternative")
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = DESTINO
    msg["Subject"] = "Relatório de Tarefas"

    msg.attach(MIMEText(html_content, "html"))

    # --- Envia o e-mail ---
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_REMETENTE, EMAIL_SENHA)  # senha de app do Gmail
        server.send_message(msg)

    print("E-mail enviado com sucesso!")



def main():
    send_email(get_pages())


if __name__ == '__main__':
    main()
