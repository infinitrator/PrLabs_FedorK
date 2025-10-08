# Промпт-инжиниринг 2025 — Лабораторные работы

Репозиторий для выполнения лабораторных работ по курсу **«Промпт-инжиниринг»** в Университете ИТМО.

Работы выполнены с использованием **GigaChat API** (модели `Gigachat-2-Pro` и `Gigachat-2-Max`).

---

## Структура проекта

```
PrLabs_Fedork/
├── notebooks/        # Jupyter-ноутбуки с экспериментами
├── src/              # Переиспользуемый Python-код
├── reports/          # Готовые отчёты (Word)
├── config/           # Конфигурация (ключи — НЕ в Git!)
└── requirements.txt  # Зависимости
```

---

## Установка

1. Клонируй репозиторий:
   ```bash
   git clone https://github.com/your-username/PrLabs_Fedork.git
   cd PrLabs_Fedork
   ```

2. Создай виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Скачай [сертификат Минцифры](https://developers.sber.ru/docs/ru/gigachat/certificates) и сохрани, например, в `C:/certs/russian_trusted_root_ca.cer`.

5. Создай файл `config/secrets.py`:
   ```python
   GIGACHAT_2_PRO_KEY = "твой-ключ-для-2-Pro"
   GIGACHAT_2_MAX_KEY = "твой-ключ-для-2-Max"
   CA_BUNDLE_PATH = "C:/certs/russian_trusted_root_ca.cer"
   ```

6. Запусти Jupyter:
   ```bash
   jupyter notebook
   ```

---

## Лабораторные работы

| № | Тема | Файл |
|---|------|------|
| 1 | Введение в GigaChat | `notebooks/lab1.ipynb` |
| 2 | Промпт-инжиниринг для эссе | `notebooks/lab2.ipynb` |

---

## Безопасность

- Файл `config/secrets.py` добавлен в `.gitignore`.
- **Никогда не коммить секреты!**
- Для совместной работы используй шаблон `config/secrets.py.example`.

---

## Стандарты кода

- Соблюдён **PEP 8** (через `ruff` или `black`).
- Документация — **PEP 257** (Google-style docstrings).
- Все функции покрыты типами (`mypy`-совместимо).

---

> Выполнил: Корнеев Фёдор, студент Университета ИТМО  
> 2025 г.