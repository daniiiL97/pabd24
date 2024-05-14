# Предиктивная аналитика больших данных

Учебный проект для демонстрации основных этапов жизненного цикла проекта предиктивной аналитики.  

## Installation 

Клонируйте репозиторий, создайте виртуальное окружение, активируйте и установите зависимости:  

```sh
git clone https://github.com/yourgit/pabd24
cd pabd24
python -m venv venv

source venv/bin/activate  # mac or linux
.\venv\Scripts\activate   # windows

pip install -r requirements.txt
```

## Usage

### 1. Сбор данных о ценах на недвижимость 
```python parse_cian.py```

### 2. Выгрузка данных в хранилище S3 
Для доступа к хранилищу скопируйте файл `.env` в корень проекта.  

```python upload_to_s3.py``` 
```python upload_to_s3.py -i data/raw/1_2024-05-14_20-14.csv```

### 3. Загрузка данных из S3 на локальную машину  

```python download_from_s3.py```
```python download_from_s3.py -i data/raw/1_2024-05-14_20-14.csv```

### 4. Предварительная обработка данных  

```python preprocess_data.py```
```python preprocess_data.py -s 0.8 -i data/raw/1_2024-05-14_20-14.csv```

### 5. Обучение модели 

todo Описание модели и входных параметров для предсказания здесь.  

### 6. Запуск приложения flask 

todo

### 7. Использование сервиса через веб интерфейс 

Для использования сервиса используйте файл `web/index.html`.  
