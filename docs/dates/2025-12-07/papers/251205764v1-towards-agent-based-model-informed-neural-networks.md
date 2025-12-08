---
layout: default
title: Towards agent-based-model informed neural networks
---

# Towards agent-based-model informed neural networks
**arXiv**：[2512.05764v1](https://arxiv.org/abs/2512.05764) · [PDF](https://arxiv.org/pdf/2512.05764.pdf)  
**作者**：Nino Antulov-Fantulin  

**一句话要点**：提出基于代理模型信息神经网络以解决复杂系统建模中约束保持问题

**关键词**：代理模型信息神经网络, 约束保持学习, 图神经网络, 复杂系统建模, 反事实分析

## 3 点简述
- 核心问题：标准神经微分方程在建模复杂系统时难以强制物理不变量外的约束，如质量守恒和网络局部性。
- 方法要点：利用受限图神经网络和层次分解，设计保持结构一致性的可解释动态学习框架。
- 实验效果：在广义Lotka-Volterra系统、图SIR传播模型和真实宏观经济模型中验证了参数恢复、预测鲁棒性和反事实分析能力。

## 摘要（原文）

> In this article, we present a framework for designing neural networks that remain consistent with the underlying principles of agent-based models. We begin by highlighting the limitations of standard neural differential equations in modeling complex systems, where physical invariants (like energy) are often absent but other constraints (like mass conservation, network locality, bounded rationality) must be enforced. To address this, we introduce Agent-Based-Model informed Neural Networks(ABM-NNs), which leverage restricted graph neural networks and hierarchical decomposition to learn interpretable, structure-preserving dynamics. We validate the framework across three case studies of increasing complexity: (i) a generalized Generalized Lotka--Volterra system, where we recover ground-truth parameters from short trajectories in presence of interventions; (ii) a graph-based SIR contagion model, where our method outperforms state-of-the-art graph learning baselines (GCN, GraphSAGE, Graph Transformer) in out-of-sample forecasting and noise robustness; and (iii) a real-world macroeconomic model of the ten largest economies, where we learn coupled GDP dynamics from empirical data and demonstrate gradient-based counterfactual analysis for policy interventions.

