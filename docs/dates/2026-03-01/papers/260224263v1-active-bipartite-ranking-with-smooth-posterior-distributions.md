---
layout: default
title: Active Bipartite Ranking with Smooth Posterior Distributions
---

# Active Bipartite Ranking with Smooth Posterior Distributions
**arXiv**：[2602.24263v1](https://arxiv.org/abs/2602.24263) · [PDF](https://arxiv.org/pdf/2602.24263.pdf)  
**作者**：James Cheshire, Stephan Clémençon  

**一句话要点**：提出平滑排序算法以解决连续后验分布下的主动二分排序问题

**关键词**：主动学习, 二分排序, 连续后验分布, Hölder平滑性, PAC学习, ROC曲线优化

## 3 点简述
- 研究主动二分排序问题，扩展至连续后验分布场景，克服离散假设限制
- 提出平滑排序算法，基于Hölder平滑性约束，最小化ROC曲线与最优曲线的sup范数距离
- 理论证明算法为PAC(ε,δ)，提供采样时间上下界，数值实验验证性能优于替代方法

## 摘要（原文）

> In this article, bipartite ranking, a statistical learning problem involved in many applications and widely studied in the passive context, is approached in a much more general \textit{active setting} than the discrete one previously considered in the literature. While the latter assumes that the conditional distribution is piece wise constant, the framework we develop permits in contrast to deal with continuous conditional distributions, provided that they fulfill a Hölder smoothness constraint. We first show that a naive approach based on discretisation at a uniform level, fixed \textit{a priori} and consisting in applying next the active strategy designed for the discrete setting generally fails. Instead, we propose a novel algorithm, referred to as smooth-rank and designed for the continuous setting, which aims to minimise the distance between the ROC curve of the estimated ranking rule and the optimal one w.r.t. the $\sup$ norm. We show that, for a fixed confidence level $ε>0$ and probability $δ\in (0,1)$, smooth-rank is PAC$(ε,δ)$. In addition, we provide a problem dependent upper bound on the expected sampling time of smooth-rank and establish a problem dependent lower bound on the expected sampling time of any PAC$(ε,δ)$ algorithm. Beyond the theoretical analysis carried out, numerical results are presented, providing solid empirical evidence of the performance of the algorithm proposed, which compares favorably with alternative approaches.

