# 🚀 Keploy Flask Demo

This project showcases a simple *Flask API* that demonstrates *automated API testing using Keploy, a powerful open-source tool for capturing and generating test cases from real API traffic. It also integrates Keploy tests into a **CI/CD pipeline* using *GitHub Actions*.

---

## 📁 Project Structure
keploy-flask-demo/ │ ├── app.py                  # Flask application code ├── openapi.yaml            # OpenAPI schema used by Keploy ├── keploy.exe              # Keploy CLI (for Windows) ├── .github/ │   └── workflows/ │       └── keploy-ci.yml   # GitHub Actions CI/CD config └── README.md               # Project documentation (this file)

---

## 📌 Features

- ✅ Simple REST API using Flask
- ✅ OpenAPI specification
- ✅ Keploy test recording and replay support
- ✅ GitHub Actions CI/CD Integration
- ✅ Works on local machine with Postman/cURL

---

## 🧪 API Endpoints

| Method | Endpoint     | Description        |
|--------|--------------|--------------------|
| GET    | /menu      | Fetch all menu items |
| POST   | /menu      | Add a new menu item  |

### Sample POST /menu Request:
```json
{
  "name": "Pizza",
  "category": "Main",
  "price": 250,
  "availability": "Yes"
}
📖 OpenAPI Schema

The openapi.yaml file defines the API structure for Keploy. It is used to auto-generate test cases and simulate API traffic.


---

⚙ Running Keploy Tests

Record API Traffic

keploy.exe record --proxy

Make some API calls using Postman or cURL while the proxy is running.

Test Replay

keploy.exe test --command "python app.py"

Keploy will run the tests it captured during the recording phase.


---

🔁 CI/CD Integration

The GitHub Actions workflow (.github/workflows/keploy-ci.yml) ensures that every commit triggers:

1. Python setup


2. Dependency installation


3. Keploy test execution



Workflow File: keploy-ci.yml

name: Keploy CI

on:
  push:
    branches:
      - main

jobs:
  keploy-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'

      - name: Install Dependencies
        run: pip install flask

      - name: Download Keploy
        run: |
          wget https://github.com/keploy/keploy/releases/download/v0.1.6/keploy_linux_amd64.tar.gz
          tar -xvzf keploy_linux_amd64.tar.gz
          chmod +x keploy

      - name: Run Keploy Tests
        run: ./keploy test --command "python app.py"


---



✍ Author

👩‍💻 Thiraviya
Passionate about building and testing reliable software with AI-powered tools like Keploy.


---

📝 License

This project is licensed under the MIT License. See LICENSE for details.
