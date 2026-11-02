# Test Data

Good test data makes tests readable and repeatable.

## Fixtures

Fixtures create reusable setup, such as a logged-in user or a seeded database.

## Factories and builders

Factories generate objects with sensible defaults so each test overrides only what matters.

## Handling sensitive data

Never copy production data into tests. Use synthetic or anonymised data.

## Cleaning up after tests

Roll back transactions or delete created records so tests do not affect each other.
