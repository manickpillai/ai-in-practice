# Integration Testing

Integration tests verify that components work together, such as a service and its database.

## When to use integration tests

Use them for boundaries: database queries, API contracts, message queues and file systems.

## Setting up test environments

Use containers or an in-memory database, and reset state between tests.

## Testing APIs

Call endpoints with a test client and assert on status codes and response bodies.

## Flaky integration tests

Avoid fixed sleeps, isolate data per test, and retry only network-level failures.
