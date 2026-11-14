# Contributing

Thank you for considering a contribution to NEXORA.

## Before you start

- Search existing issues before opening a duplicate.
- For significant changes, open an issue to discuss the proposed direction.
- Keep pull requests focused and explain the motivation and user-visible impact.

## Development setup

```bash
git clone https://github.com/jsjshsbehjejwkwkaosoj828/NEXORA.git
cd NEXORA
python -m venv .venv
pip install -e ".[dev]"
```

## Quality checks

```bash
pytest
python -m compileall nexora tests
ruff check .
```

## Pull request checklist

- [ ] The change has a clear purpose.
- [ ] Tests cover relevant behavior.
- [ ] Documentation is updated.
- [ ] No credentials, local databases, or generated artifacts are committed.
- [ ] The change does not claim unfinished functionality.

## Code style

- Prefer readable, explicit Python.
- Use type hints for public interfaces where practical.
- Keep persistence logic out of UI widgets.
- Use parameterized SQL.
- Avoid unnecessary dependencies.

By participating, you agree to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
