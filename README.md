🚀 Python CI/CD Pipeline

📌 Project Overview

This is a beginner-friendly CI/CD mini project built using Python, pytest, GitHub, and GitHub Actions.

The project demonstrates how Continuous Integration (CI) can automatically test Python code whenever changes are pushed to a GitHub repository.

🎯 Project Objective

The main objective of this project is to understand and implement a basic CI pipeline using GitHub Actions.

The pipeline automatically:

Checks out the source code.

Sets up Python.

Installs project dependencies.

Tests the application with multiple Python versions.

Runs automated tests using pytest.

Reports whether the tests passed or failed.

🛠️ Technologies Used

Python

pytest

pip

Git

GitHub

GitHub Actions

YAML

📂 Project Structure

python-cicd-project/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── .gitignore
├── app.py
├── test_app.py
├── requirements.txt
└── README.md

🐍 Application

The project contains simple Python functions for demonstration and testing.

The main application file is app.py.

The application includes:

Addition

Multiplication

🧪 Automated Testing

Automated tests are written using pytest.

The test file is test_app.py.

To run the tests locally:

pytest

Expected result:

2 passed

🔄 CI Pipeline

The project uses GitHub Actions to implement Continuous Integration.

Pipeline Flow

Developer
    ↓
Write / Modify Code
    ↓
Git Commit
    ↓
Git Push
    ↓
GitHub Repository
    ↓
GitHub Actions
    ↓
Setup Python
    ↓
Install Dependencies
    ↓
Run Automated Tests
    ↓
Test Result
   ↙       ↘
PASS       FAIL
 🟢         🔴

⚙️ GitHub Actions Workflow

The workflow file is located at:

.github/workflows/python-ci.yml

The workflow performs the following tasks:

1. Checkout Code

GitHub Actions gets the latest project code from the repository.

2. Setup Python

The pipeline tests the project using:

Python 3.11

Python 3.12

Python 3.13

3. Install Dependencies

Dependencies are installed using:

pip install -r requirements.txt

4. Dependency Caching

The workflow uses pip dependency caching to make future workflow runs more efficient.

5. Run Automated Tests

The pipeline runs:

pytest

If all tests pass, the workflow becomes successful.

📦 Requirements

Project dependencies are listed in requirements.txt.

Currently, the project uses:

pytest

🧠 What I Learned

Through this project, I learned:

Python project structure

Git basics

GitHub repository management

Git commits and pushes

Automated testing with pytest

GitHub Actions

YAML workflow configuration

Continuous Integration

Matrix testing

Multiple Python versions

Dependency management with pip

pip dependency caching

CI failure debugging

GitHub workflow monitoring

Project documentation

🐞 CI Failure Testing

As part of learning CI, an intentional error was introduced into the Python code.

The GitHub Actions pipeline detected the failed test and reported a failure.

After correcting the code, the pipeline was run again and successfully passed.

This demonstrated the complete CI feedback cycle:

Code Change
    ↓
CI Test
    ↓
❌ Failure
    ↓
Identify Error
    ↓
Fix Code
    ↓
Push Changes
    ↓
✅ CI Success

🚀 Future Improvements

The project can be extended with:

Code linting

Test coverage

More unit tests

Python package building

Continuous Delivery

Automatic deployment

Docker integration

Cloud deployment

📊 Project Status

Status: Completed ✅

The current project successfully implements a basic Python Continuous Integration pipeline using GitHub Actions.

The pipeline automatically tests the project using multiple Python versions.

👩‍💻 Author

Samruddhi Hankare

AI and Data Science Engineering Student