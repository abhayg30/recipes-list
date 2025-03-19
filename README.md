# Recipes Django Project

Welcome to the Recipes Django Project! This project is designed to help you manage and share your favorite recipes.

## Project Structure

```
recipes/
├── manage.py
├── requirements.txt
├── recipes/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── serializers.py
│   ├── util.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
README.md
docker-compose.yml
```

## Getting Started

### Prerequisites

All pre-requisites are mentioned in the requirements.txt
You need an virtual environment in which you need to install all dependencies and then run the project

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/abhayg30/recipes-list.git
    ```
2. Navigate to the project directory:
    ```sh
    cd recipes
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Run docker compose:
   Go to the parent folder using:
   ```sh
   cd ..
   ```
   Then run:
   ```
   docker-compose up -d
   ```

### Running the Project

1. Run the development server:
   Go into the `recipes` folder then:
    ```sh
    python manage.py runserver
    ```
3. Your backend is now live on:  `http://127.0.0.1:8000/`

## Features

- Add recipes
- View a list of all recipes
- Search for recipes by `id` and get the ingredients as per servings required and units you want

Happy cooking!
