# Process Modelling References

## Domain Introduction

This section covers papers that model manufacturing process behavior, process-response relationships, or physically meaningful outcomes using AI or machine learning.

The key boundary here is that modelling papers should help explain or predict how a manufacturing process evolves. This section is not for generic materials informatics, generic optimization, or papers whose main contribution is only downstream decision policy. The best modelling papers in this repository are the ones that make manufacturing dynamics more computable, more interpretable, or more usable for later monitoring, optimisation, or control.

## Scope Boundary

Included here:

- surrogate models for thermal, geometric, or process-state prediction
- physics-informed or hybrid models of manufacturing behavior
- process-parameter to outcome models with clear physical relevance
- models of melt-pool, thermal-history, or material-response evolution

Usually excluded from this section:

- pure defect classification papers
- scheduling or resource-allocation models
- control papers whose main contribution is policy design rather than process modelling
- broad materials-property prediction work with weak process grounding

## Subcategories

- Surrogate modelling for thermal and process fields
- Physics-informed and hybrid process models
- Process-parameter to outcome prediction
- Reduced-order and long-horizon spatiotemporal models

## How Papers Are Curated Here

Priority goes to papers that model melt-pool behavior, thermal histories, microstructure evolution, stress-strain response, or other manufacturing-relevant process outcomes. The central question is whether the model helps us understand or compute the manufacturing process in a way that matters.

## Curated Entries

### Physics-Informed Machine Learning Regulated by Finite Element Analysis for Simulation Acceleration of Laser Powder Bed Fusion

**Authors:** R. Sharma, M. Raissi, Y. B. Guo  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2506.20537v2

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Physics-informed surrogate modelling  
**Problem addressed:** Replacing repeated high-cost thermal simulations with a faster but physically credible learned model  
**Inputs / modalities:** FEA-generated thermal process data with phase-change and material-property information  
**Method summary:** The paper introduces an FEA-regulated PINN that preserves key LPBF thermal physics while accelerating prediction and supporting transfer across process settings.  
**Why it matters:** This is a strong modelling paper because it targets the core bottleneck in manufacturing simulation: how to remain faithful to process physics without paying full numerical cost every time.  
**Limitations / caution:** It is still largely a simulation-side contribution, so practical value depends on how robustly it connects to real process measurements.

### Physics-informed machine learning surrogate for scalable simulation of thermal histories during wire-arc directed energy deposition

**Authors:** Michael Ryan, Mohammad Hassan Baqershahi, Hessamoddin Moshayedi, Elyas Ghafoori  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2507.09591v1

**Manufacturing domain:** Wire-arc directed energy deposition  
**AI category:** Physics-informed surrogate modelling  
**Problem addressed:** Predicting thermal histories at scales where repeated FEM simulation becomes impractical  
**Inputs / modalities:** Process conditions and thermal-history simulation data for WA-DED  
**Method summary:** The paper builds a physics-informed surrogate to approximate thermal evolution in large-scale deposition, aiming to preserve process relevance while making repeated simulation tractable.  
**Why it matters:** This is an important complement to LPBF-heavy modelling literature because large-scale DED and WAAM-like processes pose different computational and control challenges.  
**Limitations / caution:** The main evidence is still surrogate performance; downstream integration with planning or control is not yet the central contribution.

### A Fast and Generalizable Fourier Neural Operator-Based Surrogate for Melt-Pool Prediction in Laser Processing

**Authors:** Alix Benoit, Toni Ivas, Mateusz Papierz, Asel Sagingalieva, Alexey Melnikov, Elia Iseli  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2602.06241v3

**Manufacturing domain:** Laser processing and welding  
**AI category:** Operator learning, surrogate modelling  
**Problem addressed:** Predicting melt-pool geometry and temperature fields across laser-processing settings  
**Inputs / modalities:** Multiphysics simulation data reformulated in the moving-laser frame  
**Method summary:** The paper uses a Fourier Neural Operator to learn the parametric solution operator for melt-pool fields, reducing the cost of exploring process settings compared with high-fidelity simulation alone.  
**Why it matters:** Melt-pool behaviour is one of the core process states behind defect formation and quality. A fast surrogate in this space has clear value for exploration, digital twins, and later control.  
**Limitations / caution:** It remains model-centric; industrial usefulness depends on whether the learned operator retains accuracy under broader experimental variability.

### PiGRAND: Physics-informed Graph Neural Diffusion for Intelligent Additive Manufacturing

**Authors:** Benjamin Uhrich, Tim Hantschel, Erhard Rahm  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.15194v1

