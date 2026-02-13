---
layout: default
title: Robust Optimization Approach and Learning Based Hide-and-Seek Game for Resilient Network Design
---

# Robust Optimization Approach and Learning Based Hide-and-Seek Game for Resilient Network Design
**arXiv**：[2602.11854v1](https://arxiv.org/abs/2602.11854) · [PDF](https://arxiv.org/pdf/2602.11854.pdf)  
**作者**：Mohammad Khosravi, Setareh Maghsudi  

**一句话要点**：提出基于鲁棒优化和学习博弈的方法，以设计不确定环境下具有再生器的弹性通信网络。

**关键词**：鲁棒优化, 网络弹性设计, 再生器部署, 预算不确定性集, 学习博弈, 列约束生成

## 3 点简述
- 研究在链路和节点不确定下，部署再生器确保网络连通性的最小成本问题。
- 采用鲁棒优化框架，结合列约束生成、Benders分解和迭代方法求解。
- 通过理论分析和计算实验验证方法优于传统静态鲁棒模型和确定性最坏情况公式。

## 摘要（原文）

> We study the design of resilient and reliable communication networks in which a signal can be transferred only up to a limited distance before its quality falls below an acceptable threshold. When excessive signal degradation occurs, regeneration is required through regenerators installed at selected network nodes. In this work, both network links and nodes are subject to uncertainty. The installation costs of regenerators are modeled using a budgeted uncertainty set. In addition, link lengths follow a dynamic budgeted uncertainty set introduced in this paper, where deviations may vary over time. Robust optimization seeks solutions whose performance is guaranteed under all scenarios represented by the underlying uncertainty set. Accordingly, the objective is to identify a minimum-cost subset of nodes for regenerator deployment that ensures full network connectivity, even under the worst possible realizations of uncertainty. To solve the problem, we first formulate it within a robust optimization framework, and then develop scalable solution methods based on column-and-constraint generation, Benders decomposition, and iterative robust optimization. In addition, we formulate a learning-based hide-and-seek game to further analyze the problem structure. The proposed approaches are evaluated against classical static budgeted robust models and deterministic worst-case formulations. Both theoretical analysis and computational results demonstrate the effectiveness and advantages of our methodology.

