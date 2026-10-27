# Git commands for the assignment

## Part B - first push
    git init
    git branch -M main
    git remote add origin https://github.com/<username>/mlops-cicd.git
    git add .
    git commit -m "Initial ML project"
    git push -u origin main

(Or: clone the empty repo with `git clone https://github.com/<username>/mlops-cicd.git`,
copy these files into it, then git add / commit / push origin main.)

## Part E - workflow push (only if you add the workflow separately)
    git add .github/workflows/ci-cd.yml
    git commit -m "Add MLOps CI/CD pipeline"
    git push origin main

## Part F - failure scenario
NOTE: with this dataset/split, LogisticRegression gets accuracy = 1.0000,
so `assert accuracy >= 0.99` would still PASS. To make the test fail, use:

    assert accuracy >= 1.01

Then:
    git add tests/test_model.py
    git commit -m "Break test to demo failure"
    git push origin main
-> Actions shows Test FAILED and Deploy SKIPPED.

Restore:
    assert accuracy >= 0.80
    git add tests/test_model.py
    git commit -m "Restore test"
    git push origin main
-> Pipeline is green again.
