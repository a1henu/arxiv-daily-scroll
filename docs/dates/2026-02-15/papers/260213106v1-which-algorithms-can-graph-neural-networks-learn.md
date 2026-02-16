---
layout: default
title: Which Algorithms Can Graph Neural Networks Learn?
---

# Which Algorithms Can Graph Neural Networks Learn?
**arXiv**：[2602.13106v1](https://arxiv.org/abs/2602.13106) · [PDF](https://arxiv.org/pdf/2602.13106.pdf)  
**作者**：Solveig Wittig, Antonis Vasileiou, Robert R. Nerem, Timo Stoll, Floris Geerts, Yusu Wang, Christopher Morris  

**一句话要点**：提出理论框架以分析图神经网络学习算法的条件与局限性

**关键词**：图神经网络, 算法学习, 理论框架, 泛化性分析, 动态规划, 消息传递网络

## 3 点简述
- 研究图神经网络学习离散算法的能力，关注泛化性理论保证
- 建立框架分析MPNNs学习算法的充分条件，覆盖最短路径、最小生成树等
- 提供不可能性结果并设计更表达性架构，实验支持理论发现

## 摘要（原文）

> In recent years, there has been growing interest in understanding neural architectures' ability to learn to execute discrete algorithms, a line of work often referred to as neural algorithmic reasoning. The goal is to integrate algorithmic reasoning capabilities into larger neural pipelines. Many such architectures are based on (message-passing) graph neural networks (MPNNs), owing to their permutation equivariance and ability to deal with sparsity and variable-sized inputs. However, existing work is either largely empirical and lacks formal guarantees or it focuses solely on expressivity, leaving open the question of when and how such architectures generalize beyond a finite training set. In this work, we propose a general theoretical framework that characterizes the sufficient conditions under which MPNNs can learn an algorithm from a training set of small instances and provably approximate its behavior on inputs of arbitrary size. Our framework applies to a broad class of algorithms, including single-source shortest paths, minimum spanning trees, and general dynamic programming problems, such as the $0$-$1$ knapsack problem. In addition, we establish impossibility results for a wide range of algorithmic tasks, showing that standard MPNNs cannot learn them, and we derive more expressive MPNN-like architectures that overcome these limitations. Finally, we refine our analysis for the Bellman-Ford algorithm, yielding a substantially smaller required training set and significantly extending the recent work of Nerem et al. [2025] by allowing for a differentiable regularization loss. Empirical results largely support our theoretical findings.

