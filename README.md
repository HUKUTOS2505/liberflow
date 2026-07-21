# LiberFlow

LiberFlow — внутренняя система LiberCode для управления техническими
проектами, сотрудниками, спринтами, задачами разработки, Kanban-процессом и
учётом рабочего времени. Система будет интегрирована с облачным порталом
Битрикс24 компании, при этом данные о технической разработке останутся внутри
LiberFlow.

Проект разрабатывается небольшими проверяемыми дневными пакетами. Первый пакет
содержит только базовую структуру Django и endpoint проверки состояния.
PostgreSQL, Docker, бизнес-сущности, REST API и подключение к Битрикс24 пока
намеренно не реализованы.

## Требования

- Python 3.12 или новее
- Git

## Локальный запуск

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python manage.py migrate
python manage.py runserver
```

Bash:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python manage.py migrate
python manage.py runserver
```

Конфигурация разработки содержит безопасные локальные значения по умолчанию.
Файл `.env.example` описывает переменные окружения, но загрузчик `.env` не
входит в первый дневной пакет. Чтобы переопределить значения, экспортируйте
переменные в текущей командной оболочке. Полноценная настройка окружения и
PostgreSQL запланирована на второй дневной пакет.

После запуска откройте `http://127.0.0.1:8000/health/`. Endpoint вернёт:

```json
{
  "status": "ok"
}
```

## Проверки качества

```powershell
python manage.py check
pytest
ruff check .
```

Порядок разработки описан в [ROADMAP.md](ROADMAP.md), границы системы — в
[ARCHITECTURE.md](ARCHITECTURE.md), а текущее состояние проекта — в
[PROJECT_STATE.md](PROJECT_STATE.md).
