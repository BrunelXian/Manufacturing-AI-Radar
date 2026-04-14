# Additive Manufacturing References

## Domain Introduction

This section covers papers on AI methods for additive manufacturing process intelligence, especially work that connects sensing, defect formation, process modelling, material response, and decision-making.

Additive manufacturing is one of the strongest entry points for manufacturing AI because it produces rich thermal and geometric process data while remaining highly sensitive to process parameters. That makes it a natural domain for monitoring, prediction, surrogate modelling, defect reasoning, and eventually closed-loop control.

The most useful papers here are not generic ML applications with an additive-manufacturing label attached. They are papers that help explain, predict, or improve the physical process itself.

## Subcategories

- Melt-pool monitoring and multimodal sensing
- Physics-informed process and material modelling
- Defect reasoning and quality inference
- Decision support and control-oriented optimisation

## How Papers Are Curated Here

Entries are selected for manufacturing-process relevance, technical clarity, and usefulness to the radar. Priority is given to papers that connect AI methods to process physics, sensing, defect formation, or real manufacturing decisions.

## Curated Entries

### Multimodal learning of melt pool dynamics in laser powder bed fusion

**Authors:** Satyajit Mojumder, Pallock Halder, Tiana Tonge  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2509.03029v1

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Multimodal learning, transfer learning  
**Problem addressed:** Predicting melt-pool dynamics from sensing signals with different fidelity and cost  
**Inputs / modalities:** High-speed X-ray data and photodiode absorptivity signals  
**Method summary:** The paper combines CNN-based spatial feature extraction with recurrent temporal modelling in an early-fusion architecture. The high-fidelity X-ray stream is used to improve learning and then support transfer to lower-cost sensing.  
**Why it matters:** This is exactly the kind of work that matters for practical additive-manufacturing intelligence: it addresses the gap between rich scientific sensing and deployable industrial sensing.  
**Limitations / caution:** The strongest signals come from X-ray data that most production systems do not have, so deployment value depends on how well the transfer setup generalizes to cheaper sensors.

### Physics-guided denoiser network for enhanced additive manufacturing data quality

**Authors:** Pallock Halder, Satyajit Mojumder  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2508.02712v1

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Physics-guided representation learning, data denoising  
**Problem addressed:** Recovering usable process signals from noisy thermal sensing data  
**Inputs / modalities:** Thermal emission data guided by a PINN surrogate of the LPBF process  
**Method summary:** The authors introduce a denoising framework that combines learned denoising with physics-based regularization so that cleaned signals remain consistent with process behavior.  
**Why it matters:** High-quality sensing is a precondition for monitoring and control. This paper is useful because it focuses on an often overlooked upstream problem: whether the process data are reliable enough for downstream intelligence at all.  
**Limitations / caution:** It is an enabling method rather than a full manufacturing decision system, and transfer across machines or materials is still an open question.

### Physics-Informed Machine Learning Regulated by Finite Element Analysis for Simulation Acceleration of Laser Powder Bed Fusion

**Authors:** R. Sharma, M. Raissi, Y. B. Guo  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2506.20537v2

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Physics-informed learning, surrogate modelling  
**Problem addressed:** Accelerating thermal-field simulation while preserving the fidelity needed for process understanding  
**Inputs / modalities:** FEA-generated process data with temperature-dependent material and phase-change information  
**Method summary:** The paper proposes an FEA-regulated PINN workflow that keeps the model tied to physically meaningful LPBF behavior while reducing the computational burden of repeated simulation.  
**Why it matters:** This is a strong representative modelling paper because surrogate acceleration is central to parameter exploration, digital twins, and control-oriented prediction in additive manufacturing.  
**Limitations / caution:** It remains closer to simulation acceleration than to direct shop-floor deployment, so the operational value depends on how well the surrogate handles real process variability.

### Physics-Informed Mixture Models and Surrogate Models for Precision Additive Manufacturing

**Authors:** Sebastian Basterrech, Shuo Shan, Debabrata Adhikari, Sankhya Mohanty  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2510.26586v2

