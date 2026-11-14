<!-- NEXORA · Project README -->
<div align="center">

# ◈ N E X O R A

### A focused workspace for everything that moves your day forward.

**Plan clearly. Capture ideas. Focus deeply. Understand your progress.**

<p>
  <img src="https://img.shields.io/badge/status-active%20development-8b5cf6?style=for-the-badge" alt="Active development">
  <img src="https://img.shields.io/badge/version-0.1.0-64748b?style=for-the-badge" alt="Version 0.1.0">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/UI-Kivy-00A6A6?style=for-the-badge" alt="Kivy">
  <img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge" alt="MIT License">
</p>

[Overview](#-overview) · [Features](#-capabilities) · [Quick Start](#-quick-start) · [Architecture](#-architecture) · [Roadmap](docs/ROADMAP.md) · [Contributing](CONTRIBUTING.md)

</div>

---

> [!NOTE]
> **NEXORA is under active development.** This repository currently establishes the application's modular foundation and its first local productivity workflows. Some advanced capabilities described in the roadmap are planned, not yet implemented.

## ◈ Overview

NEXORA is a modular, desktop-first productivity workspace built with **Python**, **Kivy**, and **SQLite**. It brings everyday planning tools into one calm, cohesive environment: tasks, notes, focused work sessions, and a compact overview of personal progress.

The project follows a **local-first** approach. Core information is stored in a local SQLite database, keeping the initial experience simple and independent of an online account or remote service.

### Design principles

| Principle | What it means |
| --- | --- |
| **Clarity over clutter** | A deliberate interface that prioritizes the next useful action. |
| **Local-first by default** | Core data stays in a local SQLite database. |
| **Modular architecture** | Screens, persistence, theme, and reusable widgets have clear boundaries. |
| **Honest capabilities** | Implemented features are distinguished from planned work. |
| **Room to grow** | The foundation is designed for incremental expansion. |

## ✦ Capabilities

- **Dashboard** — a concise snapshot of tasks and focus activity.
- **Task management** — create, complete, review, and remove tasks.
- **Quick notes** — capture and revisit short pieces of information.
- **Focus sessions** — a configurable Pomodoro-style timer with session tracking.
- **Local persistence** — SQLite storage initialized automatically.
- **Consistent interface** — shared theme tokens and reusable UI components.

## ⌘ Quick Start

### Requirements

- Python **3.10 or newer**
- pip
- A desktop environment supported by Kivy

### 1. Clone the repository

```bash
git clone https://github.com/jsjshsbehjejwkwkaosoj828/NEXORA.git
cd NEXORA
```

### 2. Create a virtual environment

**Windows**
```powershell
py -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Launch NEXORA

```bash
python main.py
```

The application creates its local database on first launch. The default database location is the user data directory selected by the application.

## ⌘ Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run the test suite:

```bash
pytest
```

Compile-check the Python modules:

```bash
python -m compileall nexora tests
```

## ◈ Architecture

NEXORA separates application startup, screen composition, reusable widgets, and data access. Screens use the database layer rather than issuing SQL directly.

```text
NEXORA/
├── main.py
├── nexora/
│   ├── app.py
│   ├── database.py
│   ├── theme.py
│   ├── screens/
│   │   ├── dashboard.py
│   │   ├── tasks.py
│   │   ├── notes.py
│   │   └── focus.py
│   └── widgets/
├── tests/
├── docs/
├── requirements.txt
└── pyproject.toml
```

For a deeper explanation, see [Architecture](docs/ARCHITECTURE.md).

## ◈ Data and privacy

- The initial release stores application data locally using SQLite.
- No account or cloud synchronization is required.
- No analytics or telemetry service is included in this foundation.
- Back up the local database file if its contents are important to you.

See [Data & Privacy](docs/DATA_AND_PRIVACY.md) for details.

## ⛭ Project status

| Area | Status |
| --- | --- |
| Application foundation | In progress |
| Local database | Implemented |
| Tasks and notes workflows | Initial implementation |
| Focus timer | Initial implementation |
| Automated tests | Initial coverage |
| Cloud synchronization | Planned |
| Data export and backup UI | Planned |
| Plugin system | Planned |
| Android packaging | Under evaluation |

## ✦ Roadmap

NEXORA is being developed incrementally. The roadmap tracks intended work without implying that future features are already available.

→ [Explore the roadmap](docs/ROADMAP.md)  
→ [Review the changelog](CHANGELOG.md)

## Contributing

Ideas, bug reports, and thoughtful improvements are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request and follow the community expectations in [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

NEXORA is released under the MIT License. See [LICENSE](LICENSE).

---

<div align="center">

**NEXORA** · Make room for meaningful progress.

<sub>Built with Python · Kivy · SQLite</sub>

</div>
