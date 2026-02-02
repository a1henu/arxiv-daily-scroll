---
layout: default
title: Environment-Conditioned Tail Reweighting for Total Variation Invariant Risk Minimization
---

# Environment-Conditioned Tail Reweighting for Total Variation Invariant Risk Minimization
**arXiv**：[2601.22944v1](https://arxiv.org/abs/2601.22944) · [PDF](https://arxiv.org/pdf/2601.22944.pdf)  
**作者**：Wang Yuanchao, Lai Zhao-Rong, Zhong Tianqi, Li Fengnan  

**一句话要点**：提出环境条件尾部重加权方法，以增强总变差不变风险最小化，解决混合分布偏移下的OOD泛化问题。

**关键词**：分布外泛化, 不变风险最小化, 尾部重加权, 总变差, 混合分布偏移, 环境推断

## 3 点简述
- 核心问题：OOD泛化中同时存在环境级相关偏移和样本级多样性偏移，现有方法常忽略环境内样本异质性。
- 方法要点：结合环境级不变性与环境内鲁棒性，通过环境条件尾部重加权增强TV不变学习，并扩展至无环境标注场景。
- 实验或效果：在回归、表格、时间序列和图像分类基准上，混合分布偏移下，最差环境和平均OOD性能均获提升。

## 摘要（原文）

> Out-of-distribution (OOD) generalization remains challenging when models simultaneously encounter correlation shifts across environments and diversity shifts driven by rare or hard samples. Existing invariant risk minimization (IRM) methods primarily address spurious correlations at the environment level, but often overlook sample-level heterogeneity within environments, which can critically impact OOD performance. In this work, we propose \emph{Environment-Conditioned Tail Reweighting for Total Variation Invariant Risk Minimization} (ECTR), a unified framework that augments TV-based invariant learning with environment-conditioned tail reweighting to jointly address both types of distribution shift. By integrating environment-level invariance with within-environment robustness, the proposed approach makes these two mechanisms complementary under mixed distribution shifts. We further extend the framework to scenarios without explicit environment annotations by inferring latent environments through a minimax formulation. Experiments across regression, tabular, time-series, and image classification benchmarks under mixed distribution shifts demonstrate consistent improvements in both worst-environment and average OOD performance.

