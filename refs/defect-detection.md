# Defect Detection References

## Domain Introduction

This section covers papers on identifying, localising, characterising, or reasoning about defects in manufacturing systems. The focus is on defect-detection work that retains a meaningful connection to process physics, sensing, or manufacturing quality logic.

In manufacturing, defect detection is valuable not only because it flags bad parts, but because it often serves as the first bridge between process observations and quality outcomes. The strongest papers here therefore do more than classify images. They help explain what kind of defect is present, how it is sensed, and why the result matters for manufacturing decisions.

## Subcategories

- Additive-manufacturing-specific defect detection
- In-situ or monitoring-informed defect identification
- Post-process inspection and volumetric assessment
- Welding and other process-specific defect characterization

## How Papers Are Curated Here

Priority is given to papers that connect defect detection to additive manufacturing, weld quality, process monitoring, or physically meaningful defect interpretation. Generic industrial surface-inspection papers are deprioritized unless they contribute clear manufacturing insight.

## Curated Entries

### Explainable Computer Vision Framework for Automated Pore Detection and Criticality Assessment in Additive Manufacturing

**Authors:** Akshansh Mishra, Rakesh Morisetty  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2602.03883v1

**Manufacturing domain:** Additive manufacturing  
**AI category:** Explainable computer vision, volumetric defect assessment  
**Problem addressed:** Detecting internal pores and assessing their criticality rather than merely counting them  
**Inputs / modalities:** Reconstructed three-dimensional tomographic volumes and pore geometry descriptors  
**Method summary:** The paper identifies pores from volumetric slices, extracts geometric and spatial descriptors, and builds a pore-interaction representation to assess defect criticality in a more interpretable way.  
**Why it matters:** This is one of the strongest defect papers in the current pool because it moves beyond plain defect presence toward physically meaningful quality assessment in additive manufacturing.  
**Limitations / caution:** It is a post-process inspection framework rather than an in-situ defect prevention system, so its value is strongest for qualification and failure analysis.

### Feature-Aware Anisotropic Local Differential Privacy for Utility-Preserving Graph Representation Learning in Metal Additive Manufacturing

**Authors:** MD Shafikul Islam, Mahathir Mohammad Bappy, Saifur Rahman Tushar, Md Arifuzzaman  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2604.05077v1

**Manufacturing domain:** Metal additive manufacturing  
**AI category:** Graph learning for defect detection, privacy-preserving learning  
**Problem addressed:** Detecting defects from melt-pool observations while preserving the utility of sensitive process data  
**Inputs / modalities:** Layer-wise thermal and spatial process features from metal AM sensing  
**Method summary:** The paper combines a hierarchical graph attention model with anisotropic privacy noise allocation so that defect-relevant process signatures are retained more effectively than under uniform privacy perturbation.  
**Why it matters:** It is useful because it treats defect detection as a structured process-intelligence problem rather than a flat image-classification task. It also raises an important practical issue: high-value manufacturing data are often not freely shareable.  
**Limitations / caution:** The privacy angle is central, so this should be read as a defect-detection system under data-sharing constraints, not as a generic benchmark for raw detection accuracy.

### Towards Agentic Defect Reasoning: A Graph-Assisted Retrieval Framework for Laser Powder Bed Fusion

**Authors:** Muhammad Rizwan Awan, Volker Pickert, Muhammad Waqar Ashraf, Saleh Ali, Farshid Mahmouditabar, Shafiq Odhano  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2604.04208v1

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Knowledge-assisted defect reasoning  
**Problem addressed:** Making LPBF defect mechanisms easier to retrieve and reason about across scattered literature  
**Inputs / modalities:** Literature-derived parameter-mechanism-defect relations  
**Method summary:** The paper converts LPBF publications into an evidence-linked knowledge graph and uses graph-assisted retrieval to trace parameter-to-defect pathways.  
**Why it matters:** Although it is not a detector operating on process data, it is highly relevant to defect-detection mapping because LPBF defect knowledge is fragmented and difficult to use systematically.  
**Limitations / caution:** This is a knowledge-organization contribution, not an in-situ inspection model, so it should not be confused with direct defect-detection performance work.

