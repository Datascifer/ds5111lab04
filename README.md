# Setting Up a Linter and Tests for Your Code

This lab sets up `pylint` for code linting and `pytest` for testing. You'll create makefile jobs to automate both. The goal is clean, tested code — with a linter score as close to 10/10 as possible.

---

## 1. Install `pylint`

1. Add `pylint` to `requirements.txt` (if it's not already there):

```
pandas
lxml
pylint
```

2. Run:

```bash
make update
```

3. Activate your virtual environment:

```bash
source env/bin/activate
```

4. Confirm `pylint` is available:

```bash
pylint --version
```

---

## 2. Set Up `pylint` Config

1. Generate a config file:

```bash
pylint --generate-rcfile >> pylintrc
```

2. Test it's working:

```bash
pylint path/to/your_script.py
```

You should see style warnings (e.g. indentation, naming, docstrings).

3. To confirm it's reading your config, search in `pylintrc` for:

```
indent-string='    '
```

Change it to two spaces (`'  '`), re-run `pylint`, and observe the output. Change it back to four spaces afterward.

---

## 3. Add a `lint` Makefile Job

In your `Makefile`, add:

```make
lint:
	./env/bin/pylint your_module.py
```

Run it with:

```bash
make lint
```

---

## 4. Set Up `pytest`

1. Add `pytest` to `requirements.txt`:

```
pytest
```

2. Update environment:

```bash
make update
```

3. Create a `tests/` directory and a test file:

```bash
mkdir tests
touch tests/test_your_module.py
```

4. In `test_your_module.py`, add:

```python
import sys
sys.path.append('.')
import your_module  # replace with actual module

def test_example():
    assert 2 + 2 == 4  # Replace with a real test
```

5. Run tests:

```bash
pytest -vv tests
```

---

## 5. Add `test` Makefile Job

In `Makefile`, add:

```make
test: lint
	./env/bin/pytest -vv tests
```

This runs linting first, then tests.

---

## 6. Refactor, Fix, Commit

Repeat this cycle:

1. Run:

```bash
make test
```

2. Fix one issue (either linter or test)
3. Commit your work when you reach a stable state
4. Repeat until:

- All tests pass
- `pylint` reports `10.00/10`

---

## Notes

- Only `test_` functions will run under `pytest`
- `pylint` evaluates naming, structure, spacing, comments, and more
- Use `.gitignore` to exclude `env/`, `__pycache__/`, and `.pytest_cache/`

---

## References

- Pylint: https://pylint.readthedocs.io/en/latest/user_guide/
- Pytest: https://docs.pytest.org/en/stable/  
