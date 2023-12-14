# API Documentation

## Introduction

The API for our system is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+. FastAPI leverages standard Python type hints for automatic data validation and documentation generation.

## Framework Used

### FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is employed as the primary framework for building our API. It provides a robust and efficient foundation for creating API endpoints with Python, ensuring high performance and ease of use.

## System Functionalities

The API supports the following system functionalities through two distinct tasks:

1. **Sexism Detection Task:**
   - **Endpoint:** `/prediction_sexism`

2. **Category Detection Task:**
   - **Endpoint:** `/prediction_category`

## Usage

To run the FastAPI server, execute the following command:

```bash
uvicorn main:app --reload
```
## Swagger UI
It is possible to test the API  using Swagger UI, a user-friendly interface that simplifies the understanding of API functionalities. To access to the Swagger UI, navigate to:

```bash
http://127.0.0.1:8000/docs
```
Here is showed the main window of the UI.

![SwaggerUI](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/blob/main/src/api/SwaggerUI.png)

As we can see in the picture there are two endpoint used to make the prediction of a given message. 

Here there is an example of the `/prediction_sexism` endpoint.

![Sexism1](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/blob/main/src/api/Sexism1.png)

In the response body is showned the message that has been inserted from the user and the prediction.

![Sexism2](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/blob/main/src/api/Sexism2.png)

Instead here we have an example  of the `/prediction_category` endpoint. The user has to insert the message and then it will be displayed the result.

![Category1](https://github.com/se4ai2324-uniba/DetectionOfOnlineSexism/blob/main/src/api/Category1.png)

