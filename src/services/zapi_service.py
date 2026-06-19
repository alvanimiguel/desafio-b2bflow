import requests
import json
from src.config import (
    ZAPI_INSTANCE_ID,
    ZAPI_TOKEN,
    CLIENT_TOKEN
)

def send_message(phone: str, message: str) -> dict:
    # envia uma mensagem de texto para um número de telefone via endpoint da z-api.
    # retorna:
        # dict: um dicionário contendo o status do envio ('success'), o código HTTP ('status_code') e a resposta da api ('response')

    # montagem da url de destino utilizando as variáveis de instância e token
    url = (
        f"https://api.z-api.io/instances/"
        f"{ZAPI_INSTANCE_ID}/token/"
        f"{ZAPI_TOKEN}/send-text"
    )

    # corpo da requisição exigido pela z-api
    payload = {
        "phone": phone,
        "message": message
    }

    try:
        # cabeçalho obrigatório para autenticação segura da conta do cliente
        headers = {
            "Client-Token": CLIENT_TOKEN
        }

        # realiza a requisição post com um limite de tempo (timeout) de 10 segundos
        response = requests.post(url, json=payload, headers=headers, timeout=10)

        data = {}

        try:
            # tenta decodificar a resposta da API como JSON
            data = response.json()
        except Exception:
            # caso a api retorne texto puro ou erro html, captura o conteúdo bruto
            data = {"raw": response.text}

        # o envio só é considerado bem-sucedido se o status http for 2xx (ok)
        # e a Z-API não tiver retornado uma propriedade "error" dentro do json
        success = response.ok and data.get("error") is None

        return {
            "success": success,
            "status_code": response.status_code,
            "response": data
        }

    except requests.RequestException as e:
        # captura falhas de rede, quedas de conexão ou estouro de timeout
        return {
            "success": False,
            "status_code": None,
            "response": str(e)
        }


def check_instance_status() -> bool:
    # verifica se a instância da z-api está conectada ao whatsapp
    # retorna:
        # bool: true se a instância estiver ativa e conectada e false caso não esteja
    url = (
        f"https://api.z-api.io/instances/"
        f"{ZAPI_INSTANCE_ID}/token/"
        f"{ZAPI_TOKEN}/status"
    )

    headers = {
        "Client-Token": CLIENT_TOKEN
    }

    try:
        # consulta o endpoint de status da z-api
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        data = response.json()

        # retorna true apenas se a requisição foi bem-sucedida e o campo "connected" for true
        return (
            response.ok and
            data.get("connected") is True
        )

    except Exception:
        # qualquer falha de comunicação ou json inválido, invalida a checagem
        return False