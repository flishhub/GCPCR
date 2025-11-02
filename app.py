from flask import Flask, request
app = Flask(__name__)

@app.get("/")
def index():
    name = request.args.get("name", "World")
    return f"Hello, {name}! � Running on Cloud Run."

# Cloud Run listens on port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
