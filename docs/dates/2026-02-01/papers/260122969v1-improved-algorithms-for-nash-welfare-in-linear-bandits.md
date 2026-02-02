---
layout: default
title: Improved Algorithms for Nash Welfare in Linear Bandits
---

# Improved Algorithms for Nash Welfare in Linear Bandits
**arXiv**：[2601.22969v1](https://arxiv.org/abs/2601.22969) · [PDF](https://arxiv.org/pdf/2601.22969.pdf)  
**作者**：Dhruv Sarkar, Nishant Pandey, Sayak Ray Chowdhury  

**一句话要点**：提出FairLinBandit框架以解决线性赌博机中Nash遗憾的次优性问题，并扩展至p均值遗憾。

**关键词**：线性赌博机, Nash遗憾, p均值遗憾, 公平性优化, 元算法框架, 实验验证

## 3 点简述
- 核心问题：现有线性赌博机中Nash遗憾的界限在维度d上存在次优性，源于证明技术依赖限制性集中不等式。
- 方法要点：引入新分析工具实现最优Nash遗憾界限，提出FairLinBandit元算法框架，基于Phased Elimination和UCB实例化。
- 实验或效果：在真实数据集生成的线性赌博机实例上，方法持续优于现有基线，验证了p均值遗憾的次线性性能。

## 摘要（原文）

> Nash regret has recently emerged as a principled fairness-aware performance metric for stochastic multi-armed bandits, motivated by the Nash Social Welfare objective. Although this notion has been extended to linear bandits, existing results suffer from suboptimality in ambient dimension $d$, stemming from proof techniques that rely on restrictive concentration inequalities. In this work, we resolve this open problem by introducing new analytical tools that yield an order-optimal Nash regret bound in linear bandits. Beyond Nash regret, we initiate the study of $p$-means regret in linear bandits, a unifying framework that interpolates between fairness and utility objectives and strictly generalizes Nash regret. We propose a generic algorithmic framework, FairLinBandit, that works as a meta-algorithm on top of any linear bandit strategy. We instantiate this framework using two bandit algorithms: Phased Elimination and Upper Confidence Bound, and prove that both achieve sublinear $p$-means regret for the entire range of $p$. Extensive experiments on linear bandit instances generated from real-world datasets demonstrate that our methods consistently outperform the existing state-of-the-art baseline.

