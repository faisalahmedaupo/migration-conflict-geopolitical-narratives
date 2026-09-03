"""ACLED adapter placeholder.
ACLED API access requires an authorized account/token. Never hard-code credentials.
See docs and official API instructions before enabling this script.
"""
import os

def check_credentials():
    if not os.getenv("ACLED_ACCESS_TOKEN"):
        raise RuntimeError("Set ACLED_ACCESS_TOKEN after obtaining authorized ACLED API access.")
    print("ACLED token detected. Implement/query according to your account's current API permissions and terms.")

if __name__ == "__main__":
    check_credentials()
