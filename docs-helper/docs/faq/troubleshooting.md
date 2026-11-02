# Troubleshooting

Fixes for common problems.

## Tests pass locally but fail in CI

Check for differences in environment variables, time zones, dependency versions and test ordering.

## Tests are slow

Profile with `pytest --durations=10`, mock slow dependencies and run tests in parallel.

## Import errors when running tests

Make sure the package is installed in the active environment, for example with `uv sync`.

## mkdocs serve fails to start

Confirm dependencies are installed with `uv sync` and that port 8000 is free.
