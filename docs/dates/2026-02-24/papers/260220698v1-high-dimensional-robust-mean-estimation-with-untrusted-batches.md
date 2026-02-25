---
layout: default
title: High-Dimensional Robust Mean Estimation with Untrusted Batches
---

# High-Dimensional Robust Mean Estimation with Untrusted Batches
**arXiv**：[2602.20698v1](https://arxiv.org/abs/2602.20698) · [PDF](https://arxiv.org/pdf/2602.20698.pdf)  
**作者**：Maryam Aliakbarpour, Vladimir Braverman, Yuhan Liu, Junze Yin  

**一句话要点**：提出基于平方和算法的高维鲁棒均值估计方法，处理批次数据中的双重腐败问题。

**关键词**：高维鲁棒估计, 批次数据腐败, 平方和算法, 均值估计, 统计异质性, 恶意用户检测

## 3 点简述
- 研究高维均值估计，用户以批次贡献数据，存在恶意用户和统计异质性双重腐败。
- 使用平方和算法处理连续高维场景，考虑均值偏移或样本级腐败两种偏差模型。
- 算法达到极小极大最优误差率，显示批次结构能抑制恶意用户影响，误差率与腐败参数相关。

## 摘要（原文）

> We study high-dimensional mean estimation in a collaborative setting where data is contributed by $N$ users in batches of size $n$. In this environment, a learner seeks to recover the mean $μ$ of a true distribution $P$ from a collection of sources that are both statistically heterogeneous and potentially malicious. We formalize this challenge through a double corruption landscape: an $\varepsilon$-fraction of users are entirely adversarial, while the remaining ``good'' users provide data from distributions that are related to $P$, but deviate by a proximity parameter $α$.
>   Unlike existing work on the untrusted batch model, which typically measures this deviation via total variation distance in discrete settings, we address the continuous, high-dimensional regime under two natural variants for deviation: (1) good batches are drawn from distributions with a mean-shift of $\sqrtα$, or (2) an $α$-fraction of samples within each good batch are adversarially corrupted. In particular, the second model presents significant new challenges: in high dimensions, unlike discrete settings, even a small fraction of sample-level corruption can shift empirical means and covariances arbitrarily.
>   We provide two Sum-of-Squares (SoS) based algorithms to navigate this tiered corruption. Our algorithms achieve the minimax-optimal error rate $O(\sqrt{\varepsilon/n} + \sqrt{d/nN} + \sqrtα)$, demonstrating that while heterogeneity $α$ represents an inherent statistical difficulty, the influence of adversarial users is suppressed by a factor of $1/\sqrt{n}$ due to the internal averaging afforded by the batch structure.

