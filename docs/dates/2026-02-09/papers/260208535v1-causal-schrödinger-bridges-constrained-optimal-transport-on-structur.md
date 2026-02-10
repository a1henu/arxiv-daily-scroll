---
layout: default
title: Causal Schrödinger Bridges: Constrained Optimal Transport on Structural Manifolds
---

# Causal Schrödinger Bridges: Constrained Optimal Transport on Structural Manifolds
**arXiv**：[2602.08535v1](https://arxiv.org/abs/2602.08535) · [PDF](https://arxiv.org/pdf/2602.08535.pdf)  
**作者**：Rui Wu, Li YongJun  

**一句话要点**：提出因果薛定谔桥以解决因果干预下确定性生成模型的不稳定性问题

**关键词**：因果推断, 生成模型, 最优传输, 扩散过程, 结构约束, 反事实推理

## 3 点简述
- 核心问题：确定性流在因果干预中因低密度区域向量场未定义而变得脆弱，导致数值不稳定和虚假相关性。
- 方法要点：将反事实推断重构为熵最优传输，利用扩散过程在支持不匹配时稳健传输，并严格施加结构可接受约束。
- 实验或效果：在高维干预任务（如Morpho-MNIST）中，CSB在结构一致性上显著优于确定性基线，尤其在强分布外处理下。

## 摘要（原文）

> Generative modeling typically seeks the path of least action via deterministic flows (ODE). While effective for in-distribution tasks, we argue that these deterministic paths become brittle under causal interventions, which often require transporting probability mass across low-density regions ("off-manifold") where the vector field is ill-defined. This leads to numerical instability and spurious correlations. In this work, we introduce the Causal Schrödinger Bridge (CSB), a framework that reformulates counterfactual inference as Entropic Optimal Transport. Unlike deterministic approaches that require strict invertibility, CSB leverages diffusion processes (SDEs) to robustly "tunnel" through support mismatches while strictly enforcing structural admissibility constraints. We prove the Structural Decomposition Theorem, showing that the global high-dimensional bridge factorizes into local, robust transitions. Empirical validation on high-dimensional interventions (Morpho-MNIST) demonstrates that CSB significantly outperforms deterministic baselines in structural consistency, particularly in regimes of strong, out-of-distribution treatments.

