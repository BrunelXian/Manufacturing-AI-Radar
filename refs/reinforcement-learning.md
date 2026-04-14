# Reinforcement Learning References

## Domain Introduction

This section covers reinforcement-learning-related papers in manufacturing. The main interest is not RL as a generic optimization tool, but RL for sequential manufacturing decisions where uncertainty, delayed consequences, and action constraints matter.

The current pool contains a mix of process-level, robotic, and scheduling-oriented RL papers. For this first curated pass, priority is given to papers with clearer links to manufacturing process intelligence and adaptive decision-making.

## Subcategories

- RL for additive-manufacturing process decisions
- RL for robotic manufacturing skills
- RL for manufacturing resource allocation and scheduling

## How Papers Are Curated Here

Entries are selected when they frame manufacturing as a sequential decision process and offer something useful for the radar, such as process adaptation, physically meaningful action design, or industrially relevant decision structure.

## Curated Entries

### Laser Scan Path Design for Controlled Microstructure in Additive Manufacturing with Integrated Reduced-Order Phase-Field Modeling and Deep Reinforcement Learning

**Authors:** Augustine Twumasi, Prokash Chandra Roy, Zixun Li, Soumya Shouvik Bhattacharjee, Zhengtao Gan  
**Year:** 2025  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2506.21815v1

**Manufacturing domain:** Laser Powder Bed Fusion  
**AI category:** Deep reinforcement learning, physics-guided decision-making  
**Problem addressed:** Learning scan-path strategies that drive microstructure toward desired outcomes  
**Inputs / modalities:** Reduced-order phase-field predictions, thermal history, and surrogate-model outputs  
**Method summary:** The authors combine phase-field simulation, a learned surrogate, and deep RL to search scan strategies that better control grain-structure behavior.  
**Why it matters:** This is one of the strongest RL papers in the current pool because the action space is tied to a real manufacturing lever and the reward structure is linked to material outcome.  
**Limitations / caution:** The work remains simulation-dependent, so robustness to real machine variability is still unresolved.

### Dynamic resource matching in manufacturing using deep reinforcement learning

**Authors:** Saunak Kumar Panda, Yisha Xiang, Ruiqi Liu  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.27066v1

**Manufacturing domain:** Manufacturing resource allocation and capacity sharing  
**AI category:** Deep reinforcement learning  
**Problem addressed:** Matching demand and capacity dynamically in a manufacturing setting with large state and action spaces  
**Inputs / modalities:** Multi-period demand-capacity states  
**Method summary:** The paper formulates resource matching as a sequential decision problem and uses model-free deep RL to handle the combinatorial allocation problem without explicit transition modelling.  
**Why it matters:** While it is not a process-physics paper, it is a good example of manufacturing RL applied to dynamic operational decision-making rather than static optimization.  
**Limitations / caution:** It is closer to operations-level manufacturing intelligence than to process control, so it should not be mistaken for shop-floor feedback control.

### Simulation-based Learning of Electrical Cabinet Assembly Using Robot Skills

**Authors:** Arik Laemmle, Balazs Andras Balint, Philipp Tenbrock, Frank Naegele, David Traunecker, Jozsef Vancza, Marco F. Huber  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2602.14561v1

**Manufacturing domain:** Robotic assembly  
**AI category:** Deep reinforcement learning, simulation-to-real skill learning  
**Problem addressed:** Automating force-controlled assembly under product variation and difficult contact dynamics  
**Inputs / modalities:** Physics-simulation states, force-sensitive interaction models, parameterizable robot skills  
**Method summary:** The work trains RL agents in simulation for snap-fit assembly using reusable robot-skill abstractions and domain randomization, then transfers policies toward real execution.  
**Why it matters:** This is a strong RL-for-manufacturing paper because it links learning to a difficult contact-rich industrial task instead of only to benchmark scheduling problems.  
**Limitations / caution:** Real-world transfer quality is the key question, and the paper should be read carefully on that point before treating it as a robust deployment success.

### Graph-Enhanced Deep Reinforcement Learning for Multi-Objective Unrelated Parallel Machine Scheduling

**Authors:** Bulent Soykan, Sean Mondesire, Ghaith Rabadi, Grace Bochenek  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2602.08052v1

**Manufacturing domain:** Machine scheduling  
**AI category:** Deep reinforcement learning, graph neural networks  
**Problem addressed:** Learning a scheduling policy that balances tardiness and setup time under complex machine constraints  
**Inputs / modalities:** Job-machine-setup relationships encoded as graph state  
**Method summary:** The paper combines a GNN state representation with PPO to learn direct dispatching policies for a multi-objective scheduling problem.  
**Why it matters:** It is a representative example of RL used for structured manufacturing decisions where graph state encoding matters.  
**Limitations / caution:** This is still scheduling rather than physical process intelligence, so it is lower priority than process-level RL for the long-term radar.

### Learning Memory-Enhanced Improvement Heuristics for Flexible Job Shop Scheduling

**Authors:** Jiaqi Wang, Zhiguang Cao, Peng Zhao, Rui Cao, Yubin Xiao, Yuan Jiang, You Zhou  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.02846v1

**Manufacturing domain:** Flexible job shop scheduling  
**AI category:** Reinforcement-learning-based heuristic search  
**Problem addressed:** Improving scheduling quality beyond constructive RL approaches in flexible production settings  
**Inputs / modalities:** Scheduling states and neighborhood-search information  
**Method summary:** The paper moves from direct constructive scheduling toward improvement-based search with memory-enhanced policy learning, aiming for better solution quality on complex FJSP instances.  
**Why it matters:** It is useful as a representative of how RL is evolving in manufacturing operations from direct dispatching toward richer iterative search.  
**Limitations / caution:** The contribution is meaningful for operations research, but it is still several layers removed from process-level manufacturing control.

### Minimizing Material Waste in Additive Manufacturing through Online Reel Assignment

**Authors:** Ilayda Celenk, Willem van Jaarsveld, Ivo J. B. F. Adan, Alp Akcay  
**Year:** 2026  
**Source:** arXiv  
**Link:** http://arxiv.org/abs/2603.23042v1

**Manufacturing domain:** Filament-based additive manufacturing operations  
**AI category:** Sequential decision modelling, MDP-based policy design  
**Problem addressed:** Reducing long-run material waste in reel assignment under stochastic demand arrival  
**Inputs / modalities:** Sequential reel states and incoming component demands  
**Method summary:** The paper formulates reel assignment as an average-cost Markov decision problem and derives structured policies for online decision-making under uncertainty.  
**Why it matters:** It broadens the additive-manufacturing RL and sequential-decision picture beyond process physics to operational waste reduction, which is still a meaningful manufacturing objective.  
**Limitations / caution:** It is not a canonical deep RL process-control paper, so it should be treated as operations-focused sequential decision-making rather than as a core control result.

## Key Observations

- The best RL paper in the current pool is the additive-manufacturing scan-path paper because it ties actions to physical process outcomes.
- Most other RL papers in the pool are stronger on manufacturing operations and robotic skills than on in-situ process control.
- The repository should therefore keep RL clearly separated into process-level and operations-level strands.

## Current Gaps

- There are very few strong examples of RL deployed directly in closed-loop manufacturing process control.
- Safety, uncertainty, and sample efficiency remain underdeveloped in the current paper pool.
- Welding, machining, and forming are much less represented than scheduling and additive-manufacturing optimization.

## What Should Be Scanned Next

- safe RL for process control
- offline RL for manufacturing data logs
- RL with digital twins or simulators for additive manufacturing
- robot-manufacturing RL with clearer real-system validation
