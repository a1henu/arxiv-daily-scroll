---
layout: default
title: Score Matching for Estimating Finite Point Processes
---

# Score Matching for Estimating Finite Point Processes
**arXiv**：[2512.04617v1](https://arxiv.org/abs/2512.04617) · [PDF](https://arxiv.org/pdf/2512.04617.pdf)  
**作者**：Haoqun Cao, Yixuan Zhang, Feng Zhou  

**一句话要点**：提出加权分数匹配估计器以解决有限点过程分数匹配的理论与应用问题

**关键词**：分数匹配, 有限点过程, Janossy测度, 时空点过程, 非参数估计, 计算效率

## 3 点简述
- 核心问题：现有分数匹配方法在有限点过程上缺乏数学严谨分析，导致假设失效和归一化问题。
- 方法要点：基于Janossy测度建立框架，引入自回归加权分数匹配估计器，并针对非参数模型提出生存分类增强。
- 实验或效果：在合成和真实时空数据集上验证方法能准确恢复强度，性能媲美最大似然估计且效率更高。

## 摘要（原文）

> Score matching estimators have garnered significant attention in recent years because they eliminate the need to compute normalizing constants, thereby mitigating the computational challenges associated with maximum likelihood estimation (MLE).While several studies have proposed score matching estimators for point processes, this work highlights the limitations of these existing methods, which stem primarily from the lack of a mathematically rigorous analysis of how score matching behaves on finite point processes -- special random configurations on bounded spaces where many of the usual assumptions and properties of score matching no longer hold. To this end, we develop a formal framework for score matching on finite point processes via Janossy measures and, within this framework, introduce an (autoregressive) weighted score-matching estimator, whose statistical properties we analyze in classical parametric settings. For general nonparametric (e.g., deep) point process models, we show that score matching alone does not uniquely identify the ground-truth distribution due to subtle normalization issues, and we propose a simple survival-classification augmentation that yields a complete, integration-free training objective for any intensity-based point process model for spatio-temporal case. Experiments on synthetic and real-world temporal and spatio-temporal datasets, demonstrate that our method accurately recovers intensities and achieves performance comparable to MLE with better efficiency.

