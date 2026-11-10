# Cognitive Twin: Personalized Algorithmic Ingestion & Execution Engine

An open-source framework and reference implementation for creating hyper-personalized AI cognitive twins from a baseline dataset tailored to a single user's problem-solving style, codebases, game telemetry, and epistemic history.

---

## Architecture & Subclasses

The repository is structured around modular subclasses that ingest multi-modal user data:

1. **`codebase_subclass/`**: Parses version control repositories (AST, modularity, error handling).
2. **`telemetry_subclass/`**: Captures real-time decision-making heuristics, risk tolerance, and structural triage bias.
3. **`epistemic_subclass/`**: Filters YouTube watch histories and streaming media logs by completion rate to build a knowledge graph and prevent redundant explanations.
4. **`lexical_subclass/`**: Performs stylometric analysis and intertextual mapping to match vocabulary density and tone.
5. **`aesthetic_subclass/`**: Profiles visual composition and music tempo/harmonic preferences.

---

## Repository Structure

```text
cognitive_twin/
├── README.md
├── requirements.txt
├── main.py
├── index.html
└── core/
    ├── __init__.py
    ├── ingester.py
    ├── behavioral_proxy.py
    └── epistemic_baseline.py
```

---

## Installation & Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/willwallace-rit/cognitive_twin.git
   cd cognitive_twin
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the engine:
   ```bash
   python main.py
   ```

---

## Web Ingestion Portal

Open `index.html` in any modern web browser to use the interactive dashboard for loading, auto-classifying, and exporting user behavioral data across all subclasses.

---

## License
MIT Open-Source License.
