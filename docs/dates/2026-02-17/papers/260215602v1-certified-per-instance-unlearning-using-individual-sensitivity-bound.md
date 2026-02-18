---
layout: default
title: Certified Per-Instance Unlearning Using Individual Sensitivity Bounds
---

# Certified Per-Instance Unlearning Using Individual Sensitivity Bounds
**arXiv**：[2602.15602v1](https://arxiv.org/abs/2602.15602) · [PDF](https://arxiv.org/pdf/2602.15602.pdf)  
**作者**：Hanna Benarroch, Jamal Atif, Olivier Cappé  

**一句话要点**：提出基于个体敏感度界的认证逐实例遗忘方法，以减少噪声注入并提升性能。

**关键词**：认证遗忘, 逐实例差分隐私, 个体敏感度界, 岭回归, Langevin动态, 噪声校准

## 3 点简述
- 核心问题：传统认证遗忘依赖最坏情况敏感度，导致噪声过大和性能下降。
- 方法要点：利用逐实例差分隐私定义个体敏感度，为岭回归的Langevin动态推导高概率敏感度界。
- 实验或效果：在线性设置中验证理论，并在深度学习环境中提供实证证据，显示噪声减少。

## 摘要（原文）

> Certified machine unlearning can be achieved via noise injection leading to differential privacy guarantees, where noise is calibrated to worst-case sensitivity. Such conservative calibration often results in performance degradation, limiting practical applicability. In this work, we investigate an alternative approach based on adaptive per-instance noise calibration tailored to the individual contribution of each data point to the learned solution. This raises the following challenge: how can one establish formal unlearning guarantees when the mechanism depends on the specific point to be removed? To define individual data point sensitivities in noisy gradient dynamics, we consider the use of per-instance differential privacy. For ridge regression trained via Langevin dynamics, we derive high-probability per-instance sensitivity bounds, yielding certified unlearning with substantially less noise injection. We corroborate our theoretical findings through experiments in linear settings and provide further empirical evidence on the relevance of the approach in deep learning settings.

