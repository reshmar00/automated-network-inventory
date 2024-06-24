# install-test.py
import ansible
import django
import dotenv

print(f"ansible version: {ansible.__version__}")
print(f"django version: {django.__version__}")

from importlib.metadata import version

try:
    dotenv_version = version('python-dotenv')
    print(f"python-dotenv version: {dotenv_version}")
except Exception as e:
    print(f"Failed to retrieve version for python-dotenv: {e}")
