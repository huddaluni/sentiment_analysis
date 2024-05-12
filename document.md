

# Text Classification

This project implements a RESTful API using FastAPI for performing text classification tasks such as sentiment analysis or emotion classification. The API utilizes a pre-trained Hugging Face Transformer model and is containerized using Docker.

## Prerequisites

- Docker installed on your machine

## Build and Run the Docker Container

1. Clone this repository to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd text-classification-api
    ```

3. Build the Docker container:

    ```bash
    docker build -t text-classification-api .
    ```

4. Run the Docker container:

    ```bash
    docker run -d --name text-classification-api-container -p 8000:8000 text-classification-api
    ```

## Interacting with the API

Once the Docker container is running, you can interact with the API using HTTP requests.

