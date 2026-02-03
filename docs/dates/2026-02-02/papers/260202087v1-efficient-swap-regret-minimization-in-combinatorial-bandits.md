---
layout: default
title: Efficient Swap Regret Minimization in Combinatorial Bandits
---

# Efficient Swap Regret Minimization in Combinatorial Bandits
**arXiv**：[2602.02087v1](https://arxiv.org/abs/2602.02087) · [PDF](https://arxiv.org/pdf/2602.02087.pdf)  
**作者**：Andreas Kontogiannis, Vasilis Pollatos, Panayotis Mertikopoulos, Ioannis Panageas  

**一句话要点**：提出高效无交换遗憾算法，解决组合赌博机中指数级动作空间的遗憾最小化问题。

**关键词**：组合赌博机, 无交换遗憾, 多对数缩放, 高效算法, 遗憾最小化

## 3 点简述
- 核心问题：组合赌博机中动作数N指数级大，实现依赖N的多对数无交换遗憾是未解难题。
- 方法要点：设计新算法，遗憾在N上多对数缩放，对组合赌博机类紧致，且每轮计算复杂度也依赖N多对数。
- 实验或效果：算法在多种应用中高效实现，验证了理论结果的实际可行性。

## 摘要（原文）

> This paper addresses the problem of designing efficient no-swap regret algorithms for combinatorial bandits, where the number of actions $N$ is exponentially large in the dimensionality of the problem. In this setting, designing efficient no-swap regret translates to sublinear -- in horizon $T$ -- swap regret with polylogarithmic dependence on $N$. In contrast to the weaker notion of external regret minimization - a problem which is fairly well understood in the literature - achieving no-swap regret with a polylogarithmic dependence on $N$ has remained elusive in combinatorial bandits. Our paper resolves this challenge, by introducing a no-swap-regret learning algorithm with regret that scales polylogarithmically in $N$ and is tight for the class of combinatorial bandits. To ground our results, we also demonstrate how to implement the proposed algorithm efficiently -- that is, with a per-iteration complexity that also scales polylogarithmically in $N$ -- across a wide range of well-studied applications.

