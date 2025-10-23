---
layout: default
title: How to Evaluate Monocular Depth Estimation?
---

# How to Evaluate Monocular Depth Estimation?
**arXiv**：[2510.19814v1](https://arxiv.org/abs/2510.19814) · [PDF](https://arxiv.org/pdf/2510.19814.pdf)  
**作者**：Siyang Wu, Jack Nugent, Willow Yang, Jia Deng  

**一句话要点**：提出基于相对表面法线的新指标以改进单目深度估计评估

**关键词**：单目深度估计, 评估指标, 表面法线, 扰动分析, 人类对齐

## 3 点简述
- 核心问题：现有单目深度估计评估指标缺乏标准化，对扰动敏感度不足。
- 方法要点：引入相对表面法线指标和可视化工具，提升与人类判断对齐。
- 实验或效果：分析显示现有指标对曲率扰动不敏感，新指标改善评估效果。

## 摘要（原文）

> Monocular depth estimation is an important task with rapid progress, but how
> to evaluate it remains an open question, as evidenced by a lack of
> standardization in existing literature and a large selection of evaluation
> metrics whose trade-offs and behaviors are not well understood. This paper
> contributes a novel, quantitative analysis of existing metrics in terms of
> their sensitivity to various types of perturbations of ground truth,
> emphasizing comparison to human judgment. Our analysis reveals that existing
> metrics are severely under-sensitive to curvature perturbation such as making
> flat surfaces wavy. To remedy this, we introduce a new metric based on relative
> surface normals, along with new depth visualization tools and a principled
> method to create composite metrics with better human alignment. Code and data
> are available at: https://github.com/princeton-vl/evalmde.

