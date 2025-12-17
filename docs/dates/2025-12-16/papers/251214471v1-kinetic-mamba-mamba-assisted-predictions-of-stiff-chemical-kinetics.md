---
layout: default
title: Kinetic-Mamba: Mamba-Assisted Predictions of Stiff Chemical Kinetics
---

# Kinetic-Mamba: Mamba-Assisted Predictions of Stiff Chemical Kinetics
**arXiv**：[2512.14471v1](https://arxiv.org/abs/2512.14471) · [PDF](https://arxiv.org/pdf/2512.14471.pdf)  
**作者**：Additi Pandey, Liang Wei, Hessam Babaee, George Em Karniadakis  

**一句话要点**：提出Kinetic-Mamba框架，基于Mamba架构预测刚性化学动力学，用于燃烧模拟。

**关键词**：化学动力学建模, Mamba架构, 神经算子, 燃烧模拟, 时间序列预测

## 3 点简述
- 核心问题：化学动力学建模对燃烧模拟至关重要，需准确预测复杂反应路径和热化学状态演化。
- 方法要点：集成神经算子和Mamba架构，包括独立Mamba模型、约束Mamba模型和基于温度区间的双模型架构。
- 实验或效果：在Syngas和GRI-Mech 3.0反应机制上验证，仅需初始条件即可高保真预测动力学行为。

## 摘要（原文）

> Accurate chemical kinetics modeling is essential for combustion simulations, as it governs the evolution of complex reaction pathways and thermochemical states. In this work, we introduce Kinetic-Mamba, a Mamba-based neural operator framework that integrates the expressive power of neural operators with the efficient temporal modeling capabilities of Mamba architectures. The framework comprises three complementary models: (i) a standalone Mamba model that predicts the time evolution of thermochemical state variables from given initial conditions; (ii) a constrained Mamba model that enforces mass conservation while learning the state dynamics; and (iii) a regime-informed architecture employing two standalone Mamba models to capture dynamics across temperature-dependent regimes. We additionally develop a latent Kinetic-Mamba variant that evolves dynamics in a reduced latent space and reconstructs the full state on the physical manifold. We evaluate the accuracy and robustness of Kinetic-Mamba using both time-decomposition and recursive-prediction strategies. We further assess the extrapolation capabilities of the model on varied out-of-distribution datasets. Computational experiments on Syngas and GRI-Mech 3.0 reaction mechanisms demonstrate that our framework achieves high fidelity in predicting complex kinetic behavior using only the initial conditions of the state variables.

