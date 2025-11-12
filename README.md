# Two-Stage Yielding in Pristine Crystals: A Mesoscopic Tensorial Model Study

This repository contains the manuscript and figures for a scientific paper investigating quasi-brittle plastic yielding in pristine crystals using the Mesoscopic Tensorial Model (MTM) approach.

## Abstract

This work demonstrates that quasi-brittle yielding, typically associated with well-annealed glassy materials, also characterizes plastic yielding in model 2D perfect crystals. We show a two-stage yielding process where:

1. **Stage 1**: Massive dislocation nucleation converts pristine crystalline configurations into effectively glassy states
2. **Stage 2**: Quasi-brittle yielding behavior emerges, similar to that observed in pseudo-amorphous systems

The research bridges the gap between crystal plasticity and glass physics through avalanche statistics and demonstrates universal yielding behavior across different material states.

## Preprint

**arXiv preprint**: [arXiv:2511.08187](https://arxiv.org/abs/2511.08187)

## Authors

- **O.U. Salman** - LSPM, CNRS UPR3407, Université Sorbonne Paris Nord
- **A. Ahadi** - PMMH, CNRS UMR 7636 ESPCI PSL  
- **L. Truskinovsky** - PMMH, CNRS UMR 7636 ESPCI PSL

## Repository Structure

```
.
├── README.md                 # This file
├── two_stage_1.tex          # Main LaTeX manuscript
├── formatted.bib            # Bibliography file
└── figures_ordering/        # Directory containing all figures
    ├── figure_01.png        # Figures 1-3 in PNG format
    ├── figure_02.png
    ├── figure_03.png
    └── figure_04-17.pdf     # Figures 4-17 in PDF format
```

## Compilation Instructions

The manuscript is written in LaTeX using the RevTeX4-1 document class. To compile:

```bash
pdflatex two_stage_1.tex
bibtex two_stage_1
pdflatex two_stage_1.tex
pdflatex two_stage_1.tex
```

### Requirements

The document uses the following LaTeX packages:
- `revtex4-1` (document class)
- `graphicx` (figure inclusion)
- `amsmath`, `amsfonts`, `amssymb` (mathematical symbols)
- `subfigure` (subfigures)
- `natbib` (citations)
- `hyperref` (links)
- `mathrsfs` (script math fonts)

Ensure these packages are installed in your LaTeX distribution.

## Key Findings

- **Universal yielding behavior**: Perfect crystals exhibit yielding characteristics similar to glassy materials
- **Avalanche statistics**: The two-stage yielding process is characterized by distinctive avalanche patterns
- **Quasi-amorphous state**: Massive dislocation nucleation creates an effectively glassy state within the crystalline structure
- **MTM framework**: The Mesoscopic Tensorial Model successfully captures the transition from crystalline to glass-like yielding

## Mesoscopic Tensorial Model (MTM)

The MTM approach provides a unified computational framework for modeling:
- Plasticity through dislocation dynamics
- Fracture mechanics
- Phase transitions
- Material instabilities

This work specifically focuses on dislocation nucleation and avalanche phenomena during the yielding of pristine 2D crystals.

## Contact

For questions or collaboration inquiries, please contact:
- O.U. Salman (Corresponding author) - LSPM, CNRS

## License

This repository contains academic research materials. Please cite appropriately if you use this work.

## Citation

If you use this work in your research, please cite:

```bibtex
@article{salman2024twostage,
  title={Two-Stage Yielding in Pristine Crystals},
  author={Salman, O.U. and Ahadi, A. and Truskinovsky, L.},
  journal={arXiv preprint arXiv:2511.08187},
  year={2024},
  eprint={2511.08187},
  archivePrefix={arXiv},
  url={https://arxiv.org/abs/2511.08187}
}
```

---

**Note**: This is a working manuscript. Figures and content may be updated as the research progresses.
