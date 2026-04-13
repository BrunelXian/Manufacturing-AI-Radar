# Manufacturing AI Taxonomy

## Purpose

This taxonomy organizes AI in manufacturing around industrial function rather than around AI model families alone.

A manufacturing-oriented taxonomy is necessary because the same AI method can play very different roles depending on whether it is used for sensing, diagnosis, prediction, optimisation, or control.

## Taxonomy Overview

The current framework uses ten primary categories:

1. Sensing
2. Monitoring
3. Defect Detection
4. Modelling
5. Prediction
6. Control
7. Optimisation
8. Reinforcement Learning
9. Digital Twin
10. Industrial Deployment

## 1. Sensing

### Definition

Sensing covers the acquisition of raw information from the manufacturing process or production environment.

### Typical Tasks

- capturing thermal, optical, acoustic, force, vibration, or electrical signals
- collecting layer-wise or time-series process data
- combining multiple sensor channels into usable process observations

### Typical Methods

- sensor fusion
- image acquisition pipelines
- signal conditioning
- multimodal data alignment

### Typical Applications

- melt pool image capture in additive manufacturing
- acoustic emission collection in machining
- camera-based weld seam observation
- in-situ thermal monitoring

## 2. Monitoring

### Definition

Monitoring covers the interpretation of process observations to estimate current manufacturing state or process health.

### Typical Tasks

- state estimation
- anomaly detection
- drift detection
- process stability tracking
- online quality indication

### Typical Methods

- computer vision
- signal processing with machine learning
- anomaly detection models
- temporal models for process state inference

### Typical Applications

- online melt pool stability assessment
- tool wear monitoring
- machine condition monitoring
- process deviation alarms

## 3. Defect Detection

### Definition

Defect detection identifies whether a manufactured part or process contains unacceptable flaws, during production or after processing.

### Typical Tasks

- classification of defective versus acceptable outcomes
- defect localization and segmentation
- surface inspection
- internal defect indication
- defect severity grading

### Typical Methods

- convolutional neural networks
- segmentation models
- anomaly detection
- vision transformers
- hybrid signal-image defect models

### Typical Applications

- porosity detection in additive manufacturing
- crack inspection in welded joints
- surface defect inspection in rolled products
- defect screening in machined components

## 4. Modelling

### Definition

Modelling builds representations of manufacturing processes, material behavior, or system dynamics.

### Typical Tasks

- surrogate modelling
- process response approximation
- state transition modelling
- hybrid physics-data representations
- uncertainty-aware process modelling

### Typical Methods

- regression models
- Gaussian processes
- neural surrogates
- physics-informed machine learning
- reduced-order and hybrid models

### Typical Applications

- melt pool geometry approximation
- residual stress modelling
- microstructure evolution approximation
- machine dynamics representation

## 5. Prediction

### Definition

Prediction uses observed or modeled information to estimate future states, outcomes, or quality metrics.

### Typical Tasks

- quality prediction
- remaining useful life estimation
- future process state forecasting
- defect probability estimation
- production outcome prediction

### Typical Methods

- supervised learning
- sequence models
- probabilistic forecasting
- ensemble learning
- uncertainty quantification

### Typical Applications

- predicting build failures in additive manufacturing
- forecasting tool wear
- predicting dimensional accuracy
- estimating quality from early process signals

## 6. Control

### Definition

Control uses sensed or inferred process information to adjust manufacturing actions in order to maintain or improve performance.

### Typical Tasks

- parameter adjustment
- closed-loop process regulation
- trajectory correction
- disturbance rejection
- quality-consistent process stabilization

### Typical Methods

- adaptive control
- model predictive control
- learning-enhanced controllers
- observer-controller integration
- rule-learning for control tuning

### Typical Applications

- laser power adjustment in additive manufacturing
- feed rate control in machining
- welding parameter adaptation
- robotic path correction

## 7. Optimisation

### Definition

Optimisation searches for better parameter sets, schedules, strategies, or design choices under manufacturing objectives and constraints.

### Typical Tasks

- process parameter tuning
- multi-objective trade-off exploration
- resource allocation
- design of experiments acceleration
- production planning improvement

### Typical Methods

- Bayesian optimisation
- evolutionary algorithms
- surrogate-assisted optimisation
- gradient-based optimisation with learned models
- hybrid heuristic-learning methods

### Typical Applications

- parameter window design for additive manufacturing
- cycle time and quality balancing
- production scheduling improvement
- process recipe optimisation

## 8. Reinforcement Learning

### Definition

Reinforcement learning addresses sequential decision-making where a manufacturing agent learns from interaction, delayed reward, and uncertainty.

### Typical Tasks

- adaptive control
- robotic manipulation
- scheduling under uncertainty
- policy learning for dynamic process adjustment
- decision-making in partially observed environments

### Typical Methods

- value-based reinforcement learning
- policy gradient methods
- actor-critic methods
- model-based reinforcement learning
- offline reinforcement learning

### Typical Applications

- adaptive process control in additive manufacturing
- robotic assembly policy learning
- dynamic scheduling in flexible manufacturing systems
- autonomous parameter adjustment under stochastic disturbances

## 9. Digital Twin

### Definition

Digital twin refers to an integrated virtual representation of a manufacturing asset, process, or system that remains linked to physical operation through data and models.

### Typical Tasks

- process simulation with live data
- virtual commissioning
- predictive analysis
- anomaly explanation
- what-if scenario evaluation

### Typical Methods

- physics-based simulation
- hybrid models
- data assimilation
- state synchronization
- machine learning-enhanced simulation

### Typical Applications

- twin-based monitoring of additive manufacturing builds
- production line digital replicas
- machine health twins
- process optimisation through virtual experimentation

## 10. Industrial Deployment

### Definition

Industrial deployment concerns the translation of AI methods into usable, trustworthy, and maintainable manufacturing systems.

### Typical Tasks

- model integration with industrial software and controls
- robustness validation
- latency management
- human-in-the-loop interaction
- lifecycle monitoring and retraining

### Typical Methods

- MLOps for industrial systems
- edge deployment
- model compression
- uncertainty handling
- governance and traceability workflows

### Typical Applications

- deployment of machine vision inspection models on production lines
- integration of predictive models with MES or SCADA systems
- edge AI for machine condition diagnostics
- operator-facing decision support tools

## Cross-Cutting Relationships

The categories often connect in paths such as:

`Sensing -> Monitoring -> Prediction -> Control`

and:

`Sensing -> Defect Detection -> Root-cause Analysis -> Optimisation`

Digital twin and industrial deployment cut across these paths at the system level.
