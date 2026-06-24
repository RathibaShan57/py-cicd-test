# py-cicd-test

A minimal Python project used to validate CI/CD workflows — push, pull request, and commit triggers.

## Structure

```
py-cicd-test/
├── src/
│   └── calculator.py      # Core module
├── tests/
│   └── test_calculator.py # Pytest test suite
├── .github/
│   └── workflows/
│       └── ci.yml         # GitHub Actions CI
├── requirements.txt
└── setup.cfg
```

## Running tests locally

```bash
pip install -r requirements.txt
pytest tests/ --cov=src --cov-report=term-missing
```

## CI triggers

| Event | Workflow runs |
|---|---|
| Push to any branch | Yes |
| Pull request opened / updated | Yes |
| Commit pushed to main | Yes |
