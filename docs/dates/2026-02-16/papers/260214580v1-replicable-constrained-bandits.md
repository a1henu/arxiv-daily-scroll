---
layout: default
title: Replicable Constrained Bandits
---

# Replicable Constrained Bandits
**arXiv**：[2602.14580v1](https://arxiv.org/abs/2602.14580) · [PDF](https://arxiv.org/pdf/2602.14580.pdf)  
**作者**：Matteo Bollini, Gianmarco Genalti, Francesco Emanuele Stradi, Matteo Castiglioni, Alberto Marchesi  

**一句话要点**：提出可复制约束多臂老虎机算法，在未知随机环境中实现决策序列一致性与约束满足。

**关键词**：可复制算法, 约束多臂老虎机, 在线学习, UCB算法, 随机环境, 遗憾分析

## 3 点简述
- 研究可复制算法在约束多臂老虎机问题中的应用，旨在确保决策序列在不同执行中高度一致。
- 设计可复制算法，其遗憾和约束违反与非可复制算法在轮数T上匹配，基于可复制UCB类方法。
- 未知实验细节，但理论保证表明可复制性在约束优化中可行，无需牺牲性能。

## 摘要（原文）

> Algorithmic \emph{replicability} has recently been introduced to address the need for reproducible experiments in machine learning. A \emph{replicable online learning} algorithm is one that takes the same sequence of decisions across different executions in the same environment, with high probability. We initiate the study of algorithmic replicability in \emph{constrained} MAB problems, where a learner interacts with an unknown stochastic environment for $T$ rounds, seeking not only to maximize reward but also to satisfy multiple constraints. Our main result is that replicability can be achieved in constrained MABs. Specifically, we design replicable algorithms whose regret and constraint violation match those of non-replicable ones in terms of $T$. As a key step toward these guarantees, we develop the first replicable UCB-like algorithm for \emph{unconstrained} MABs, showing that algorithms that employ the optimism in-the-face-of-uncertainty principle can be replicable, a result that we believe is of independent interest.

