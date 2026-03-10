---
layout: default
title: Split Federated Learning Architectures for High-Accuracy and Low-Delay Model Training
---

# Split Federated Learning Architectures for High-Accuracy and Low-Delay Model Training
**arXiv**：[2603.08687v1](https://arxiv.org/abs/2603.08687) · [PDF](https://arxiv.org/pdf/2603.08687.pdf)  
**作者**：Yiannis Papageorgiou, Yannis Thomas, Ramin Khalili, Iordanis Koutsopoulos  

**一句话要点**：提出优化分割联邦学习架构以提升精度并降低延迟与开销

**关键词**：分割联邦学习, 模型分割, 延迟优化, 通信开销, 启发式算法, 联合优化

## 3 点简述
- 研究分割联邦学习中模型分割与客户端分配对精度、延迟和开销的影响
- 通过联合优化问题建模，提出首个精度感知启发式算法
- 仿真实验显示精度提升3%，延迟降低20%，开销减少50%

## 摘要（原文）

> Can we find a network architecture for ML model training so as to optimize training loss (and thus, accuracy) in Split Federated Learning (SFL)? And can this architecture also reduce training delay and communication overhead? While accuracy is not influenced by how we split the model in ordinary, state-of-the-art SFL, in this work we answer the questions above in the affirmative. Recent Hierarchical SFL (HSFL) architectures adopt a three-tier training structure consisting of clients, (local) aggregators, and a central server. In this architecture, the model is partitioned at two partitioning layers into three sub-models, which are executed across the three tiers. Despite their merits, HSFL architectures overlook the impact of the partitioning layers and client-to-aggregator assignments on accuracy, delay, and overhead. This work explicitly captures the impact of the partitioning layers and client-to-aggregator assignments on accuracy, delay and overhead by formulating a joint optimization problem. We prove that the problem is NP-hard and propose the first accuracy-aware heuristic algorithm that explicitly accounts for model accuracy, while remaining delay-efficient. Simulation results on public datasets show that our approach can improve accuracy by 3%, while reducing delay by 20% and overhead by 50%, compared to state-of-the-art SFL and HSFL schemes.

