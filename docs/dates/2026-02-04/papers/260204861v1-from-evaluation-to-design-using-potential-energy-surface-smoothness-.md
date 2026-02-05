---
layout: default
title: From Evaluation to Design: Using Potential Energy Surface Smoothness Metrics to Guide Machine Learning Interatomic Potential Architectures
---

# From Evaluation to Design: Using Potential Energy Surface Smoothness Metrics to Guide Machine Learning Interatomic Potential Architectures
**arXiv**：[2602.04861v1](https://arxiv.org/abs/2602.04861) · [PDF](https://arxiv.org/pdf/2602.04861.pdf)  
**作者**：Ryan Liu, Eric Qu, Tobias Kreiman, Samuel M. Blau, Aditi S. Krishnapriyan  

**一句话要点**：提出键平滑表征测试以指导机器学习原子间势能模型设计

**关键词**：机器学习原子间势能, 势能面平滑性, 键平滑表征测试, 模型设计指导, 分子动力学模拟, Transformer架构

## 3 点简述
- 机器学习原子间势能模型有时无法重现量子势能面的物理平滑性，导致下游模拟错误
- 引入键平滑表征测试，通过受控键变形高效检测非平滑性，包括不连续性和虚假力
- 该测试作为验证指标和设计代理，指导模型优化，实现低回归误差和稳定模拟

## 摘要（原文）

> Machine Learning Interatomic Potentials (MLIPs) sometimes fail to reproduce the physical smoothness of the quantum potential energy surface (PES), leading to erroneous behavior in downstream simulations that standard energy and force regression evaluations can miss. Existing evaluations, such as microcanonical molecular dynamics (MD), are computationally expensive and primarily probe near-equilibrium states. To improve evaluation metrics for MLIPs, we introduce the Bond Smoothness Characterization Test (BSCT). This efficient benchmark probes the PES via controlled bond deformations and detects non-smoothness, including discontinuities, artificial minima, and spurious forces, both near and far from equilibrium. We show that BSCT correlates strongly with MD stability while requiring a fraction of the cost of MD. To demonstrate how BSCT can guide iterative model design, we utilize an unconstrained Transformer backbone as a testbed, illustrating how refinements such as a new differentiable $k$-nearest neighbors algorithm and temperature-controlled attention reduce artifacts identified by our metric. By optimizing model design systematically based on BSCT, the resulting MLIP simultaneously achieves a low conventional E/F regression error, stable MD simulations, and robust atomistic property predictions. Our results establish BSCT as both a validation metric and as an "in-the-loop" model design proxy that alerts MLIP developers to physical challenges that cannot be efficiently evaluated by current MLIP benchmarks.

