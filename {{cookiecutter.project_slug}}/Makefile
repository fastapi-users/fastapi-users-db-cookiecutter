isort:
	isort ./{{ cookiecutter.package_name }} ./tests

format: isort
	black .

test:
	pytest --cov={{ cookiecutter.package_name }}/ --cov-report=term-missing --cov-fail-under=100

bumpversion-major:
	bumpversion major

bumpversion-minor:
	bumpversion minor

bumpversion-patch:
	bumpversion patch
