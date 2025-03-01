# Flask API Activity

## Introduction
This is a simple Flask API project that provides an endpoint to retrieve and add items, along with a Jinja2-powered web interface for managing items.

## Prerequisites
Make sure you have the following installed:
- Python (>=3.6)
- Flask

## Setup Instructions

1. **Clone the Repository (or create project folder manually)**
   ```sh
   git clone <your-repo-link>
   cd <your-repo-folder>
   ```

2. **Create a Virtual Environment (Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install flask
   ```

4. **Run the Application**
   ```sh
   python main.py
   ```
   The server will start at `http://127.0.0.1:5000/`

## API Endpoints

### 1. Welcome Message
- **Endpoint:** `/`
- **Method:** GET
- **Response:**
  ```json
  {
    "message": "Welcome to the Flask API!"
  }
  ```

### 2. Get All Items
- **Endpoint:** `/items`
- **Method:** GET
- **Response:**
  ```json
  [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Mouse", "price": 25},
    {"id": 3, "name": "Keyboard", "price": 75}
  ]
  ```

### 3. Get Item by ID
- **Endpoint:** `/items/<id>`
- **Method:** GET
- **Response:**
  ```json
  {"id": 1, "name": "Laptop", "price": 1200}
  ```
- **Error Response (if ID is not found):**
  ```json
  {"error": "Item not found"}
  ```

### 4. Add New Item (API)
- **Endpoint:** `/items`
- **Method:** POST
- **Request Body (Form Data):**
  ```sh
  name=Laptop Stand
  price=50.99
  ```
- **Response:**
  ```json
  {"id": 4, "name": "Laptop Stand", "price": 50.99}
  ```

## Web Interface

### 1. View Items in Web Page
- **URL:** `http://127.0.0.1:5000/items_web`

### 2. Add Item via Web Form
- **URL:** `http://127.0.0.1:5000/add_item_web`
- **Steps:**
  - Fill out the form with the item name and price.
  - Click Submit.
  - The new item will be displayed in the confirmation page.

## Testing the API

### Using Curl
```sh
curl -X GET http://127.0.0.1:5000/items
```

```sh
curl -X POST -d "name=Tablet" -d "price=300" http://127.0.0.1:5000/items
```

### Using Postman
1. Open Postman and set the method to `GET` or `POST`.
2. Enter the corresponding endpoint URL (`http://127.0.0.1:5000/items`).
3. For POST requests, go to the **Body** section, select **x-www-form-urlencoded**, and enter the required parameters (`name`, `price`).
4. Click **Send** and check the response.

## Conclusion
This Flask API allows users to retrieve and manage items through both JSON API and a web-based interface. You can extend the project by adding database integration or authentication mechanisms.

