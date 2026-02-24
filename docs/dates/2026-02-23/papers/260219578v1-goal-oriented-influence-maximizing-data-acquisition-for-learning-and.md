---
layout: default
title: Goal-Oriented Influence-Maximizing Data Acquisition for Learning and Optimization
---

# Goal-Oriented Influence-Maximizing Data Acquisition for Learning and Optimization
**arXiv**：[2602.19578v1](https://arxiv.org/abs/2602.19578) · [PDF](https://arxiv.org/pdf/2602.19578.pdf)  
**作者**：Weichi Yao, Bianca Dumitrascu, Bryan R. Goldsmith, Yixin Wang  

**一句话要点**：提出GOIMDA算法，通过目标导向影响最大化实现高效主动数据采集，适用于学习和优化任务。

**关键词**：主动学习, 数据采集, 影响函数, 目标导向优化, 不确定性感知

## 3 点简述
- 核心问题：主动数据采集依赖不可靠的预测不确定性估计，导致效率低下。
- 方法要点：利用一阶影响函数，结合目标梯度、训练损失曲率和候选敏感性，避免显式后验推断。
- 实验或效果：在图像分类、文本分类和优化任务中，比基线方法显著减少样本或评估次数。

## 摘要（原文）

> Active data acquisition is central to many learning and optimization tasks in deep neural networks, yet remains challenging because most approaches rely on predictive uncertainty estimates that are difficult to obtain reliably. To this end, we propose Goal-Oriented Influence- Maximizing Data Acquisition (GOIMDA), an active acquisition algorithm that avoids explicit posterior inference while remaining uncertainty-aware through inverse curvature. GOIMDA selects inputs by maximizing their expected influence on a user-specified goal functional, such as test loss, predictive entropy, or the value of an optimizer-recommended design. Leveraging first-order influence functions, we derive a tractable acquisition rule that combines the goal gradient, training-loss curvature, and candidate sensitivity to model parameters. We show theoretically that, for generalized linear models, GOIMDA approximates predictive-entropy minimization up to a correction term accounting for goal alignment and prediction bias, thereby, yielding uncertainty-aware behavior without maintaining a Bayesian posterior. Empirically, across learning tasks (including image and text classification) and optimization tasks (including noisy global optimization benchmarks and neural-network hyperparameter tuning), GOIMDA consistently reaches target performance with substantially fewer labeled samples or function evaluations than uncertainty-based active learning and Gaussian-process Bayesian optimization baselines.

