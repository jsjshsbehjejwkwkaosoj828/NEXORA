# Data and Privacy

## Local-first storage

The current NEXORA foundation uses SQLite for application data. The application creates its database inside the operating system's user-data directory.

## Data categories

| Data | Stored fields |
| --- | --- |
| Tasks | Title, details, completion state, creation time |
| Notes | Title, body, creation time |
| Focus sessions | Completed duration, completion time |

## Network behavior

The current application foundation does not require an online account or NEXORA cloud service for its core workflows. Dependency installation and repository access require network access outside the application's local data layer.

## User responsibilities

- Protect access to the device account where NEXORA is installed.
- Back up the local database before reinstalling or moving the application.
- Do not place passwords, recovery codes, or secrets in notes.

## Future changes

Any future synchronization, telemetry, or account feature must be documented before release, including what is transmitted, why, and how users can control it.
