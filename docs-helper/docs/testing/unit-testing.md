# Unit Testing

A unit test checks one small piece of code in isolation.

## Writing a good unit test

Arrange the inputs, act by calling the code, then assert on the result. Keep one concept per test.

```python
def test_add():
    assert add(2, 3) == 5
```

## Mocking dependencies

Replace databases, network calls and clocks with mocks or fakes so tests stay fast and deterministic.

### Mocking a database

Patch the repository or session object, or use an in-memory database, so no real connection is made.

### Mocking time

Inject a clock or freeze time so tests do not depend on the current date.

## Code coverage

Coverage shows which lines ran during tests. Use it to find gaps, not as a goal on its own.

## Common unit testing mistakes

Testing implementation details, sharing state between tests, and over-mocking.
