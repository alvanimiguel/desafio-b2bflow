from dotenv import load_dotenv
import os

# carrega as variáveis de ambiente do arquivo oculto '.env' para a memória do sistema
load_dotenv()

# inicia as credenciais do supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# inicia as credenciais do z-api
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")

# verifica se todas as variáveis de ambiente foram preenchidas
def validate_env():
    # dicionário de mapeamento para facilitar a iteração e checagem das variáveis obrigatória
    required_vars = {
        "SUPABASE_URL": SUPABASE_URL,
        "SUPABASE_KEY": SUPABASE_KEY,
        "ZAPI_INSTANCE_ID": ZAPI_INSTANCE_ID,
        "ZAPI_TOKEN": ZAPI_TOKEN,
        "CLIENT_TOKEN": CLIENT_TOKEN
    }

    missing_vars = []

    # verifica o dicionário procurando algum valor que esteja vazio, nulo ou ausente
    for name, value in required_vars.items():
        if not value:
            missing_vars.append(name)

    return missing_vars