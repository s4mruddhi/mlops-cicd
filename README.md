# MLOps CI/CD Pipeline using GitHub Actions

A simple Iris classification project (Logistic Regression) with an automated
CI/CD pipeline: **Code Commit -> Build -> Test -> Deploy**.

## Project structure
    mlops-cicd/
    ├── .github/workflows/ci-cd.yml   # GitHub Actions workflow
    ├── src/model.py                  # trains model, returns accuracy
    ├── tests/test_model.py           # unit test (accuracy >= 0.80)
    ├── requirements.txt
    ├── app.py
    └── README.md

## Run locally
    pip install -r requirements.txt
    python app.py
    pytest -v

## Pipeline
Triggered on every push or pull request to `main`.
1. **Test ML Application**: checkout, setup Python 3.11, install dependencies, run pytest.
2. **Deploy Application**: runs only if tests pass and the branch is `main` (deployment is simulated with `echo`).

If tests fail, deployment is skipped.
