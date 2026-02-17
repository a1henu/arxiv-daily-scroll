---
layout: default
title: A Bayesian Approach to Low-Discrepancy Subset Selection
---

# A Bayesian Approach to Low-Discrepancy Subset Selection
**arXiv**：[2602.14607v1](https://arxiv.org/abs/2602.14607) · [PDF](https://arxiv.org/pdf/2602.14607.pdf)  
**作者**：Nathan Kirk  

**一句话要点**：提出贝叶斯优化方法以解决核差异子集选择问题的NP难性

**关键词**：子集选择, 核差异, 贝叶斯优化, NP难问题, 深度嵌入核, 低差异设计

## 3 点简述
- 核心问题：核差异子集选择被证明为NP难问题，难以高效求解
- 方法要点：利用深度嵌入核，设计贝叶斯优化框架来最小化差异度量
- 实验或效果：算法在减少差异方面表现良好，框架适用于多种设计标准

## 摘要（原文）

> Low-discrepancy designs play a central role in quasi-Monte Carlo methods and are increasingly influential in other domains such as machine learning, robotics and computer graphics, to name a few. In recent years, one such low-discrepancy construction method called subset selection has received a lot of attention. Given a large population, one optimally selects a small low-discrepancy subset with respect to a discrepancy-based objective. Versions of this problem are known to be NP-hard. In this text, we establish, for the first time, that the subset selection problem with respect to kernel discrepancies is also NP-hard. Motivated by this intractability, we propose a Bayesian Optimization procedure for the subset selection problem utilizing the recent notion of deep embedding kernels. We demonstrate the performance of the BO algorithm to minimize discrepancy measures and note that the framework is broadly applicable any design criteria.

