# Cookiecutter Hatch PyPackage

Cookiecutter template for a cutting-edge Python package: `Hatch`, `ruff`, `mypy`, `GitHub Actions` and more!


|         |                                    |
|---------|------------------------------------|
| Details | [![License - MIT][MIT-image]][MIT-link] [![GitHub Sponsors][sponsor-image]][sponsor-link] |
| Features | [![Hatch project][hatch-image]][hatch-link] [![linting - Ruff][ruff-image]][ruff-link] [![types - mypy][mypy-image]][mypy-link] [![test - pytest][pytest-image]][pytest-link] [![Github Actions][github-actions]][precommit-link]  [![linting - precommit][precommit-image]][precommit-link] [![docs - mkdocs][mkdocs-image]][mkdocs-link] |



## ✨ Features

* [X] Lightweight starter
* [X] [`Hatch`](https://hatch.pypa.io/latest/install/) package management
* [X] [hatch-vcs]: determine the package version automatically from git tags, e.g. `v0.9`
* [X] Linting and formatting with [`ruff`](https://github.com/charliermarsh/ruff) which replaces [isort], [flake8], [black], etc.
* [X] Type checking with [`mypy`](https://github.com/python/mypy)
* [X] Check unused, missing and transitive dependencies with [`deptry`](https://deptry.com/)
* [X] Unit tests with [`pytest`](https://github.com/pytest-dev/pytest) with optional asyncio setup.
* [X] Automate and standardize testing with [Hatch-env-matrices]
* [X] Documentation with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and docstring reference support with [mkdocstrings](https://mkdocstrings.github.io/).
* [X] Ready-to-use [GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions) pipelines with `dependabot`, `release-drafter`, `labeler`, `publish to PYPI workflows`, `publish to test PYPI workflows` & more.
* [X] [hatch-pip-compile]: *experimental* support for lock-files,
* [X] [pyproject.toml]: all package, build and tool configuration in one file,
* [X] [coverage]: tool for measuring code coverage of Python programs with pytest integration,
* [X] [pre-commit]: pre-commit git hooks that make your life easier,
* [X] [Markdown]: instead of reStructuredText, Markdown is used consistently for all text files,
* [X] [EditorConfig]: maintain consistent coding styles for multiple developers,
* [X] [src-layout]: the actual Python package is kept under a `src` folder avoiding many common errors.

## 💫 Quickstart

Generate the project:

```bash
cookiecutter https://github.com/Aviksaikat/cookiecutter-hatch-pypackage
```

The generator will automatically call `hatch env create & git init` at the end.

Then, for the `GitHub Actions pipelines` to work correctly, you should:

* Enable the GitHub repository in `Codecov`.
* Set `CODECOV_TOKEN` in your GitHub repository secrets. You can find in the Codecov settings of the corresponding project.
* Enable `GitHub Pages` using the `GitHub Actions` source.
* Option to publish to Test [`PyPI`](https://test.pypi.org/) for testing.
* Configure the [Trusted Publisher method on PyPI](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/): it's a modern and secure method to push your package to PyPI.

### With cruft

[cruft](https://github.com/cruft/cruft) is a layer above Cookiecutter allowing you to update your project from the template after it has been generated.

```bash
cruft create https://github.com/Aviksaikat/cookiecutter-hatch-pypackage
```

## Demo
![](./media/demo.gif)


## License

This project is licensed under the terms of the [MIT](https://github.com/Aviksaikat/cookiecutter-hatch-pypackage/blob/main/LICENSE) license.



[cookiecutter]: https://cookiecutter.readthedocs.io/
[hatch-vcs]: https://github.com/ofek/hatch-vcs
[github-actions]: https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white
[Hatch-env-matrices]: https://hatch.pypa.io/dev/config/environment/advanced/#matrix
[hatch-pip-compile]: https://github.com/juftin/hatch-pip-compile
[cookiecutter-pypackage]: https://github.com/audreyfeldroy/cookiecutter-pypackage
[pre-commit]: https://pre-commit.com/
[mkdocs]: https://www.mkdocs.org/
[Markdown]: https://www.markdownguide.org/
[src-layout]: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
[flake8]: https://pypi.org/project/flake8/
[isort]: https://pycqa.github.io/isort/
[pytest]: https://docs.pytest.org/
[coverage]: https://coverage.readthedocs.io/
[mypy]: https://mypy-lang.org/
[black]: https://black.readthedocs.io/
[ruff]: https://beta.ruff.rs/
[EditorConfig]: http://editorconfig.org/
[Typer]: https://typer.tiangolo.com/
[pyproject.toml]: https://hatch.pypa.io/latest/config/metadata/
[pipenv]: https://pipenv.pypa.io/
[poetry]: https://python-poetry.org/
[conda]: https://docs.conda.io/
[virtualenv]: https://virtualenv.pypa.io/
[vanilla Python project]: https://github.com/aviksaikat/the-hatchlor-demo
[`README.md`]: https://github.com/aviksaikat/the-hatchlor-demo

[Tests-image]: https://github.com/aviksaikat/the-hatchlor/actions/workflows/run-tests.yml/badge.svg?branch=main
[Tests-link]: https://github.com/aviksaikat/the-hatchlor/actions/workflows/run-tests.yml
[hatch-image]: https://img.shields.io/badge/%F0%9F%A5%9A-hatch-4051b5.svg
[hatch-link]: https://github.com/pypa/hatch
[ruff-image]: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff-link]: https://github.com/charliermarsh/ruff
[mypy-image]: https://img.shields.io/badge/Types-mypy-blue.svg
[mypy-link]: https://mypy-lang.org/
[pytest-image]: https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white
[pytest-link]:  https://docs.pytest.org/
[mkdocs-image]: https://img.shields.io/badge/Docs-mkdocs-blue.svg
[mkdocs-link]: https://www.mkdocs.org/
[precommit-image]: https://img.shields.io/badge/Linting-pre--commit-red.svg
[precommit-link]:  https://pre-commit.com/
[MIT-image]: https://img.shields.io/badge/License-MIT-9400d3.svg
[MIT-link]: LICENSE
[sponsor-image]: https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=ff69b4
[sponsor-link]: https://github.com/sponsors/aviksaikat