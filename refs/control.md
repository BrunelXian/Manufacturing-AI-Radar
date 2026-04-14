# Closed-loop Control References

## Domain Introduction

This section covers papers where AI contributes to manufacturing decisions that change the process, rather than only observing or predicting it.

Closed-loop control is one of the hardest and most valuable areas in manufacturing AI because it requires models to be fast enough, reliable enough, and physically grounded enough to affect real actions. The current pool is still thinner here than in monitoring and modelling, so curation is intentionally selective.

## Subcategories

- Model predictive control with learned surrogates
- Reinforcement-learning-guided process decisions
- Physics-guided control-oriented optimisation

## How Papers Are Curated Here

Papers are included only if they clearly address process intervention, control-relevant optimisation, or real-time decision support. Pure monitoring or passive prediction papers are excluded unless they are directly embedded in a control loop.

## Curated Entries

### Real-Time Decision-Making for Digital Twin in Additive Manufacturing with Model Predictive Control using Time-Series Deep Neural Networks

**Authors:** Yi-Ping Chen, Vispi Karkaria, Ying-Kuan Tsai, Faith Rolark, Daniel Quispe, Robert X. Gao, Jian Cao, Wei Chen  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2501.07601v5

**Manufacturing domain:** Directed Energy Deposition additive manufacturing  
**AI category:** Model predictive control, surrogate modelling, digital twin  
**Problem addressed:** Real-time decision-making for a nonlinear additive-manufacturing process  
**Inputs / modalities:** Time-series process states processed by a TiDE deep neural surrogate  
**Method summary:** The paper builds a multi-step predictive surrogate and embeds it inside an MPC framework so that future process states can be predicted quickly enough for real-time control-oriented optimization.  
**Why it matters:** This is one of the clearest control papers in the current pool because it connects digital twins, learned prediction, and actual decision-making in an additive-manufacturing setting.  
**Limitations / caution:** The abstract supports a strong decision-support story, but deployment maturity depends on how robust the surrogate remains under real process drift and uncertainty.

### Laser Scan Path Design for Controlled Microstructure in Additive Manufacturing with Integrated Reduced-Order Phase-Field Modeling and Deep Reinforcement Learning

**Authors:** Augustine Twumasi, Prokash Chandra Roy, Zixun Li, Soumya Shouvik Bhattacharjee, Zhengtao Gan  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2506.21815v1

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Deep reinforcement learning, reduced-order modelling  
**Problem addressed:** Designing scan paths to steer microstructure outcomes instead of relying on manual trial-and-error  
**Inputs / modalities:** Reduced-order phase-field simulations and thermal-history-informed surrogate predictions  
**Method summary:** The work combines a phase-field model, a 3D U-Net surrogate, and deep reinforcement learning to optimize scan strategies for desired microstructure behavior.  
**Why it matters:** It is a strong example of control-oriented AI in manufacturing because the objective is not merely to predict quality, but to choose actions that shape it.  
**Limitations / caution:** The method is still simulation-driven, and the jump from optimized scan design to robust shop-floor control remains substantial.

### Physics-guided denoiser network for enhanced additive manufacturing data quality

**Authors:** Pallock Halder, Satyajit Mojumder  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2508.02712v1

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Control-enabling sensing, physics-guided preprocessing  
**Problem addressed:** Improving signal quality for downstream diagnostics and control  
**Inputs / modalities:** Noisy thermal emission data guided by a process surrogate  
**Method summary:** The paper uses physics-guided denoising so that thermal measurements become more useful for later decision-making tasks, especially where raw sensor noise would undermine action quality.  
**Why it matters:** It is included here because in manufacturing control, poor sensing often breaks the loop before controller design even begins. This is enabling rather than full closed-loop control, but still important.  
**Limitations / caution:** This is not a controller by itself and should be read as control-adjacent infrastructure.

### Physics-Informed Machine Learning Regulated by Finite Element Analysis for Simulation Acceleration of Laser Powder Bed Fusion

**Authors:** R. Sharma, M. Raissi, Y. B. Guo  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2506.20537v2

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Control-oriented surrogate modelling  
**Problem addressed:** Reducing simulation cost so that prediction can become practical for optimization and control workflows  
**Inputs / modalities:** FEA-driven thermal process data with dynamic material behavior  
**Method summary:** The paper develops an FEA-regulated PINN that keeps important LPBF thermal physics while making repeated predictive evaluation far cheaper than full simulation.  
**Why it matters:** Manufacturing control often depends on models that are accurate enough to trust but fast enough to optimize over. This paper sits directly in that enabling space.  
**Limitations / caution:** The contribution remains model-side rather than controller-side, so it should not be overstated as a solved feedback-control result.

## Key Observations

- The strongest control-related papers in the current pool are still additive-manufacturing centered.
- Learned surrogates appear repeatedly as the practical bridge between expensive physics and real-time decision-making.
- The pool currently contains more control-enabling infrastructure than mature closed-loop industrial demonstrations.

## Current Gaps

- There are too few papers with clear experimental closed-loop validation on manufacturing equipment.
- Welding, machining, and forming are underrepresented compared with additive manufacturing.
- Safe control under uncertainty remains much weaker in the current pool than monitoring and modelling.

## What Should Be Scanned Next

- model predictive control for additive manufacturing and welding
- adaptive control with in-situ sensing
- safe learning-based control under process uncertainty
- real-machine demonstrations rather than simulation-only optimization
