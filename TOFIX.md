# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `pyproject.toml:91-95` - a `[[tool.mypy.overrides]]` block sets `ignore_missing_imports` for `pyfakeuse.*`, the package's own first-party module (the comment above it says "Third-party libraries without type stubs"); it is a config-level ignore that hides nothing real - delete the override block.
- `rsconstruct.toml:28` and `rsconstruct.toml:32` - `ruff` and `mypy` list `config` in `src_dirs`, but `config/` holds only `.lua` files; drop `config` so the src_dirs name only folders that contain Python.

## Low

- `pyproject.toml:86` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/`, which do not exist in this repo; reduce it to `src`.
- `src/pyfakeuse/pyfakeuse.py:3-7` - the comment says "The next line is needed ... the "p" parameter", but the parameter is `_p` (the leading underscore already silences unused-argument warnings); reword (or drop) the comment so it matches the code.
- `pyproject.toml:29` - classifier `Environment :: Console` is wrong for a pure library with no `[project.scripts]` entry point; remove it.
- `tests/unit_tests/test_basic.py:20-28` - the only tests are import checks; nothing ever calls `fake_use` (e.g. with no args, positional args, keyword-free varargs) - add a behavioural test.