### Machine Learning-Based Ultrasonic Weld Characterization Using Hierarchical Wave Modeling and Diffusion-Driven Distribution Alignment

**Authors:** Joshua R. Tempelman, Adam J. Wachtor, Eric B. Flynn  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2510.13023v2

**Manufacturing domain:** Weld inspection  
**AI category:** Nondestructive evaluation, signal-based defect characterization  
**Problem addressed:** Characterising weld heterogeneity and crack-related defects under data scarcity and signal corruption  
**Inputs / modalities:** Ultrasonic wave data supported by reduced-order simulation and diffusion-based alignment  
**Method summary:** The paper uses a reduced-order physical model to generate data, aligns distributions under realistic signal corruption, and applies learned segmentation and inversion to ultrasonic inspection.  
**Why it matters:** This is a stronger manufacturing defect paper than many vision-only studies because it is grounded in inspection physics and addresses difficult industrial signal conditions.  
**Limitations / caution:** The contribution is strongest in NDE workflow design; transfer into varied weld geometries and shop-floor conditions still needs careful validation.

### Hybrid Quantum-Classical AI for Industrial Defect Classification in Welding Images

**Authors:** Akshaya Srinivasan, Xiaoyin Cheng, Jianming Yi, Alexander Geng, Desislava Ivanova, Andreas Weinmann, Ali Moghiseh  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.28995v1

**Manufacturing domain:** TIG welding  
**AI category:** Vision-based defect classification  
**Problem addressed:** Classifying weld defects from inspection images using compact hybrid feature-processing pipelines  
**Inputs / modalities:** Welding images encoded after CNN feature extraction  
**Method summary:** The paper uses CNN-derived features and compares two hybrid quantum-classical routes against a conventional deep model for defect classification.  
**Why it matters:** It is included not because of the quantum angle itself, but because weld defect classification is a legitimate manufacturing quality task and the paper is clearly process-specific.  
**Limitations / caution:** The manufacturing value appears more incremental than foundational, and the quantum framing should not distract from the need to judge whether it improves reliability or deployment practicality.

### Non-Contact and Non-Destructive Detection of Structural Defects in Bioprinted Constructs Using Video-Based Vibration Analysis

**Authors:** Md Anisur Rahman, Md Asif Hasan Khan, Tuan Mai, Jinki Kim  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2601.00073v1

**Manufacturing domain:** Extrusion-based bioprinting  
**AI category:** Non-contact defect detection, vibration analysis  
**Problem addressed:** Detecting hidden structural defects in soft bioprinted constructs without damaging the part  
**Inputs / modalities:** Video-based vibration responses from printed constructs  
**Method summary:** The paper uses non-contact vibration measurements to identify structural integrity problems that are difficult to inspect with conventional contact-based methods.  
**Why it matters:** It expands the defect-detection map beyond metals and shows how manufacturing-specific material constraints can dictate a very different sensing and detection strategy.  
**Limitations / caution:** It is domain-specific to bioprinting and soft materials, so it should be read as a useful specialty case rather than as a general manufacturing defect-detection template.

## Key Observations

- The strongest defect-detection entries in the current pool are those that stay close to additive-manufacturing quality logic or physically grounded inspection workflows.
- Process-aware defect reasoning is still much rarer than generic visual defect classification.
- Post-process inspection remains better represented than true in-situ defect detection and prevention.

## Current Gaps

- There are still too few strong papers on direct lack-of-fusion or porosity detection from live process signals.
- The current pool underrepresents multimodal in-situ defect identification in DED, WAAM, and welding.
- Many available industrial vision papers remain weakly connected to process interpretation or root-cause analysis.

## What Should Be Scanned Next

- in-situ porosity and lack-of-fusion detection in LPBF
- multimodal defect identification in directed energy deposition and welding
- process-linked defect prediction rather than post-process inspection alone
- defect severity assessment tied to qualification or failure risk
