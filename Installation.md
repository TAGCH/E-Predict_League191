# Prerequisites
Make sure you have Python 3.8, 3.9, 3.10, or 3.11 installed on your system.


# Installation steps

## 1. Clone repository

- Clone this repository to your local computer.

```
git clone https://github.com/TAGCH/EPL-Prediction.git
```

## 2. Create virtual environment and install dependencies

- Create virtual environment.

```
python -m venv env
```

- Change to your newly created virtual environment.

For Mac and Linux.
```
source env/bin/activate
```
For Window.
```
env\Scripts\activate.bat
```

- Install packages from requirements.txt

```
pip install -r requirements.txt
```

## 3. Set values for externalized variables
- Create file `.env` to configuration.

- Copy code from [sample.env](sample.env) and paste it in `.env`

## 4. Create and apply the database migrations.



```
python manage.py makemigrations
python manage.py migrate
```
