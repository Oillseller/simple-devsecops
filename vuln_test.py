## vuln_test.py

# Hardcoded password example (這個會被 Semgrep 抓到)
def login():
    username = "admin"
    password = "123456"  # Sensitive hardcoded credential
    print(f"Logging in with {username}/{password}")

if __name__ == "__main__":
    login()
