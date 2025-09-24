# Amorphous Crystals: Two-Stage Yielding of Pristine Crystals

A scientific paper investigating quasi-brittle plastic yielding in pristine crystals using mesoscopic tensorial modeling (MTM).

## Authors
- O.U. Salman (LSPM, CNRS UPR3407, Université Sorbonne Paris Nord)
- N. Gorbushin (PMMH, CNRS UMR 7636 ESPCI PSL)
- L. Truskinovsky (PMMH, CNRS UMR 7636 ESPCI PSL)

## Abstract
This paper demonstrates that quasi-brittle yielding, typically associated with well-annealed glassy materials, also characterizes plastic yielding in model 2D perfect crystals. The research shows a two-stage yielding process where massive dislocation nucleation converts crystalline configurations to effectively glassy states, followed by quasi-brittle yielding behavior similar to pseudo-amorphous systems.

## Repository Structure
.
├── two_stage_1.tex
├── formatted.bib
├── README.md
├── figures_ordering/
│   ├── figure_01.png
│   ├── figure_02.png
│   ├── figure_03.png
│   ├── figure_04.pdf
│   ├── figure_05.pdf
│   ├── figure_06.pdf
│   ├── figure_07.pdf
│   ├── figure_08.pdf
│   ├── figure_09.pdf
│   ├── figure_10.pdf
│   ├── figure_11.pdf
│   ├── figure_12.pdf
│   ├── figure_13.pdf
│   ├── figure_14.pdf
│   ├── figure_15.pdf
│   ├── figure_16.pdf
│   └── figure_17.pdf
└── (and other files as needed)
└── README.md               # This file

## Compilation Requirements

### LaTeX Packages
The document uses RevTeX4-1 with the following key packages:
- `revtex4-1` (document class)
- `graphicx` (figure inclusion)
- `amsmath`, `amsfonts`, `amssymb` (mathematical symbols)
- `subfigure` (subfigures)
- `natbib` (citations)
- `hyperref` (links)
- `mathrsfs` (script math fonts)

### Compilation Command
```bash
pdflatex two_stage_1.tex
bibtex two_stage_1
pdflatex two_stage_1.tex
pdflatex two_stage_1.tex