**Manufacturing domain:** Intelligent additive manufacturing  
**AI category:** Physics-informed graph modelling  
**Problem addressed:** Modelling heat transport under limited data and high sensing cost  
**Inputs / modalities:** Graph-structured process representations linked to diffusion behavior  
**Method summary:** The paper builds a graph neural diffusion framework inspired by numerical schemes for continuous heat transport, aiming to improve efficiency while retaining physically meaningful dynamics.  
**Why it matters:** It represents a more structured direction for manufacturing modelling, where graph learning is shaped by the governing transport process instead of being treated as an unstructured black box.  
**Limitations / caution:** The exact fit between graph abstraction and real industrial process states still needs careful evaluation.

### Adaptive Uncertainty-Guided Surrogates for Efficient phase field Modeling of Dendritic Solidification

**Authors:** Eider Garate-Perez, Kerman Lopez de Calle-Etxabe, Oihana Garcia, Borja Calvo, Meritxell Gomez-Omella, Jon Lambarri  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.00093v1

**Manufacturing domain:** Additive-manufacturing-relevant solidification modelling  
**AI category:** Uncertainty-aware surrogate modelling  
**Problem addressed:** Reducing the computational cost of dendritic solidification modelling while preserving spatiotemporal predictive utility  
**Inputs / modalities:** Phase-field simulation data with adaptive uncertainty-guided sampling  
**Method summary:** The paper combines surrogate learning with uncertainty-guided sampling to focus expensive simulation effort where model uncertainty is highest.  
**Why it matters:** This is useful because microstructure-sensitive manufacturing depends on process models that can capture solidification dynamics without collapsing under computational cost.  
**Limitations / caution:** It sits near the boundary between manufacturing process modelling and computational materials modelling, so its relevance comes from solidification control rather than from generic microstructure prediction.

### Stable Long-Horizon Spatiotemporal Prediction on Meshes Using Latent Multiscale Recurrent Graph Neural Networks

**Authors:** Lionel Salesses, Larbi Arbaoui, Tariq Benamara, Arnaud Francois, Caroline Sainvitu  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2602.18146v1

**Manufacturing domain:** Additive manufacturing  
**AI category:** Long-horizon spatiotemporal modelling  
**Problem addressed:** Predicting full temperature histories on complex geometries over long horizons without unstable rollout  
**Inputs / modalities:** Geometry, process parameters, and mesh-based temperature-field states  
**Method summary:** The paper uses a multiscale latent recurrent graph architecture to model temperature evolution directly on meshes while maintaining stability over long prediction windows.  
**Why it matters:** Long-horizon thermal prediction is highly relevant for understanding defect formation and residual effects in additive manufacturing.  
**Limitations / caution:** As with many simulation-trained models, the key unanswered question is how much fidelity carries over under real manufacturing disturbances and sensor uncertainty.

### Predicting Stress-strain Behaviors of Additively Manufactured Materials via Loss-based and Activation-based Physics-informed Machine Learning

**Authors:** Chenglong Duan, Dazhong Wu  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.14489v1

**Manufacturing domain:** Additively manufactured polymers and metals  
**AI category:** Process-to-property modelling, physics-informed sequence modelling  
**Problem addressed:** Predicting stress-strain behavior from manufacturing conditions with more physical consistency than purely data-driven baselines  
**Inputs / modalities:** Process parameters and segmented stress-strain data  
**Method summary:** The paper combines regression and LSTM-based sequence models while embedding constitutive knowledge into the elastic and plastic regions of the response.  
**Why it matters:** This paper is important because manufacturing modelling should connect process settings to functional outcomes, not only to intermediate thermal states.  
**Limitations / caution:** It is downstream of the immediate process itself, so it should be read as process-to-property modelling rather than in-situ state modelling.

## Key Observations

- The current modelling pool is strongest in additive manufacturing, especially LPBF and deposition-related thermal modelling.
- Physics-informed and hybrid surrogate models clearly dominate the strongest entries.
- The best papers are those that keep a strong line of sight from process parameters to physically meaningful outcomes such as thermal fields, melt-pool behavior, solidification, or material response.

## Current Gaps

- There are still too few modelling papers tied directly to experimental monitoring data rather than simulated process fields.
- Machining, welding, and forming remain weaker than additive-manufacturing process modelling.
- Some potentially relevant papers sit uncomfortably between materials modelling and manufacturing process modelling, so boundary judgment remains important.

## What Should Be Scanned Next

- melt-pool and thermal-field models validated against in-situ sensing
- hybrid models linking process states to defects and microstructure
- reduced-order models for control-oriented manufacturing prediction
- modelling work outside additive manufacturing, especially welding and machining
