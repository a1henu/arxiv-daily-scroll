---
layout: default
title: Federated Causal Representation Learning in State-Space Systems for Decentralized Counterfactual Reasoning
---

# Federated Causal Representation Learning in State-Space Systems for Decentralized Counterfactual Reasoning
**arXiv**：[2602.19414v1](https://arxiv.org/abs/2602.19414) · [PDF](https://arxiv.org/pdf/2602.19414.pdf)  
**作者**：Nazal Mohamed, Ayush Mohanty, Nagi Gebraeel  

**一句话要点**：提出联邦因果表示学习框架，以解决工业资产网络中数据隐私下的去中心化反事实推理问题。

**关键词**：联邦学习, 因果表示学习, 状态空间系统, 反事实推理, 工业控制系统, 隐私保护

## 3 点简述
- 核心问题：工业资产网络因数据高维和私有，难以集中分析跨客户操作变化的影响。
- 方法要点：客户将高维观测映射为低维潜在状态，服务器估计全局状态转移和控制结构，实现仅交换潜在状态的去中心化推理。
- 实验或效果：在合成和真实工业控制数据集上验证了可扩展性和准确的跨客户反事实推断。

## 摘要（原文）

> Networks of interdependent industrial assets (clients) are tightly coupled through physical processes and control inputs, raising a key question: how would the output of one client change if another client were operated differently? This is difficult to answer because client-specific data are high-dimensional and private, making centralization of raw data infeasible. Each client also maintains proprietary local models that cannot be modified. We propose a federated framework for causal representation learning in state-space systems that captures interdependencies among clients under these constraints. Each client maps high-dimensional observations into low-dimensional latent states that disentangle intrinsic dynamics from control-driven influences. A central server estimates the global state-transition and control structure. This enables decentralized counterfactual reasoning where clients predict how outputs would change under alternative control inputs at others while only exchanging compact latent states. We prove convergence to a centralized oracle and provide privacy guarantees. Our experiments demonstrate scalability, and accurate cross-client counterfactual inference on synthetic and real-world industrial control system datasets.

