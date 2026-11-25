# Linear Algebra for AI and ML

A practical, notebook-driven study of the linear algebra foundations used in AI and machine learning.

## Scope

This repository covers ten connected topic groups: foundations; vector geometry; linear combinations and vector spaces; matrices; linear systems; transformations; subspaces, rank and null space; orthogonality and projections; eigenvalues and decompositions; and applications to AI/ML.

The curriculum contains **44 sub-topics** across these ten notebooks. Familiar topics remain included for continuity; prior knowledge changes the depth of revision, not the coverage.

## Repository map

| Notebook | Topic group |
|---|---|
| `010` | Linear Algebra Foundations |
| `020` | Vector Operations and Geometry |
| `030` | Linear Combinations and Vector Spaces |
| `040` | Matrices and Matrix Operations |
| `050` | Systems of Linear Equations |
| `060` | Linear Transformations |
| `070` | Subspaces, Rank and Null Space |
| `080` | Orthogonality and Projections |
| `090` | Eigenvalues and Matrix Decompositions |
| `100` | Linear Algebra for AI and ML |

See [`CURRICULUM_INDEX.md`](CURRICULUM_INDEX.md) for the detailed sub-topic index.

## Learning approach

Each notebook uses a consistent progression: motivation, intuition, mathematical foundations, derivation, worked example, NumPy verification, AI/ML connection, limitations and independent practice.

**Notebook completion is not evidence of mastery.** Competency must be demonstrated independently through explanation, derivation, calculation, interpretation and implementation where relevant.

## Setup

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
jupyter lab
```

## Practice scripts

Create your own `.py` practice files alongside the notebooks, using the same numeric prefix followed by `1` (or the agreed topic-specific sequence). For example:

- `010-linear-algebra-foundations.ipynb`
- `011-linear-algebra-foundations-practice.py`

Practice scripts are intentionally not pre-created; they are for independent implementation and experimentation.

## Scope boundary

The final notebook introduces the linear algebra behind embeddings, neural-network affine layers and Transformer Q/K/V projections. It does not replace the separate mathematics modules for calculus, probability, statistics, optimisation, deep learning or complete Transformer/LLM mathematics.
