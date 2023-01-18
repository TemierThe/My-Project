# Запуск веб-сервера
from website import create_app

app = create_app()

# точка входа
if __name__ == '__main__':  #  веб-сервер запускается только при запуске файла main.py
    app.run(debug=True)  # debug=True - каждый раз, когда мы вносим изменения в код, веб-сервер автоматически перезапускается