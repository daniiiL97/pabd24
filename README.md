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

Запуск обучения модели (также проводит и валидацию из скрипта test_model.py при локальном запуске). На вход можно передать путь для сохранения весов обученной модели.
```python train_model.py```
Валидация модели:
```python test_model.py```

### 6. Запуск приложения flask 
Запуск приложения локально
```python predict_app.py```
Запуск приложения при деплое на сервере gunicorn на виртуальной машине
```gunicorn -b 0.0.0.0 src.predict_app:app --daemon```
Адрес:
http://192.144.14.184:8000/predict

### 7. Использование сервиса через веб интерфейс 

Для использования сервиса используйте файл `web/index.html`.  

### 8. Использование сервиса через веб интерфейс 

docker run -dp 8000:8000 dan4ik97/pabd24:latest


