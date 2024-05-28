"""{{cookiecutter.project_short_description}}"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{ cookiecutter.dist_name }}")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
