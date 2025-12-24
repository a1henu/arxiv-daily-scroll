---
layout: default
title: Mixture-of-Experts with Gradient Conflict-Driven Subspace Topology Pruning for Emergent Modularity
---

# Mixture-of-Experts with Gradient Conflict-Driven Subspace Topology Pruning for Emergent Modularity
**arXiv**：[2512.20291v1](https://arxiv.org/abs/2512.20291) · [PDF](https://arxiv.org/pdf/2512.20291.pdf)  
**作者**：Yuxing Gan, Ziyu Lei  

**一句话要点**：提出CDSP-MoE框架，通过梯度冲突驱动的子空间拓扑剪枝解决MoE结构隔离和指令过拟合问题。

**关键词**：混合专家模型, 梯度冲突, 子空间剪枝, 模块化结构, 动态专家实例化, 盲推理

## 3 点简述
- 核心问题：MoE架构存在结构参数隔离导致灾难性遗忘和指令过拟合降低无指令场景性能。
- 方法要点：基于通用权重子空间假设，在共享物理子空间中动态实例化专家，利用梯度冲突作为结构监督信号进行拓扑剪枝。
- 实验或效果：在无显式指令的严格盲推理协议下，实现稳健的内容驱动路由和语义专业化。

## 摘要（原文）

> Mixture-of-Experts (MoE) architectures achieve parameter efficiency through conditional computation, yet contemporary designs suffer from two fundamental limitations: structural parameter isolation that causes catastrophic forgetting, and instruction-overfitting that degrades performance in instruction-free scenarios. We propose CDSP-MoE (Conflict-Driven Subspace Pruning MoE), a framework that addresses these issues through a paradigm shift from isolated expert containers to dynamic expert instantiation within a shared physical subspace. Grounded in the Universal Weight Subspace Hypothesis, CDSP-MoE maintains a super-complete parameter backbone where logical experts are carved out via learnable topology masks. Unlike prior work that uses gradient conflict for token reassignment or optimization surgery, we leverage it as a structural supervisory signal: a Lagged Gradient Game penalizes interfering connections in the shared manifold, enabling the topology to spontaneously prune conflicting pathways and evolve interpretable modular structures. Experimental results demonstrate that CDSP-MoE achieves robust content-driven routing without human-defined task labels, maintaining semantic specialization even under strict blind inference protocols where explicit instructions are absent. Code is available at: https://github.com/konodiodaaaaa1/Conflict-Driven-Subspace-Pruning-Mixture-of-Experts

