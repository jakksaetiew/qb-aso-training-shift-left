.DEFAULT_GOAL := help # when you run make, it defaults to printing available commands

.PHONY: conda-create-env
conda-create-env:
	conda env create -f environment.yaml

.PHONY: install
install:
	pip install .

.PHONY: develop
develop:
	pip install -e ".[dev,test,docs]"
	pre-commit install --install-hooks

.PHONY: lint
lint:
	pre-commit run -a --hook-stage manual

.PHONY: test
test:
	pytest

.PHONY: build-requirements
build-requirements:
	pip-compile -o requirements.txt \
		--resolver=backtracking \
		--no-emit-find-links \
		--no-emit-index-url \
		pyproject.toml
	pip-compile --extra dev,test,docs \
		-o requirements.txt \
		--resolver=backtracking \
		--no-emit-find-links \
		--no-emit-index-url \
		pyproject.toml

.PHONY: build-docs
build-docs:
	jupyter-book clean -a docs
	jupyter-book build docs/src --path-output docs
	jupyter-book build -W --keep-going docs/src --path-output docs --builder linkcheck

.PHONY: clean
clean:
	rm -rf build dist docs/_build pip-wheel-metadata
	rm .coverage
	find . -regex ".*/.mypy_cache" -exec rm -rf {} +
	find . -regex ".*/.pytest_cache" -exec rm -rf {} +
	find . -regex ".*/__pycache__" -exec rm -rf {} +
	find . -regex ".*\.egg-info" -exec rm -rf {} +
	jupyter-book clean -a docs
	pre-commit clean || true
