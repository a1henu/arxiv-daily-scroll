---
layout: default
title: Convergence Guarantees for Federated SARSA with Local Training and Heterogeneous Agents
---

# Convergence Guarantees for Federated SARSA with Local Training and Heterogeneous Agents
**arXiv**：[2512.17688v1](https://arxiv.org/abs/2512.17688) · [PDF](https://arxiv.org/pdf/2512.17688.pdf)  
**作者**：Paul Mangold, Eloïse Berthier, Eric Moulines  

**一句话要点**：提出联邦SARSA算法，在异构环境下提供收敛保证与复杂度分析。

**关键词**：联邦强化学习, SARSA算法, 异构性分析, 收敛保证, 线性函数逼近, 本地训练

## 3 点简述
- 核心问题：联邦强化学习中，本地转移和奖励的异构性影响收敛。
- 方法要点：基于线性函数逼近，建立多步误差展开，量化异构影响。
- 实验或效果：数值实验支持理论，显示线性加速和收敛性。

## 摘要（原文）

> We present a novel theoretical analysis of Federated SARSA (FedSARSA) with linear function approximation and local training. We establish convergence guarantees for FedSARSA in the presence of heterogeneity, both in local transitions and rewards, providing the first sample and communication complexity bounds in this setting. At the core of our analysis is a new, exact multi-step error expansion for single-agent SARSA, which is of independent interest. Our analysis precisely quantifies the impact of heterogeneity, demonstrating the convergence of FedSARSA with multiple local updates. Crucially, we show that FedSARSA achieves linear speed-up with respect to the number of agents, up to higher-order terms due to Markovian sampling. Numerical experiments support our theoretical findings.

