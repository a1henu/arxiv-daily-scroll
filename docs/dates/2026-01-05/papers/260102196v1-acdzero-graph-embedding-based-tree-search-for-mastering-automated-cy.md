---
layout: default
title: ACDZero: Graph-Embedding-Based Tree Search for Mastering Automated Cyber Defense
---

# ACDZero: Graph-Embedding-Based Tree Search for Mastering Automated Cyber Defense
**arXiv**：[2601.02196v1](https://arxiv.org/abs/2601.02196) · [PDF](https://arxiv.org/pdf/2601.02196.pdf)  
**作者**：Yu Li, Sizhe Tang, Rongqian Chen, Fei Xu Yu, Guangyu Jiang, Mahdi Imani, Nathaniel D. Bastian, Tian Lan  

**一句话要点**：提出基于图嵌入与树搜索的自动化网络防御方法，以解决复杂网络中的样本效率问题。

**关键词**：自动化网络防御, 图神经网络, 蒙特卡洛树搜索, 样本效率, 部分可观测马尔可夫决策过程, 图嵌入

## 3 点简述
- 核心问题：自动化网络防御在复杂网络中面临决策空间大、样本需求高的探索挑战。
- 方法要点：结合图神经网络嵌入观测为图，并利用蒙特卡洛树搜索进行规划，实现探索与利用的平衡。
- 实验或效果：在CAGE-4场景中评估，相比先进强化学习基线，提升了防御奖励和鲁棒性。

## 摘要（原文）

> Automated cyber defense (ACD) seeks to protect computer networks with minimal or no human intervention, reacting to intrusions by taking corrective actions such as isolating hosts, resetting services, deploying decoys, or updating access controls. However, existing approaches for ACD, such as deep reinforcement learning (RL), often face difficult exploration in complex networks with large decision/state spaces and thus require an expensive amount of samples. Inspired by the need to learn sample-efficient defense policies, we frame ACD in CAGE Challenge 4 (CAGE-4 / CC4) as a context-based partially observable Markov decision problem and propose a planning-centric defense policy based on Monte Carlo Tree Search (MCTS). It explicitly models the exploration-exploitation tradeoff in ACD and uses statistical sampling to guide exploration and decision making. We make novel use of graph neural networks (GNNs) to embed observations from the network as attributed graphs, to enable permutation-invariant reasoning over hosts and their relationships. To make our solution practical in complex search spaces, we guide MCTS with learned graph embeddings and priors over graph-edit actions, combining model-free generalization and policy distillation with look-ahead planning. We evaluate the resulting agent on CC4 scenarios involving diverse network structures and adversary behaviors, and show that our search-guided, graph-embedding-based planning improves defense reward and robustness relative to state-of-the-art RL baselines.

