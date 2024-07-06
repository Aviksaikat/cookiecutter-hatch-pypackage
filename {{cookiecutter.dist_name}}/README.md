# {{cookiecutter.project_name}}


<div align="center">

| Feature       | Value                     |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Technology    | [![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)](https://www.python.org/) [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) [![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white)](https://github.com/features/actions) [![Pytest](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=flat&logo=Pytest&logoColor=white)]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/actions/workflows/tests.yml/badge.svg)                           |
| Type Checking | [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CI/CD         | [![Release]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/actions/workflows/release.yml/badge.svg)]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/actions/workflows/build.yml) [![Tests]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/actions/workflows/tests.yml/badge.svg)]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/actions/workflows/tests.yml) [![Labeler]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/actions/workflows/labeler.yml/badge.svg)]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/actions/workflows/labeler.yml) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit) [![codecov](https://codecov.io/gh/Ankvik-Tech-Labs/{{cookiecutter.project_name}}/graph/badge.svg?token=ISTIW37DO6)](https://codecov.io/gh/Ankvik-Tech-Labs/{{cookiecutter.project_name}})                                                                                                                                                                                                           |
| Docs          | [![Docs]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/actions/workflows/documentation.yml/badge.svg)]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/actions/workflows/build.yml)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Package       | [![PyPI - Version](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)](https://pypi.org/project/{{cookiecutter.project_name}}/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}})](https://pypi.org/project/{{cookiecutter.project_name}}/) [![PyPI - License](https://img.shields.io/pypi/l/{{cookiecutter.project_name}})](https://pypi.org/project/{{cookiecutter.project_name}}/)                                                                                                                                                                                                                                                                                                                                                                                                        |
| Meta          | [![GitHub license](https://img.shields.io/github/license/Ankvik-Tech-Labs/{{cookiecutter.project_name}}?style=flat&color=1573D5)]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/blob/main/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/Ankvik-Tech-Labs/{{cookiecutter.project_name}}?style=flat&color=1573D5)]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/commits/main) [![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Ankvik-Tech-Labs/{{cookiecutter.project_name}}?style=flat&color=1573D5)]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}/graphs/commit-activity) [![GitHub top language](https://img.shields.io/github/languages/top/Ankvik-Tech-Labs/{{cookiecutter.project_name}}?style=flat&color=1573D5)]({{cookiecutter.repository_url}}{{cookiecutter.project_name}}) |

</div>

---

# Description

{{cookiecutter.project_short_description}}

# Installation

- Install using `pip`
```py
pip install {{cookiecutter.dist_name}}
```

# Usage

TODO


---

**Documentation**: <a href="{{cookiecutter.docs_url}}" target="_blank">{{cookiecutter.docs_url}}</a>

**Source Code**: <a href="{{cookiecutter.repository_url}}" target="_blank">{{cookiecutter.repository_url}}</a>

---

<details close>
<summary>Development</summary>
<br>


## Development

### Setup environment

We use [Hatch](https://hatch.pypa.io/latest/install/) to manage the development environment and production build. Ensure it's installed on your system.

### Run unit tests

You can run all the tests with:

```bash
hatch run test
```

### Format the code

Execute the following command to apply linting and check typing:

```bash
hatch run lint
```

### Publish a new version

You can bump the version, create a commit and associated tag with one command:

```bash
hatch version patch
```

```bash
hatch version minor
```

```bash
hatch version major
```

Your default Git text editor will open so you can add information about the release.

When you push the tag on GitHub, the workflow will automatically publish it on PyPi and a GitHub release will be created as draft.

## Serve the documentation

You can serve the Mkdocs documentation with:

```bash
hatch run docs-serve
```

It'll automatically watch for changes in your code.


</details>


## License

This project is licensed under the terms of the {{cookiecutter.open_source_license}}.
