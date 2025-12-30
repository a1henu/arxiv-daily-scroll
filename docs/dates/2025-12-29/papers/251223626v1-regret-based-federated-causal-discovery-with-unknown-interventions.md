---
layout: default
title: Regret-Based Federated Causal Discovery with Unknown Interventions
---

# Regret-Based Federated Causal Discovery with Unknown Interventions
**arXiv**：[2512.23626v1](https://arxiv.org/abs/2512.23626) · [PDF](https://arxiv.org/pdf/2512.23626.pdf)  
**作者**：Federico Baldo, Charles K. Assaad  

**一句话要点**：提出I-PERI算法以解决联邦因果发现中未知干预导致的异质性问题

**关键词**：联邦因果发现, 未知干预, 异质因果模型, Φ-Markov等价类, 隐私保护

## 3 点简述
- 核心问题：联邦因果发现中客户端因未知干预导致因果模型异质，现有方法假设同质不现实
- 方法要点：I-PERI先恢复客户端图并集的CPDAG，再利用干预诱导的结构差异定向边，生成Φ-CPDAG
- 实验或效果：理论保证收敛与隐私性，合成数据实验验证算法有效性

## 摘要（原文）

> Most causal discovery methods recover a completed partially directed acyclic graph representing a Markov equivalence class from observational data. Recent work has extended these methods to federated settings to address data decentralization and privacy constraints, but often under idealized assumptions that all clients share the same causal model. Such assumptions are unrealistic in practice, as client-specific policies or protocols, for example, across hospitals, naturally induce heterogeneous and unknown interventions. In this work, we address federated causal discovery under unknown client-level interventions. We propose I-PERI, a novel federated algorithm that first recovers the CPDAG of the union of client graphs and then orients additional edges by exploiting structural differences induced by interventions across clients. This yields a tighter equivalence class, which we call the $\mathbfΦ$-Markov Equivalence Class, represented by the $\mathbfΦ$-CPDAG. We provide theoretical guarantees on the convergence of I-PERI, as well as on its privacy-preserving properties, and present empirical evaluations on synthetic data demonstrating the effectiveness of the proposed algorithm.

