"""Вспомогательные функции для анализа и сравнения ответов GigaChat.

Содержит инструменты для:
- подсчёта слов и предложений, — выявления маркеров галлюцинаций ([проверить], [Тьюринг] и т.д.), — форматированного вывода сравнений.
"""

import re


def count_words(text: str) -> int:
    """Подсчитывает количество слов в тексте.

    Args:
        text (str): Входной текст.

    Returns:
        int: Количество слов.
    """
    return len(text.split())


def count_sentences(text: str) -> int:
    """Подсчитывает количество предложений по знакам препинания.

    Args:
        text (str): Входной текст.

    Returns:
        int: Количество предложений.
    """
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])


def extract_fact_markers(text: str) -> list:
    """Извлекает все маркеры фактов вида [что-то].

    Args:
        text (str): Текст ответа модели.

    Returns:
        list[str]: Список найденных маркеров, например: ['[1956]', '[проверить]'].
    """
    return re.findall(r'\[[^]]+]', text)


def compare_responses(
    prompt: str,
    response_pro: str,
    response_max: str,
    step_name: str = "Шаг без названия",
) -> str:
    """Формирует читаемое сравнение двух ответов.

    Args:
        prompt (str): Промпт, использованный для генерации.
        response_pro (str): Ответ от Gigachat-2-Pro.
        response_max (str): Ответ от Gigachat-2-Max.
        step_name (str): Название шага (для заголовка).

    Returns:
        str: Форматированный Markdown-текст сравнения.
    """
    lines = [f"### {step_name}", "", "**Промпт:**", f"> {prompt}", "", "---"]

    lines.extend([
        "**Gigachat-2-Pro:**",
        f"> {response_pro}",
        "",
        f"- Слов: {count_words(response_pro)}",
        f"- Предложений: {count_sentences(response_pro)}",
        f"- Маркеры фактов: {extract_fact_markers(response_pro) or 'нет'}",
        "",
        "**Gigachat-2-Max:**",
        f"> {response_max}",
        "",
        f"- Слов: {count_words(response_max)}",
        f"- Предложений: {count_sentences(response_max)}",
        f"- Маркеры фактов: {extract_fact_markers(response_max) or 'нет'}",
        "",
        "**Сравнение:**",
        "> [Твой анализ: 2–3 предложения]",
        "",
        "---",
        ""
    ])
    return "\n".join(lines)


def build_essay(parts: list[str]) -> str:
    """Собирает эссе из списка абзацев.

    Args:
        parts (list[str]): Список абзацев (вступление, позиция, примеры и т.д.).

    Returns:
        str: Полный текст эссе с пустыми строками между абзацами.
    """
    return "\n\n".join(part.strip() for part in parts if part.strip())