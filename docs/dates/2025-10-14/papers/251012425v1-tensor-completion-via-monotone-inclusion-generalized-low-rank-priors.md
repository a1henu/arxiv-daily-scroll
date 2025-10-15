---
layout: default
title: Tensor Completion via Monotone Inclusion: Generalized Low-Rank Priors Meet Deep Denoisers
---

# Tensor Completion via Monotone Inclusion: Generalized Low-Rank Priors Meet Deep Denoisers
**arXiv**：[2510.12425v1](https://arxiv.org/abs/2510.12425) · [PDF](https://arxiv.org/pdf/2510.12425.pdf)  
**作者**：Peng Chen, Deliang Wei, Jiale Yao, Fang Li  

**一句话要点**：提出基于单调包含范式的张量补全框架，融合广义低秩先验与深度伪压缩去噪器

**关键词**：张量补全, 单调包含范式, 广义低秩先验, 深度去噪器, 全局收敛分析, 低采样率性能

## 3 点简述
- 核心问题：多维数据缺失条目影响下游分析，现有方法依赖经验收敛或不现实假设
- 方法要点：采用单调包含范式统一广义低秩先验与深度伪压缩去噪器，开发GTCTV DPC算法
- 实验或效果：在低采样率下，GTCTV DPC在定量指标和视觉质量上优于现有方法

## 摘要（原文）

> Missing entries in multi dimensional data pose significant challenges for
> downstream analysis across diverse real world applications. These data are
> naturally modeled as tensors, and recent completion methods integrating global
> low rank priors with plug and play denoisers have demonstrated strong empirical
> performance. However, these approaches often rely on empirical convergence
> alone or unrealistic assumptions, such as deep denoisers acting as proximal
> operators of implicit regularizers, which generally does not hold. To address
> these limitations, we propose a novel tensor completion framework grounded in
> the monotone inclusion paradigm, which unifies generalized low rank priors with
> deep pseudo contractive denoisers and extends beyond traditional convex
> optimization. Building on the Davis Yin splitting scheme, we develop the GTCTV
> DPC algorithm and rigorously establish its global convergence. Extensive
> experiments demonstrate that GTCTV DPC consistently outperforms existing
> methods in both quantitative metrics and visual quality, particularly at low
> sampling rates.

