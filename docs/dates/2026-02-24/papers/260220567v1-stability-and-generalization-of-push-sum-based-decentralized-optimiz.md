---
layout: default
title: Stability and Generalization of Push-Sum Based Decentralized Optimization over Directed Graphs
---

# Stability and Generalization of Push-Sum Based Decentralized Optimization over Directed Graphs
**arXiv**：[2602.20567v1](https://arxiv.org/abs/2602.20567) · [PDF](https://arxiv.org/pdf/2602.20567.pdf)  
**作者**：Yifei Liang, Yan Sun, Xiaochun Cao, Li Shen  

**一句话要点**：提出统一稳定性框架分析Push-Sum去中心化优化在定向图中的泛化性能

**关键词**：去中心化优化, 定向图, 泛化分析, Push-Sum算法, 稳定性框架, 通信拓扑

## 3 点简述
- 研究Push-Sum去中心化优化在定向通信网络中的有限迭代稳定性与泛化行为
- 开发基于不平衡感知一致性的统一稳定性框架，分解拓扑偏差与统计效应
- 为凸目标与Polyak–Łojasiewicz非凸目标建立优化与泛化保证，量化拓扑影响

## 摘要（原文）

> Push-Sum-based decentralized learning enables optimization over directed communication networks, where information exchange may be asymmetric. While convergence properties of such methods are well understood, their finite-iteration stability and generalization behavior remain unclear due to structural bias induced by column-stochastic mixing and asymmetric error propagation. In this work, we develop a unified uniform-stability framework for the Stochastic Gradient Push (SGP) algorithm that captures the effect of directed topology. A key technical ingredient is an imbalance-aware consistency bound for Push-Sum, which controls consensus deviation through two quantities: the stationary distribution imbalance parameter $δ$ and the spectral gap $(1-λ)$ governing mixing speed. This decomposition enables us to disentangle statistical effects from topology-induced bias. We establish finite-iteration stability and optimization guarantees for both convex objectives and non-convex objectives satisfying the Polyak--Łojasiewicz condition. For convex problems, SGP attains excess generalization error of order $\tilde{\mathcal{O}}\!\left(\frac{1}{\sqrt{mn}}+\fracγ{δ(1-λ)}+γ\right)$ under step-size schedules, and we characterize the corresponding optimal early stopping time that minimizes this bound. For PŁ objectives, we obtain convex-like optimization and generalization rates with dominant dependence proportional to $κ\!\left(1+\frac{1}{δ(1-λ)}\right)$, revealing a multiplicative coupling between problem conditioning and directed communication topology. Our analysis clarifies when Push-Sum correction is necessary compared with standard decentralized SGD and quantifies how imbalance and mixing jointly shape the best attainable learning performance.

