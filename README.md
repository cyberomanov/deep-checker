## Установка Python 3.10 и pip 3.10 на Ubuntu

### Шаг 1: Обновите систему

Перед началом установки рекомендуется обновить системные пакеты:

```bash
sudo apt update && sudo apt upgrade -y
```

### Шаг 2: Установите зависимости
Для успешной установки Python 3.10, вам потребуются некоторые зависимости:

```bash
sudo apt install software-properties-common -y
```

### Шаг 3: Добавьте PPA для Python 3.10

Добавьте репозиторий, содержащий Python 3.10:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
```

### Шаг 4: Установите Python 3.10
После добавления репозитория, установите Python 3.10:

```bash
sudo apt update && sudo apt install python3.10
```

### Шаг 5: Установите pip для Python 3.10
После установки Python 3.10, вам нужно будет установить pip:

```bash
sudo apt install python3.10-distutils
curl -sS https://bootstrap.pypa.io/get-pip.py | sudo python3.10
```

### Шаг 6: Проверьте установки
Убедитесь, что Python 3.10 и pip 3.10 установлены правильно:

```bash
python3.10 --version
pip3.10 --version
```

## Установка и запуск скрипта

### Шаг 1: Клонируйте репозиторий
Клонируйте репозиторий `deep-checker` на ваш локальный компьютер:

```bash
git clone https://github.com/cyberomanov/deep-checker.git && \
cd deep-checker
```
### Шаг 2: Откройте окно tmux
Чтобы ваш скрипт продолжал работу на сервере после вашего от него отключения, нужно использовать _tmux_.

```bash
tmux new -s deep-checker; tmux attach -t deep-checker
```
Этой же командой вы можете подключаться к старому окну, чтобы наблюдать за прогрессом.
### Шаг 3: Создайте и активируйте виртуальное окружение

```bash
python3.10 -m venv env && source env/bin/activate
```
### Шаг 4: Установите зависимости
Убедитесь, что у вас установлен pip для Python 3.10. Затем установите необходимые зависимости:

```bash
pip3.10 install -r requirements.txt
```

### Шаг 5: Настройка конфигурации
Откройте файл `user_data/config.py` в любом текстовом редакторе и настройте параметры согласно вашим требованиям.
<br><br>Откройте и настройте файл `user_data/address.txt`.

### Шаг 6: Запуск скриптов

Запустите скрипт `main.py` для запуска чекера:

```bash
python3.10 main.py
```

