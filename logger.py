import logging

# Настройка логирования
logging.basicConfig(
    filename='library_operations.log',  # Имя файла для логов
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s'  # Формат записи
)

# Функция для записи логов
def log_action(level, message):
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.debug(message)