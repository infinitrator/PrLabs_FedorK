"""Клиент для работы с GigaChat API.

Содержит функции для инициализации соединения и отправки запросов
к разным моделям (Gigachat-2-Pro и Gigachat-2-Max).
"""

from typing import Optional
from gigachat import GigaChat
# from config.secrets import CA_BUNDLE_PATH


def get_gigachat_client(
    model: str = "Gigachat-2-Pro",
    temperature: float = 0.7,
    max_tokens: Optional[int] = None,
) -> GigaChat:
    """Возвращает настроенный клиент GigaChat.

    Args:
        model (str): Название модели ('Gigachat-2-Pro' или 'Gigachat-2-Max').
        temperature (float): Температура генерации (0.0–1.0).
        max_tokens (Optional[int]): Максимальное число токенов в ответе.

    Returns:
        GigaChat: Настроенный контекстный менеджер для запросов.

    Raises:
        ValueError: Если указано неподдерживаемое имя модели.
    """
    from config.secrets import GIGACHAT_2_PRO_KEY, GIGACHAT_2_MAX_KEY

    if model == "Gigachat-2-Pro":
        credentials = GIGACHAT_2_PRO_KEY
    elif model == "Gigachat-2-Max":
        credentials = GIGACHAT_2_MAX_KEY
    else:
        raise ValueError(f"Неизвестная модель: {model}")

    return GigaChat(
        credentials=credentials,
        # ca_bundle_file=CA_BUNDLE_PATH,
        model=model,
        scope="GIGACHAT_API_B2B",
        verify_ssl_certs=False,
        # temperature=temperature,
        # max_tokens=max_tokens,
    )