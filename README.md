# Simple DevSecOps Demo

This is a basic DevSecOps demonstration project designed to showcase:

- A simple Python app (`app.py`)
- GitHub Actions workflow for automated security scanning using Semgrep
- Automation of security checks on every push or pull request

## Project Structure

- `app.py`: A minimal Python web app with a simple vulnerability (command injection) for testing.
- `.github/workflows/semgrep.yml`: GitHub Actions workflow to automatically scan code with Semgrep.

## How It Works

1. When code is pushed to the `main` branch, GitHub Actions automatically triggers Semgrep.
2. Semgrep scans the codebase for security vulnerabilities.
3. Scan results are shown in the GitHub Actions workflow output.

## Purpose

This project demonstrates the integration of **security checks** into the **CI/CD pipeline** early in the development process ("shift-left" security).

## Future Improvements

- Add additional security tools (e.g., Bandit, Trivy)
- Expand Python app complexity
- Introduce containerization and infrastructure as code (IaC) scanning

