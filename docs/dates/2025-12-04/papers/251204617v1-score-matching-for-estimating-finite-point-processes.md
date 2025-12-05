---
layout: default
title: Score Matching for Estimating Finite Point Processes
---

# Score Matching for Estimating Finite Point Processes
**arXiv**：[2512.04617v1](https://arxiv.org/abs/2512.04617) · [PDF](https://arxiv.org/pdf/2512.04617.pdf)  
**作者**：Haoqun Cao, Yixuan Zhang, Feng Zhou  

**一句话要点**：提出加权评分匹配估计器以解决有限点过程估计中的归一化问题

**关键词**：点过程估计, 评分匹配, Janossy测度, 时空建模, 非参数模型

## 3 点简述
- 核心问题：现有评分匹配方法在有限点过程上缺乏数学严谨分析，导致归一化问题无法唯一识别真实分布
- 方法要点：通过Janossy测度建立框架，引入自回归加权评分匹配估计器，并增强生存分类以解决非参数模型识别问题
- 实验或效果：在合成和真实时空数据集上验证方法能准确恢复强度，性能媲美最大似然估计且效率更高

## 摘要（原文）

> Score matching estimators have garnered significant attention in recent years because they eliminate the need to compute normalizing constants, thereby mitigating the computational challenges associated with maximum likelihood estimation (MLE).While several studies have proposed score matching estimators for point processes, this work highlights the limitations of these existing methods, which stem primarily from the lack of a mathematically rigorous analysis of how score matching behaves on finite point processes -- special random configurations on bounded spaces where many of the usual assumptions and properties of score matching no longer hold. To this end, we develop a formal framework for score matching on finite point processes via Janossy measures and, within this framework, introduce an (autoregressive) weighted score-matching estimator, whose statistical properties we analyze in classical parametric settings. For general nonparametric (e.g., deep) point process models, we show that score matching alone does not uniquely identify the ground-truth distribution due to subtle normalization issues, and we propose a simple survival-classification augmentation that yields a complete, integration-free training objective for any intensity-based point process model for spatio-temporal case. Experiments on synthetic and real-world temporal and spatio-temporal datasets, demonstrate that our method accurately recovers intensities and achieves performance comparable to MLE with better efficiency.

