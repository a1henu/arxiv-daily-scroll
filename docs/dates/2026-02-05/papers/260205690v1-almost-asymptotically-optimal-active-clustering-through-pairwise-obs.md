---
layout: default
title: Almost Asymptotically Optimal Active Clustering Through Pairwise Observations
---

# Almost Asymptotically Optimal Active Clustering Through Pairwise Observations
**arXiv**：[2602.05690v1](https://arxiv.org/abs/2602.05690) · [PDF](https://arxiv.org/pdf/2602.05690.pdf)  
**作者**：Rachel S. Y. Teo, P. N. Karthik, Ramya Korlakai Vinayak, Vincent Y. F. Tan  

**一句话要点**：提出基于主动成对观测的聚类算法，在噪声反馈下实现渐近最优聚类

**关键词**：主动聚类, 成对观测, 噪声反馈, 渐近最优性, 广义似然比, 查询复杂度

## 3 点简述
- 研究噪声主动反馈下将M项聚类到未知K组的核心问题
- 利用测度变换技术建立查询次数下界，设计基于广义似然比统计的渐近最优算法
- 开发计算可行变体，性能与下界差距在常数倍内，通过实证估计验证

## 摘要（原文）

> We propose a new analysis framework for clustering $M$ items into an unknown number of $K$ distinct groups using noisy and actively collected responses. At each time step, an agent is allowed to query pairs of items and observe bandit binary feedback. If the pair of items belongs to the same (resp.\ different) cluster, the observed feedback is $1$ with probability $p>1/2$ (resp.\ $q<1/2$). Leveraging the ubiquitous change-of-measure technique, we establish a fundamental lower bound on the expected number of queries needed to achieve a desired confidence in the clustering accuracy, formulated as a sup-inf optimization problem. Building on this theoretical foundation, we design an asymptotically optimal algorithm in which the stopping criterion involves an empirical version of the inner infimum -- the Generalized Likelihood Ratio (GLR) statistic -- being compared to a threshold. We develop a computationally feasible variant of the GLR statistic and show that its performance gap to the lower bound can be accurately empirically estimated and remains within a constant multiple of the lower bound.

