---
layout: default
title: Supervised Metric Regularization Through Alternating Optimization for Multi-Regime Physics-Informed Neural Networks
---

# Supervised Metric Regularization Through Alternating Optimization for Multi-Regime Physics-Informed Neural Networks
**arXiv**：[2602.09980v1](https://arxiv.org/abs/2602.09980) · [PDF](https://arxiv.org/pdf/2602.09980.pdf)  
**作者**：Enzo Nicolas Spotorno, Josafat Ribeiro Leal, Antonio Augusto Frohlich  

**一句话要点**：提出拓扑感知PINN，通过监督度量正则化与交替优化，解决参数化动力系统多模态建模中的谱偏差问题。

**关键词**：物理信息神经网络, 度量正则化, 交替优化, 谱偏差, 多模态建模, 动力系统

## 3 点简述
- 标准PINN在建模具有尖锐转变的参数化动力系统时，易因谱偏差导致模式崩溃。
- 方法引入监督度量正则化，优化潜空间以分离不同物理机制，并采用交替优化管理梯度冲突。
- 在Duffing振荡器实验中，相比基线，物理残差降低约49%，梯度方差减少2.18倍，参数更少。

## 摘要（原文）

> Standard Physics-Informed Neural Networks (PINNs) often face challenges when modeling parameterized dynamical systems with sharp regime transitions, such as bifurcations. In these scenarios, the continuous mapping from parameters to solutions can result in spectral bias or "mode collapse", where the network averages distinct physical behaviors. We propose a Topology-Aware PINN (TAPINN) that aims to mitigate this challenge by structuring the latent space via Supervised Metric Regularization. Unlike standard parametric PINNs that map physical parameters directly to solutions, our method conditions the solver on a latent state optimized to reflect the metric-based separation between regimes, showing ~49% lower physics residual (0.082 vs. 0.160). We train this architecture using a phase-based Alternating Optimization (AO) schedule to manage gradient conflicts between the metric and physics objectives. Preliminary experiments on the Duffing Oscillator demonstrate that while standard baselines suffer from spectral bias and high-capacity Hypernetworks overfit (memorizing data while violating physics), our approach achieves stable convergence with 2.18x lower gradient variance than a multi-output Sobolev Error baseline, and 5x fewer parameters than a hypernetwork-based alternative.

