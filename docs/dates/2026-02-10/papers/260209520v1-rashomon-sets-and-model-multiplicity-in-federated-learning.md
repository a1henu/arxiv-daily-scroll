---
layout: default
title: Rashomon Sets and Model Multiplicity in Federated Learning
---

# Rashomon Sets and Model Multiplicity in Federated Learning
**arXiv**：[2602.09520v1](https://arxiv.org/abs/2602.09520) · [PDF](https://arxiv.org/pdf/2602.09520.pdf)  
**作者**：Xenia Heilmann, Luca Corbucci, Mattia Cerrato  

**一句话要点**：提出联邦学习中的Rashomon集定义与评估方法，以解决模型多样性与决策边界不稳定问题。

**关键词**：联邦学习, Rashomon集, 模型多样性, 决策边界, 隐私保护, 公平性

## 3 点简述
- 核心问题：现有Rashomon集定义不适用于联邦学习，导致模型选择可能忽视本地数据差异与公平性。
- 方法要点：定义三种联邦Rashomon集视角，并开发隐私约束下的多样性度量估计方法。
- 实验或效果：在标准联邦学习数据集上验证，新定义能帮助客户端选择更符合本地需求的模型。

## 摘要（原文）

> The Rashomon set captures the collection of models that achieve near-identical empirical performance yet may differ substantially in their decision boundaries. Understanding the differences among these models, i.e., their multiplicity, is recognized as a crucial step toward model transparency, fairness, and robustness, as it reveals decision boundaries instabilities that standard metrics obscure. However, the existing definitions of Rashomon set and multiplicity metrics assume centralized learning and do not extend naturally to decentralized, multi-party settings like Federated Learning (FL). In FL, multiple clients collaboratively train models under a central server's coordination without sharing raw data, which preserves privacy but introduces challenges from heterogeneous client data distribution and communication constraints. In this setting, the choice of a single best model may homogenize predictive behavior across diverse clients, amplify biases, or undermine fairness guarantees. In this work, we provide the first formalization of Rashomon sets in FL.First, we adapt the Rashomon set definition to FL, distinguishing among three perspectives: (I) a global Rashomon set defined over aggregated statistics across all clients, (II) a t-agreement Rashomon set representing the intersection of local Rashomon sets across a fraction t of clients, and (III) individual Rashomon sets specific to each client's local distribution.Second, we show how standard multiplicity metrics can be estimated under FL's privacy constraints. Finally, we introduce a multiplicity-aware FL pipeline and conduct an empirical study on standard FL benchmark datasets. Our results demonstrate that all three proposed federated Rashomon set definitions offer valuable insights, enabling clients to deploy models that better align with their local data, fairness considerations, and practical requirements.

