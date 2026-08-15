# Python CI/CD Pipline 🚀

A beginner-friendly CI/CD mini project built using Python, pytest, GitHub, and GitHub Actions.

## Project Overview

This project demonstrates how Continuous Integration (CI) can automatically test Python code whenever changes are pushed to GitHub.

## Technologies Used

- Python
- pytest
- pip
- Git
- GitHub
- GitHub Actions
- YAML

## Project Structure

```text
python-cicd-project/
│
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
│
└── .github/
    └── workflows/
        └── python-ci.yml
**
# ## How CI pipline works**

Developer pushes code
        ↓
GitHub Repository
        ↓
GitHub Actions starts
        ↓
Setup Python
        ↓
Install dependencies
        ↓
Run automated tests
        ↓
Test Result
   ↙           ↘
PASS           FAIL
 🟢             🔴

🧪 Testing

This project uses pytest for automated testing.

# # **🔄 CI Workflow**

The GitHub Actions workflow performs the following steps:

1.Checks out the project code.
2.Sets up Python.
3.Tests the project with Python 3.11, 3.12, and 3.13.
4.Installs dependencies using pip.
5.Uses pip dependency caching.
6.Runs automated tests using pytest.
7.Reports whether the CI pipeline passed or failed. 
# **
📚 What I Learned**

Through this project, I learned:

*Python project structure
*Git and GitHub
*Git commits and branches
*Automated testing with pytest
*GitHub Actions
*YAML workflow configuration
*Continuous Integration
*Matrix testing with multiple Python versions
*Dependency management using pip
*pip dependency caching
*Debugging failed CI pipelines
*Writing project documentation

**# 🚀 Future Improvements**

1.Add code linting
2.Add test coverage
3.Add more unit tests
4.Build a Python package
5.Implement Continuous Delivery
6.Deploy the application automatically

**# 👩‍💻 Author**

Samruddhi Hankare

AI and Data Science Engineering Student