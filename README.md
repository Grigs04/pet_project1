# Mazda6 Market Analysis

Проект собирает объявления автомобилей Mazda6 с auto.drom.ru,
обрабатывает и очищает данные, рассчитывает рейтинг «выгодности»
каждого автомобиля и сохраняет результат в Excel и SQLite базу данных
для дальнейшего анализа.
---
## Tech Stack

- Python 3.12
- pandas
- requests
- BeautifulSoup4
- sqlite3 (standard library)
---
## Project Structure

- src/
  - config.py # Константы и настройки проекта
  - fetch.py # HTTP-запросы и загрузка HTML
  - parsing.py # Парсинг и первичная очистка данных
  - analysis.py # Расчёт рейтингов и метрик
  - unloading.py # Выгрузка данных в Excel и SQL
- data/
  - mazda_cars.xlsx # Excel-выгрузка
  - best_mazda_cars.xlsx # Excel-выгрузка топ 5 наиболее выгодных авто
  - mazda_cars.db # SQLite база данных
---
## Data Pipeline

1. **Fetch**  
   Загрузка HTML-страниц с объявлениями автомобилей

2. **Parse**  
   Извлечение характеристик:
   - год выпуска
   - комплектация
   - объем двигателя
   - мощность
   - топливо
   - коробка передач
   - привод
   - пробег
   - цена
   - ссылка на объявление

3. **Analysis**  
   Формирование рейтинга автомобиля на основе:
   - года выпуска
   - пробега
   - коробки передач
   - уровня комплектации
   - цены

4. **Export**  
   Сохранение данных:
   - в Excel-файл
   - в SQLite базу данных

---
## Как запустить проект

### 1. Клонировать репозиторий
```bash
git clone <repository_url>
cd pet_project1
```

---

### 2. Создать виртуальное окружение (рекомендуется)
```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

---

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

---

### 4. Запустить пайплайн обработки данных

Выполните скрипты по очереди:

```bash
python src/run.py
```

---

### 5. Проверить результат

После выполнения скриптов результаты будут сохранены в папке `data/`:

- `mazda_cars.xlsx` — выгрузка в Excel
- `best_mazda_cars.xlsx` — выгрузка в Excel топ 5 наиболее выгодных авто
- `mazda_cars.db` — база данных SQLite

---

### 6. (Опционально) Просмотр базы данных

Для просмотра SQLite базы данных можно использовать:
- **DB Browser for SQLite**
- **DBeaver**

Откройте файл:
```
data/mazda.db
```

---

### Требования

- Python 3.10+
- Подключение к интернету
- Windows / macOS / Linux
