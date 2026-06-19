import logging
from pathlib import Path

# diretório do logger.py
BASE_DIR = Path(__file__).parent

# pasta de logs
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "app.log"

logger = logging.getLogger("b2bflow")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

# escreve os logs no arquivo app.log
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

# escreve os logs no terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# evita handlers duplicados
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)