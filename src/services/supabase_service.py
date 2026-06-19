from supabase import create_client
from src.config import SUPABASE_URL, SUPABASE_KEY

def get_contacts() -> list:
    # conecta ao supabase e busca todos os registros da tabela 'contacts'
    # retorna:
        # list: uma lista de dicionários, onde cada dicionário representa um contato com suas respectivas colunas (id, nome, telefone)

    # cria a instância do cliente do supabase localmente dentro da função
    # isso garante que a conexão só seja tentada depois que as variáveis de ambiente forem validadas com sucesso no main.py
    supabase = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )

    # realiza a consulta na tabela "contacts" trazendo todas as colunas (*)
    response = (
        supabase
        .table("contacts")
        .select("*")
        .execute()
    )

    # retorna apenas a lista de dados brutos encontrados no banco
    return response.data