---
layout: default
title: Game-Theoretic Co-Evolution for LLM-Based Heuristic Discovery
---

# Game-Theoretic Co-Evolution for LLM-Based Heuristic Discovery
**arXiv**：[2601.22896v1](https://arxiv.org/abs/2601.22896) · [PDF](https://arxiv.org/pdf/2601.22896.pdf)  
**作者**：Xinyi Ke, Kai Li, Junliang Xing, Yifan Zhang, Jian Cheng  

**一句话要点**：提出算法空间响应预言机框架，以解决基于大语言模型的启发式发现中静态评估导致的泛化不足问题。

**关键词**：启发式发现, 大语言模型, 协同进化, 零和博弈, 组合优化, 泛化能力

## 3 点简述
- 核心问题：现有基于大语言模型的启发式发现方法依赖静态评估，易过拟合且泛化能力差。
- 方法要点：将启发式发现建模为求解器与实例生成器间的程序级协同进化零和博弈，通过大语言模型迭代扩展策略池。
- 实验或效果：在多个组合优化领域，该框架优于静态训练基线，显著提升泛化性和鲁棒性。

## 摘要（原文）

> Large language models (LLMs) have enabled rapid progress in automatic heuristic discovery (AHD), yet most existing methods are predominantly limited by static evaluation against fixed instance distributions, leading to potential overfitting and poor generalization under distributional shifts. We propose Algorithm Space Response Oracles (ASRO), a game-theoretic framework that reframes heuristic discovery as a program level co-evolution between solver and instance generator. ASRO models their interaction as a two-player zero-sum game, maintains growing strategy pools on both sides, and iteratively expands them via LLM-based best-response oracles against mixed opponent meta-strategies, thereby replacing static evaluation with an adaptive, self-generated curriculum. Across multiple combinatorial optimization domains, ASRO consistently outperforms static-training AHD baselines built on the same program search mechanisms, achieving substantially improved generalization and robustness on diverse and out-of-distribution instances.

