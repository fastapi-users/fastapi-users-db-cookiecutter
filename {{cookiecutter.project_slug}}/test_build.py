# flake8: noqa
import sys

try:
    from {{ cookiecutter.package_name }} import {{ cookiecutter.db_adapter_class_name }}
except:
    sys.exit(1)

sys.exit(0)
