# GitHub Contributors FastAPI

Python FastAPI app which allows to ingest and query contributors of GitHub repos.

## Features

- **Ingest Contributors Endpoint**: Accepts a POST request with a JSON body containing a GitHub public repository owner and repo name. Fetches all contributors of the specified repository from GitHub's API and inserts their data into a MongoDB collection.
- **Get Contributor Info Endpoint**: Accepts a POST request with parameters to retrieve contributor information from the MongoDB collection.
- **Asynchronous Operations**: Utilizes `httpx` for asynchronous HTTP requests to GitHub's API and `motor` for asynchronous MongoDB operations.
- **Input Validation and Error Handling**: Uses Pydantic models for input validation and custom exception handlers for error management.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- MongoDB (local installation or MongoDB Atlas)


### Running the Application

1. Start the FastAPI application:
   ```
   uvicorn main:app --reload
   ```
2. Access the API documentation at `http://localhost:8000/docs` to interact with the endpoints.

### Usage

#### Ingest Contributors Endpoint

To ingest contributors from a GitHub repository, make a POST request to `/ingest-contributors` with the repository owner and repo name in the request body.

Example request using `curl`:
```bash
curl --location 'http://localhost:8000/ingest-contributors' \
--header 'Content-Type: application/json' \
--data '{
    "owner": "facebook",
    "repo": "react"
}'
```

#### Get Contributor Info Endpoint

To retrieve contributor information, make a POST request to `/contributors` with the repository owner, repo name, username, and type in the request body.

Example request using `curl`:
```bash
curl --location 'http://localhost:8000/contributors' \
--header 'Content-Type: application/json' \
--data '{
    "owner": "facebook",
    "repo": "react",
    "username": "zpao",
    "type": "User"
}'
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- FastAPI for providing a fast, web-based framework for building APIs.
- MongoDB for offering a flexible, scalable NoSQL database solution.
- GitHub for hosting the public repositories and contributor data.