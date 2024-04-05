# API Backend for Library Management System

This project is an API backend for the Library Management System. It provides endpoints to manage student records in the library system using FastAPI and MongoDB. Additionally, the backend is deployed and accessible [here](#deployed-backend).


## Table of Contents
- [Project Structure](#project-structure)
- [Setup](#setup)
- [API Documentation](#api-documentation)
- [Environment Variables](#environment-variables)
- [Dependencies](#dependencies)

## Project Structure

The project follows a modular structure with the following directories:

- `config/`: Contains configuration files for database connection settings.
- `models/`: Defines data models used in the application, such as the `Student` model.
- `routes/`: Contains route handlers for different API endpoints.
- `schema/`: Defines Pydantic schemas for serialization and deserialization.
- `main.py`: Entry point of the FastAPI application.
- `.env.sample`: Sample `.env` file for configuring environment variables.
- `requirements.txt`: List of Python dependencies required by the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Utkarsh1504/api-bacosmo.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Rename `.env.sample` to `.env` and configure environment variables.

5. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

## API Documentation

The API endpoints are documented using Swagger UI. Once the server is running, you can access the documentation at:

```
http://localhost:8000/docs
```

## Environment Variables

The following environment variables can be configured in the `.env` file:

- `MONGO_URL`: MongoDB connection URL.

## Dependencies

The project uses the following main dependencies:

- [FastAPI](https://fastapi.tiangolo.com/): Web framework for building APIs with Python.
- [PyMongo](https://pymongo.readthedocs.io/): Python driver for MongoDB.
- [python-dotenv](https://pypi.org/project/python-dotenv/): For loading environment variables from a `.env` file.

