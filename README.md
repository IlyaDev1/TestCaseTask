## 🗕 Scheduler (Async version)

Асинхронный валидатор и загрузчик расписаний.  
Поддерживает валидацию структуры данных по URL.

---

### 📦 Быстрый запуск тестов через Docker

#### 🐳 Использование Docker Hub

Вы можете запустить тесты проекта без клонирования репозитория:

```bash
docker run --rm ilya407/scheduler_tests
```

Образ автоматически выполнит все тесты и выведет результат в консоль.

---

### 🧪 Локальный запуск тестов

Если вы хотите развернуть проект и запустить тесты локально:

#### 1. Клонируйте репозиторий

```bash
git clone https://github.com/IlyaDev1/TestCaseTask
cd TestCaseTask
```

#### 2. Убедитесь, что установлен Python 3.12+

#### 3. Установите зависимости с помощью [uv](https://github.com/astral-sh/uv)

```bash
pip install uv
uv venv .venv
source .venv/bin/activate  # или .venv\Scripts\activate на Windows
uv sync --all-extras
```

#### 4. Запустите тесты

```bash
uv run pytest --tb=short --disable-warnings
```

### 🚀 Контейнеризация

Если вы хотите собрать образ локально:

```bash
docker build -t scheduler_tests .
docker run --rm scheduler_tests
```
