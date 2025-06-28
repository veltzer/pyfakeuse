""" python deps for this project """

config_requires: list[str] = [
    "pyclassifiers",
]
build_requires: list[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
]
requires = config_requires + build_requires + test_requires
