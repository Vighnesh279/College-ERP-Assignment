from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>College ERP - DevOps Assignment</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f1f5f9;
                color: #1e293b;
            }
            header {
                background: #1d4ed8;
                color: white;
                padding: 24px;
                text-align: center;
            }
            main {
                max-width: 750px;
                margin: 40px auto;
                padding: 28px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 14px #00000012;
            }
            .status {
                display: inline-block;
                padding: 8px 14px;
                background: #dcfce7;
                color: #166534;
                border-radius: 20px;
            }
            footer {
                text-align: center;
                padding: 20px;
                color: #64748b;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>College ERP System</h1>
            <p>Assignment 2: CI/CD and Docker Deployment</p>
        </header>
        <main>
            <h2>Application Dashboard</h2>
            <p>Welcome to the College ERP demonstration application.</p>
            <p>This application is deployed using Docker and Docker Compose.</p>
            <p class="status">Application is running</p>
            <h3>DevOps Components</h3>
            <ul>
                <li>Automated testing with pytest</li>
                <li>Containerization with Docker</li>
                <li>Deployment with Docker Compose</li>
                <li>CI/CD automation with GitHub Actions</li>
            </ul>
        </main>
        <footer>College ERP | DevOps Practical Assignment</footer>
    </body>
    </html>
    """


@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok", service="college-erp"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)