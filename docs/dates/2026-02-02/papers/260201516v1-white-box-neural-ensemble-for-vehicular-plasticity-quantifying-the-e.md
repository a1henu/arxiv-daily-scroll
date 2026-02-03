---
layout: default
title: White-Box Neural Ensemble for Vehicular Plasticity: Quantifying the Efficiency Cost of Symbolic Auditability in Adaptive NMPC
---

# White-Box Neural Ensemble for Vehicular Plasticity: Quantifying the Efficiency Cost of Symbolic Auditability in Adaptive NMPC
**arXiv**：[2602.01516v1](https://arxiv.org/abs/2602.01516) · [PDF](https://arxiv.org/pdf/2602.01516.pdf)  
**作者**：Enzo Nicolas Spotorno, Matheus Wagner, Antonio Augusto Medeiros Frohlich  

**一句话要点**：提出白盒自适应NMPC架构，通过模块化主权仲裁解决车辆可塑性问题。

**关键词**：白盒自适应NMPC, 车辆可塑性, 模块化主权, 符号图审计, 效率成本量化

## 3 点简述
- 核心问题：车辆可塑性，即无需重新训练适应多变工况。
- 方法要点：使用冻结的特定工况神经网络专家，基于符号图实现完全可审计性。
- 实验效果：在复合工况变化下验证快速适应和高跟踪精度，量化透明度成本。

## 摘要（原文）

> We present a white-box adaptive NMPC architecture that resolves vehicular plasticity (adaptation to varying operating regimes without retraining) by arbitrating among frozen, regime-specific neural specialists using a Modular Sovereignty paradigm. The ensemble dynamics are maintained as a fully traversable symbolic graph in CasADi, enabling maximal runtime auditability. Synchronous simulation validates rapid adaptation (~7.3 ms) and near-ideal tracking fidelity under compound regime shifts (friction, mass, drag) where non-adaptive baselines fail. Empirical benchmarking quantifies the transparency cost: symbolic graph maintenance increases solver latency by 72-102X versus compiled parametric physics models, establishing the efficiency price of strict white-box implementation.

