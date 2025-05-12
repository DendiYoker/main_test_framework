# Базовый образ Python 3.12 (легковесная версия)
FROM python:3.12-slim

# Установка зависимостей для Chrome (для Selenium)
RUN apt-get update && \
    apt-get install -y wget gnupg2 xvfb && \  # xvfb для headless-режима
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \  # Установка Chrome
    rm -rf /var/lib/apt/lists/*  # Очистка кеша

# Установка Python-зависимостей (оптимизация слоев Docker)
WORKDIR /app
COPY requirements.txt .  # Копируем только requirements.txt сначала
RUN pip install --no-cache-dir -r requirements.txt  # Без кеша для уменьшения размера

# Копирование всего кода
COPY . .

# Команда запуска (headless-режим + pytest)
CMD ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x24 > /dev/null 2>&1 & export DISPLAY=:99 && pytest -v"]