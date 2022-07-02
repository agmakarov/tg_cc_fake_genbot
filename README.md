# Бот для генерации тестовых карт, написанный на Python

### Как запустить?

1. Установить Python: https://www.python.org/downloads/
2. Скачать проект из github и открыть в IDE (например, VSCode)
3. Указать API-КЛЮЧ бота, полученный из BotFather в файл .env
4. Установить требуемые библиотеки ```pip install -r requirements.txt```
6. Запускать командой ```python main.py```

### Как запустить через Docker ?

1. Скачать проект из github и перейти в папку
2. Собрать образ из Dockerfile командой ```docker build -t cc_fake_gen .```
3. Запустить образ командой ```docker run --rm --name cc_fake_gen cc_fake_gen```

### Дополнительно (Docker)
Посмотреть все запущенные контейнеры ```docker ps```

Остановить контейнер ```docker stop cc_fake_gen```

Удалить контейнер ```docker image rm cc_fake_gen```
