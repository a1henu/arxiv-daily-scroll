---
layout: default
title: Conformal Risk Control for Non-Monotonic Losses
---

# Conformal Risk Control for Non-Monotonic Losses
**arXiv**：[2602.20151v1](https://arxiv.org/abs/2602.20151) · [PDF](https://arxiv.org/pdf/2602.20151.pdf)  
**作者**：Anastasios N. Angelopoulos  

**一句话要点**：提出保形风险控制方法以处理非单调损失和多维参数场景

**关键词**：保形风险控制, 非单调损失, 多维参数, 算法稳定性, 风险控制保证, 选择性分类

## 3 点简述
- 核心问题：传统保形预测仅适用于单调损失，无法处理非单调损失和多维参数的风险控制。
- 方法要点：扩展保形风险控制，基于算法稳定性提供通用风险控制保证，适用于非单调损失和多维参数。
- 实验或效果：应用于选择性图像分类、肿瘤分割的FDR和IOU控制，以及重叠种族和性别群体的再犯预测去偏。

## 摘要（原文）

> Conformal risk control is an extension of conformal prediction for controlling risk functions beyond miscoverage. The original algorithm controls the expected value of a loss that is monotonic in a one-dimensional parameter. Here, we present risk control guarantees for generic algorithms applied to possibly non-monotonic losses with multidimensional parameters. The guarantees depend on the stability of the algorithm -- unstable algorithms have looser guarantees. We give applications of this technique to selective image classification, FDR and IOU control of tumor segmentations, and multigroup debiasing of recidivism predictions across overlapping race and sex groups using empirical risk minimization.

