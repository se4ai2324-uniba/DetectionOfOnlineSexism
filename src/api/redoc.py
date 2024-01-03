"""
Module: redoc
Description: This script serves an API using FastAPI
providing documentation with ReDoc.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
Date: 2023-11-03
"""
import uvicorn
from server_api import app
from fastapi.openapi.utils import get_openapi
from fastapi.responses import HTMLResponse

def custom_openapi():
    """
    Function: custom_openapi.
    This function customizes the OpenAPI schema for the FastAPI application,
    specifying title, version, and description for documentation.
    """
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Detection Online Sexism - ReDoc",
        version="1.0.0",
        description="API Description",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/docs", response_class=HTMLResponse)
async def redoc_html():
    """
    Function: redoc_html.
    This function generates and returns an HTML document for ReDoc.
    """
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <title>Detection Online Sexism - ReDoc</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                margin: 0;
                padding: 0;
            }
        </style>
    </head>
    <body>
        <redoc spec-url='/openapi.json'></redoc>
        <script src="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"></script>
    </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
