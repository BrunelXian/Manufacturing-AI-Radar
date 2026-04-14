# Process Monitoring References

## Domain Introduction

This section covers papers on monitoring manufacturing processes through sensor streams, spatial measurements, soft sensors, and learned representations of process state.

Monitoring matters because manufacturing intelligence depends on visibility into what the process is doing now. Without reliable monitoring, prediction, diagnosis, and control remain weakly grounded. The most relevant papers here are those that improve state estimation, fault detection, interpretability, or deployable sensing workflows.

## Subcategories

- Multimodal and edge monitoring
- Causal and interpretable monitoring
- Soft sensing and feature selection
- Process-specific sensing pipelines

## How Papers Are Curated Here

Priority goes to papers that improve process observability in real manufacturing settings, especially when they address noisy sensing, deployment constraints, or interpretable fault diagnosis.

## Curated Entries

### Causal Graph Spatial-Temporal Autoencoder for Reliable and Interpretable Process Monitoring

**Authors:** Xiangrui Zhang, Chunyue Song, Wei Dai, Zheng Zhang, Kaihua Gao, Furong Gao  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2602.03004v1

**Manufacturing domain:** Industrial process monitoring  
**AI category:** Graph learning, spatial-temporal autoencoding, causal inference  
**Problem addressed:** Reliable and interpretable fault detection in multivariate industrial processes  
**Inputs / modalities:** Time-series process variables with learned correlation and causal structure  
**Method summary:** The paper combines graph structure learning with a graph-convolutional temporal encoder-decoder, then derives a causal graph to improve monitoring interpretability beyond simple correlation-based reconstruction.  
**Why it matters:** This is a strong generic process-monitoring paper because it goes beyond anomaly scores and tries to recover structure that process engineers can reason about.  
**Limitations / caution:** The work is process-industry oriented rather than tied to one discrete manufacturing process, so direct translation into shop-floor settings still requires contextual validation.

### Causal feature selection framework for stable soft sensor modeling based on time-delayed cross mapping

**Authors:** Shi-Shun Chen, Xiao-Yang Li, Enrico Zio  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2601.14099v1

**Manufacturing domain:** Industrial process monitoring  
**AI category:** Soft sensing, causal feature selection  
**Problem addressed:** Building more stable soft sensors under delayed and interdependent process relationships  
**Inputs / modalities:** Time-delayed industrial variables for soft-sensor estimation  
**Method summary:** The paper proposes a feature-selection pipeline based on time-delayed cross mapping, aiming to select variables that are causally useful rather than merely correlated.  
**Why it matters:** Soft sensors are central to manufacturing monitoring when direct measurement is expensive or impossible. This paper is valuable because it addresses stability, which is often the real bottleneck in deployment.  
**Limitations / caution:** The contribution is upstream in feature selection, so readers should not mistake it for a full monitoring stack by itself.

### Domain-Aware Hyperdimensional Computing for Edge Smart Manufacturing

**Authors:** Fardin Jalil Piran, Anandkumar Patel, Rajiv Malhotra, Farhad Imani  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2509.26131v1

**Manufacturing domain:** CNC machining and LPBF defect monitoring  
**AI category:** Edge AI, hyperdimensional computing  
**Problem addressed:** Balancing monitoring accuracy with latency and energy constraints on edge hardware  
**Inputs / modalities:** Signal-based monitoring data for machining and image-based LPBF defect data  
**Method summary:** The paper studies how hyperdimensional-computing design choices behave across different manufacturing monitoring tasks and shows that the same settings do not transfer cleanly across domains.  
**Why it matters:** Deployment constraints are often ignored in academic monitoring work. This paper is useful because it treats edge efficiency as a first-class manufacturing requirement.  
**Limitations / caution:** It is more about architectural efficiency trade-offs than about rich process semantics or defect physics.

### Security Risks in Machining Process Monitoring: Sequence-to-Sequence Learning for Reconstruction of CNC Axis Positions

**Authors:** Lukas Krupp, Rickmar Stahlschmidt, Norbert Wehn  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.01702v1

**Manufacturing domain:** Machining process monitoring  
**AI category:** Sequence modelling, industrial signal reconstruction  
**Problem addressed:** Reconstructing machine motion from monitoring signals and exposing security risks in process data  
**Inputs / modalities:** Accelerometer-based machining monitoring signals  
**Method summary:** The authors use LSTM-based sequence-to-sequence models to infer CNC axis and tool positions from monitoring data that would usually be treated only as condition signals.  
**Why it matters:** This paper is notable because it shows that monitoring data can encode far more process information than expected. That matters both for process observability and for industrial data-governance concerns.  
**Limitations / caution:** Its main contribution is risk exposure rather than process optimization, so it belongs here as an observability paper rather than as a direct quality-monitoring method.

### Topography scanning as a part of process monitoring in power cable insulation process

**Authors:** Janne Harjuhahto, Jaakko Harjuhahto, Mikko Lahti, Jussi Hanhirova, Bjorn Sonerud  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2602.06519v1

**Manufacturing domain:** Power cable insulation production  
**AI category:** Surface monitoring, defect detection with deep learning  
**Problem addressed:** Real-time surface and geometry monitoring for insulation quality  
**Inputs / modalities:** Topography scans and reconstructed 3D surface maps  
**Method summary:** The paper presents a monitoring pipeline that combines high-resolution topography scanning with deep-learning-based surface defect detection to inspect geometry and melt homogeneity-related errors.  
**Why it matters:** It is a good example of domain-specific monitoring where the sensing system and the ML layer are designed together for a real process.  
**Limitations / caution:** The process domain is narrower than the additive-manufacturing core of the repository, so it is most useful here as an example of deployable monitoring architecture.

### Multimodal learning of melt pool dynamics in laser powder bed fusion

**Authors:** Satyajit Mojumder, Pallock Halder, Tiana Tonge  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2509.03029v1

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Multimodal monitoring, representation learning  
**Problem addressed:** Estimating melt-pool dynamics by fusing high-fidelity and low-cost sensing streams  
**Inputs / modalities:** High-speed X-ray data and photodiode absorptivity signals  
**Method summary:** The work fuses spatial and temporal sensing streams to learn more informative melt-pool representations and then uses transfer learning to move toward lower-cost sensing.  
**Why it matters:** This is one of the strongest process-monitoring papers in the current pool because it directly addresses the gap between laboratory-grade observability and industrially deployable monitoring.  
**Limitations / caution:** The industrial relevance depends on whether the lower-cost sensing path retains enough fidelity once the high-end experimental sensor is removed.

## Key Observations

- The current monitoring pool is strongest when papers address interpretability, soft sensing, or deployment constraints rather than only raw detection accuracy.
- Process monitoring is emerging as a bridge domain between sensing and decision-making, especially when causal structure or multimodal fusion is used.
- Edge and industrial security considerations are appearing as first-class concerns, which is a useful sign of maturation.

## Current Gaps

- The current pool has fewer strong monitoring papers for welding and high-rate closed-loop manufacturing than for process industries and LPBF.
- There is still limited evidence of robust cross-machine generalization.
- Many monitoring papers remain observational rather than explicitly tied to downstream control.

## What Should Be Scanned Next

- multimodal monitoring in welding and directed energy deposition
- low-latency monitoring for control loops
- interpretable monitoring linked to defect prevention
- monitoring under sensor degradation or distribution shift
