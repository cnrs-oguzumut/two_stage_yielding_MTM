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
├── two_stage_1.tex          # Main LaTeX document
├── formatted.bib            # Bibliography file
├── figures_ordering/        # Figure directory
│   ├── figure_01.png        # Poincaré disk tessellation
│   ├── figure_02.png        # Strain-energy visualization (tessellated)
│   ├── figure_03.png        # Strain-energy visualization (continuous)
│   ├── figure_04.pdf        # Finite element schematic
│   ├── figure_05.pdf        # MTM approach diagram
│   ├── figure_06.pdf        # Triangular elements illustration
│   ├── figure_07.pdf        # First stage yielding response
│   ├── figure_08.pdf        # Quasi-glassy state emergence
│   ├── figure_09.pdf        # Post-yield deformation history
│   ├── figure_10.pdf        # Microplasticity regime
│   ├── figure_11.pdf        # Second stage yielding (part 1)
│   ├── figure_12.pdf        # Second stage yielding (part 2)
│   ├── figure_13.pdf        # Grain boundary formation
│   ├── figure_14.pdf        # Multi-grain texture
│   ├── figure_15.pdf        # Mature shear bands
│   ├── figure_16.pdf        # Avalanche configurations
│   └── figure_17.pdf        # Energy drop statistics
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