**Manufacturing domain:** Directed Energy Deposition and Laser Powder Bed Fusion  
**AI category:** Physics-guided defect modelling, mixture modelling  
**Problem addressed:** Identifying defect-related process patterns while remaining sensitive to meaningful physical variation  
**Inputs / modalities:** Real additive-manufacturing process datasets with alloy and parameter information  
**Method summary:** The paper uses a mixture-model framework informed by process physics to separate meaningful process behaviors and support defect analysis across multiple AM settings.  
**Why it matters:** It is a useful bridge paper between pure statistical detection and manufacturing-aware quality reasoning.  
**Limitations / caution:** The abstract suggests promising defect sensitivity, but the exact interpretability and deployment workflow still need close reading before treating it as a mature industrial method.

### PiGRAND: Physics-informed Graph Neural Diffusion for Intelligent Additive Manufacturing

**Authors:** Benjamin Uhrich, Tim Hantschel, Erhard Rahm  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.15194v1

**Manufacturing domain:** Intelligent additive manufacturing  
**AI category:** Physics-informed graph learning, diffusion modelling  
**Problem addressed:** Learning heat-transport behavior with limited sensing and expensive data collection  
**Inputs / modalities:** Graph-structured process representations derived from heat-transport settings  
**Method summary:** The paper develops a graph neural diffusion framework inspired by numerical diffusion schemes, with the goal of modelling heat transport more efficiently than direct high-cost simulation.  
**Why it matters:** It represents a valuable direction for manufacturing AI: graph-based models that are not only data-driven, but structurally informed by the underlying process physics.  
**Limitations / caution:** The value for manufacturing readers depends on how closely the graph construction matches real industrial sensing and whether the framework generalizes across process setups.

### Predicting Stress-strain Behaviors of Additively Manufactured Materials via Loss-based and Activation-based Physics-informed Machine Learning

**Authors:** Chenglong Duan, Dazhong Wu  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.14489v1

**Manufacturing domain:** Additively manufactured polymers and metals  
**AI category:** Physics-informed sequence modelling  
**Problem addressed:** Predicting stress-strain response from additive-manufacturing process conditions while preserving physical consistency  
**Inputs / modalities:** Process parameters and segmented stress-strain behavior  
**Method summary:** The paper combines regression and LSTM models, while embedding elastic and plastic constitutive laws directly into the learning process.  
**Why it matters:** This is important because additive manufacturing intelligence should not stop at melt-pool monitoring; it should connect process settings to material performance and qualification.  
**Limitations / caution:** It is more downstream than in-situ process intelligence, and its deployment value depends on dataset breadth across materials and machines.

### Towards Agentic Defect Reasoning: A Graph-Assisted Retrieval Framework for Laser Powder Bed Fusion

**Authors:** Muhammad Rizwan Awan, Volker Pickert, Muhammad Waqar Ashraf, Saleh Ali, Farshid Mahmouditabar, Shafiq Odhano  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2604.04208v1

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Knowledge-assisted defect reasoning, retrieval-augmented modelling  
**Problem addressed:** Structuring scattered LPBF defect knowledge into an interpretable reasoning framework  
**Inputs / modalities:** Literature-derived parameter-defect-mechanism relations  
**Method summary:** The paper turns publications into an evidence-linked knowledge graph and combines semantic retrieval with graph-based reasoning to trace parameter-to-defect pathways.  
**Why it matters:** This is less a process model than a research-knowledge infrastructure paper, but it is directly relevant to the radar because additive manufacturing defect understanding is still highly fragmented.  
**Limitations / caution:** It is not a real-time monitoring or control system, so it should be read as a knowledge-organization contribution rather than as an in-process manufacturing solution.

## Key Observations

- The strongest additive-manufacturing papers in the current pool concentrate on LPBF and adjacent metal AM settings.
- Physics-informed learning is a recurring theme, especially where direct simulation is too expensive or sensing is noisy.
- The most promising papers are those that connect sensing and modelling to defect formation or material behavior, rather than papers that only apply ML to a downstream prediction task.

## Current Gaps

- There are still too few clearly industrial closed-loop control papers in the current additive-manufacturing pool.
- The collection is stronger on modelling and monitoring than on validated decision-making systems.
- WAAM and large-scale deposition workflows remain underrepresented compared with LPBF.

## What Should Be Scanned Next

- in-situ defect prediction in LPBF and DED
- adaptive process control in additive manufacturing
- multimodal monitoring with low-cost industrial sensors
- qualification-oriented process-to-property modelling
