---
layout: default
title: Partially Lazy Gradient Descent for Smoothed Online Learning
---

# Partially Lazy Gradient Descent for Smoothed Online Learning
**arXiv**：[2601.15984v1](https://arxiv.org/abs/2601.15984) · [PDF](https://arxiv.org/pdf/2601.15984.pdf)  
**作者**：Naram Mhaisen, George Iosifidis  

**一句话要点**：提出k-lazyGD算法，在平滑在线凸优化中实现懒惰性与跟踪能力的平衡。

**关键词**：平滑在线凸优化, 懒惰梯度下降, 动态遗憾, FTRL框架, 比较器路径长度

## 3 点简述
- 核心问题：在线学习中贪婪更新与懒惰更新之间的权衡，涉及命中成本和移动成本。
- 方法要点：基于FTRL框架，引入懒惰松弛参数k，连接OGD和懒惰GD，分析懒惰性与比较器路径长度的关系。
- 实验或效果：证明k-lazyGD在特定松弛范围内达到最优动态遗憾，无需牺牲命中性能。

## 摘要（原文）

> We introduce $k$-lazyGD, an online learning algorithm that bridges the gap between greedy Online Gradient Descent (OGD, for $k=1$) and lazy GD/dual-averaging (for $k=T$), creating a spectrum between reactive and stable updates. We analyze this spectrum in Smoothed Online Convex Optimization (SOCO), where the learner incurs both hitting and movement costs. Our main contribution is establishing that laziness is possible without sacrificing hitting performance: we prove that $k$-lazyGD achieves the optimal dynamic regret $\mathcal{O}(\sqrt{(P_T+1)T})$ for any laziness slack $k$ up to $Θ(\sqrt{T/P_T})$, where $P_T$ is the comparator path length. This result formally connects the allowable laziness to the comparator's shifts, showing that $k$-lazyGD can retain the inherently small movements of lazy methods without compromising tracking ability. We base our analysis on the Follow the Regularized Leader (FTRL) framework, and derive a matching lower bound. Since the slack depends on $P_T$, an ensemble of learners with various slacks is used, yielding a method that is provably stable when it can be, and agile when it must be.

