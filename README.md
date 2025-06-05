# 🧾 Django + Stripe Checkout Backend

Бэкенд-приложение на Django с интеграцией Stripe API для оформления покупок — как поштучно, так и пакетно (через заказ).

## 🚀 Онлайн-доступ

- 🌐 Сайт: [https://stripe-prj.onrender.com](https://stripe-prj.onrender.com)
- 🔑 Админка: [https://stripe-prj.onrender.com/admin](https://stripe-prj.onrender.com/admin)  

---

## 📦 Функциональность

### Основное
- Django модель **Item**: `name`, `description`, `price`.
- Stripe Checkout для покупки одного товара:  
  `GET /item/<id>/` – HTML-страница с кнопкой "Buy"  
  `GET /buy/<id>/` – создание Stripe Session и редирект на оплату

### Заказ (Order)
- Django модель **Order** с возможностью добавить несколько `Item`.
- Страница с формой выбора товаров.
- Возможность оплатить весь заказ одной Stripe-сессией.

---

## 🐳 Быстрый старт (через Docker)

```bash
git clone https://github.com/osccircuit/stripe_prj
cd stripe-prj
# заполни переменные в .env

docker compose up --build
```
---

## 🐍 Установка вручную
```bash
git clone https://github.com/osccircuit/stripe_prj
cd stripe-prj

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# заполни переменные в .env
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/payments/item.json
python manage.py runserver

```
---

## ⚙️ Конфигурация (.env)
```bash
SECRET_KEY='django-insecure'

# Stripe API keys
SECRET_KEY_STRIPE='sk_test'
PUBLIC_KEY_STRIPE='pk_test'

# PostgreSQL config
# DJANGO_ALLOWED_HOSTS=
DATABASE_ENGINE=postgresql_psycopg2
DATABASE_NAME=user_db
DATABASE_USERNAME=user
DATABASE_PASSWORD=password
DATABASE_HOST=db
# DATABASE_HOST=localhost
DATABASE_PORT=5432

DEBUG=True
```
---

## 🧪 Как протестировать

### Оплата одного товара

   - Перейти на /item/\<id>/
   - Нажать кнопку "Buy"
   - Будет создан Session и откроется Stripe Checkout

### Заказ из нескольких товаров

   - Перейти на "Главную страницу" /
   - Выбрать товары в форме
   - Подтвердить заказ на следующей странице нажать кнопку "Buy" 
   - Будет создан Session и откроется Stripe Checkout

---
## 📤 Автор

Егор Попов
Backend-разработка • Python • Django • Stripe Integration