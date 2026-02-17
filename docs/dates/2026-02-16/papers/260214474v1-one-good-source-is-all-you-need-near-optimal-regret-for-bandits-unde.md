---
layout: default
title: One Good Source is All You Need: Near-Optimal Regret for Bandits under Heterogeneous Noise
---

# One Good Source is All You Need: Near-Optimal Regret for Bandits under Heterogeneous Noise
**arXiv**：[2602.14474v1](https://arxiv.org/abs/2602.14474) · [PDF](https://arxiv.org/pdf/2602.14474.pdf)  
**作者**：Aadirupa Saha, Amith Bhat, Haipeng Luo  

**一句话要点**：提出SOAR算法以解决多源异方差噪声下的多臂老虎机问题，实现近最优遗憾界。

**关键词**：多臂老虎机, 异方差噪声, 遗憾最小化, 数据源选择, 方差优化, 自适应算法

## 3 点简述
- 研究多源异方差噪声下的多臂老虎机问题，需自适应选择数据源以最小化遗憾。
- 提出SOAR算法，通过方差集中界快速剪枝高方差源，结合平衡最小最大LCB-UCB方法识别最优臂和最小方差源。
- 理论分析显示SOAR达到接近单源最优遗憾界，实验在合成和真实数据集上验证其优越性能。

## 摘要（原文）

> We study $K$-armed Multiarmed Bandit (MAB) problem with $M$ heterogeneous data sources, each exhibiting unknown and distinct noise variances $\{σ_j^2\}_{j=1}^M$. The learner's objective is standard MAB regret minimization, with the additional complexity of adaptively selecting which data source to query from at each round. We propose Source-Optimistic Adaptive Regret minimization (SOAR), a novel algorithm that quickly prunes high-variance sources using sharp variance-concentration bounds, followed by a `balanced min-max LCB-UCB approach' that seamlessly integrates the parallel tasks of identifying the best arm and the optimal (minimum-variance) data source. Our analysis shows SOAR achieves an instance-dependent regret bound of $\tilde{O}\left({σ^*}^2\sum_{i=2}^K \frac{\log T}{Δ_i} + \sqrt{K \sum_{j=1}^M σ_j^2}\right)$, up to preprocessing costs depending only on problem parameters, where ${σ^*}^2 := \min_j σ_j^2$ is the minimum source variance and $Δ_i$ denotes the suboptimality gap of the $i$-th arm. This result is both surprising as despite lacking prior knowledge of the minimum-variance source among $M$ alternatives, SOAR attains the optimal instance-dependent regret of standard single-source MAB with variance ${σ^*}^2$, while incurring only an small (and unavoidable) additive cost of $\tilde O(\sqrt{K \sum_{j=1}^M σ_j^2})$ towards the optimal (minimum variance) source identification. Our theoretical bounds represent a significant improvement over some proposed baselines, e.g. Uniform UCB or Explore-then-Commit UCB, which could potentially suffer regret scaling with $σ_{\max}^2$ in place of ${σ^*}^2$-a gap that can be arbitrarily large when $σ_{\max} \gg σ^*$. Experiments on multiple synthetic problem instances and the real-world MovieLens\;25M dataset, demonstrating the superior performance of SOAR over the baselines.

