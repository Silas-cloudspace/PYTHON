from flask import Flask, request, jsonify

app = Flask(__name__)

# GET request
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "mail": "John.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200

# Post request
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)
    


""" This code defines a basic Flask web application with two endpoints for handling user data. Here’s a breakdown of each section:

1. Importing Flask Modules

from flask import Flask, request, jsonif

- Flask: The main class to create a Flask app.
- request: Allows access to incoming request data.
- jsonify: Converts Python dictionaries to JSON format for HTTP responses.

2. Initializing the Flask App

app = Flask(__name__)

- This creates a Flask app instance using the current module’s name, __name__.

3. GET Request Endpoint

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "mail": "John.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200
    
- Route: @app.route("/get-user/<user_id>") defines a route with a URL parameter, user_id.

- Handler Function: get_user(user_id) handles the request.
  - user_data: A dictionary containing mock user details.
  - extra = request.args.get("extra"): Checks if an additional query parameter extra is provided in the URL (e.g., /get-user/1?extra=info). If it exists, it's added to user_data.

- Response: jsonify(user_data), 200 returns the user data in JSON format with a 200 OK status code.

4. POST Request Endpoint

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    
    return jsonify(data), 201

- Route: @app.route("/create-user", methods=["POST"]) specifies that this endpoint only accepts POST requests.

- Handler Function: create_user() handles the request.
  - data = request.get_json(): Extracts JSON data from the request body (e.g., {"user_id": "1", "name": "John Doe"}).

- Response: jsonify(data), 201 echoes back the JSON data received, with a 201 Created status code indicating successful resource creation.

5. Running the App

if __name__ == "__main__":
    app.run(debug=True)

- Runs the app on a local server with debug mode enabled, which helps catch errors and automatically reloads the server for code changes. 

https://www.youtube.com/watch?v=zsYIw6RXjfM """