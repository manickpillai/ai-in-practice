# Testing Overview

Testing gives confidence that software behaves as intended and keeps working as it changes.

## Why we test

Tests catch regressions early, document expected behaviour and make refactoring safer.

## The test pyramid

Many fast unit tests, fewer integration tests, and a small number of end-to-end tests.

## Test naming conventions

Name tests after the behaviour, for example `test_login_fails_with_wrong_password`.

## Running the test suite

Run all tests with `pytest`. Use `pytest -k name` to run a subset.
