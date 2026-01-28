---
layout: default
title: Pareto-Guided Optimization for Uncertainty-Aware Medical Image Segmentation
---

# Pareto-Guided Optimization for Uncertainty-Aware Medical Image Segmentation
**arXiv**：[2601.19365v1](https://arxiv.org/abs/2601.19365) · [PDF](https://arxiv.org/pdf/2601.19365.pdf)  
**作者**：Jinming Zhang, Xi Yang, Youpeng Yang, Haosen Shi, Yuyao Yan, Qiufeng Wang, Guangliang Cheng, Kaizhu Huang  

**一句话要点**：提出帕累托引导优化与模糊标注机制，以解决医学图像分割中边界区域不确定性高的问题。

**关键词**：医学图像分割, 不确定性建模, 帕累托优化, 模糊标注, 梯度稳定, 边界区域处理

## 3 点简述
- 核心问题：医学图像分割中边界区域不确定性高，传统训练方法导致早期优化不稳定。
- 方法要点：引入区域课程策略和帕累托一致损失，平衡区域间不确定性，并采用模糊标注机制稳定梯度。
- 实验或效果：在脑转移和非转移性肿瘤分割实验中，方法在所有肿瘤子区域均优于传统方法。

## 摘要（原文）

> Uncertainty in medical image segmentation is inherently non-uniform, with boundary regions exhibiting substantially higher ambiguity than interior areas. Conventional training treats all pixels equally, leading to unstable optimization during early epochs when predictions are unreliable. We argue that this instability hinders convergence toward Pareto-optimal solutions and propose a region-wise curriculum strategy that prioritizes learning from certain regions and gradually incorporates uncertain ones, reducing gradient variance. Methodologically, we introduce a Pareto-consistent loss that balances trade-offs between regional uncertainties by adaptively reshaping the loss landscape and constraining convergence dynamics between interior and boundary regions; this guides the model toward Pareto-approximate solutions. To address boundary ambiguity, we further develop a fuzzy labeling mechanism that maintains binary confidence in non-boundary areas while enabling smooth transitions near boundaries, stabilizing gradients, and expanding flat regions in the loss surface. Experiments on brain metastasis and non-metastatic tumor segmentation show consistent improvements across multiple configurations, with our method outperforming traditional crisp-set approaches in all tumor subregions.

