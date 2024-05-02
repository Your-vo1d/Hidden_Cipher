# Используем базовый образ Python с PyQt5
FROM python:3.12.3-slim

# Установка рабочей директории в контейнере
WORKDIR /app

# Копирование исходного кода в контейнер
COPY interface.py .
COPY main.py .

# Установка зависимостей PyQt5
RUN pip install pyqt5

# Указание команды запуска приложения
CMD ["python", "main.py"]