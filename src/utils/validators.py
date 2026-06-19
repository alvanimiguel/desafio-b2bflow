import re

# valida número brasileiro no formato:
# 55 + ddd + número de 8 a 9 dígitos

# exemplos válidos:
# 5579999999999
# 557999999999
def validate_phone(phone: str) -> bool:
    if not phone:
        return False

    return bool(
        re.fullmatch(r"55\d{10,11}", str(phone))
    )