from src.utils.logger import logger
from src.config import validate_env
from src.utils.validators import validate_phone
from src.services.supabase_service import get_contacts
from src.services.zapi_service import (
    send_message,
    check_instance_status
)

# registra o início do ciclo de execução do script
logger.info("Iniciando aplicação")

# verifica se o arquivo .env possui todas as credenciais necessárias
missing_vars = validate_env()

if missing_vars:
    logger.error("Variáveis de ambiente ausentes: " + ", ".join(missing_vars))
    exit(1)

# valida se a instância do whatsapp na z-api está conectada
if not check_instance_status():
    logger.error(
        "Instância Z-API desconectada. "
        "Escaneie o QR Code ou cheque a conexão com a internet e tente novamente."
    )
    exit(1)

# copia a lista de contatos direto do banco de dados
contatos = get_contacts()
logger.info(f"{len(contatos)} contatos encontrados")

# limita a execução aos 3 primeiros contatos da lista
for contato in contatos[:3]:
    nome = contato["nome"]
    telefone = contato["telefone"]

    # valida o formato do número
    if not validate_phone(telefone):
        logger.error(
            f"Número inválido para {nome}: {telefone}"
        )
        continue

    logger.info(
        f"Enviando mensagem para {nome}"
    )

    # envia a mensagem personalizada usando o z-api
    result = send_message(
        telefone,
        f"Olá {nome}, tudo bem com você?"
    )
    # tratamento do retorno da api
    if result["success"]:
        logger.info(
            f"Mensagem enviada para {nome} | "
            f"Status: {result['status_code']}"
        )
    else:
        # identifica a estrutura do erro
        if isinstance(result["response"], dict):
            error_msg = result["response"].get(
                "error",
                str(result["response"])
            )
        else:
            error_msg = str(result["response"])

        logger.error(
            f"Falha ao enviar para {nome} | "
            f"{error_msg}"
        )
# registra o encerramento com sucesso de todo o pipeline
logger.info("Processo finalizado")