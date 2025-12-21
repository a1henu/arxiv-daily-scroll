---
layout: default
title: Sharpness-aware Second-order Latent Factor Model for High-dimensional and Incomplete Data
---

# Sharpness-aware Second-order Latent Factor Model for High-dimensional and Incomplete Data
**arXiv**：[2512.16277v1](https://arxiv.org/abs/2512.16277) · [PDF](https://arxiv.org/pdf/2512.16277.pdf)  
**作者**：Jialiang Wang, Xueyan Bao, Hao Wu  

**一句话要点**：提出锐度感知二阶隐因子模型以优化高维不完整数据的表示学习

**关键词**：二阶隐因子模型, 锐度感知最小化, 高维不完整数据, 表示学习, 非凸优化

## 3 点简述
- 核心问题：二阶隐因子模型因双线性和非凸性导致优化困难，影响泛化能力。
- 方法要点：结合锐度感知最小化，通过Hessian-向量积获取二阶信息并注入锐度项。
- 实验或效果：在多个工业数据集上验证，模型性能优于现有基线方法。

## 摘要（原文）

> Second-order Latent Factor (SLF) model, a class of low-rank representation learning methods, has proven effective at extracting node-to-node interaction patterns from High-dimensional and Incomplete (HDI) data. However, its optimization is notoriously difficult due to its bilinear and non-convex nature. Sharpness-aware Minimization (SAM) has recently proposed to find flat local minima when minimizing non-convex objectives, thereby improving the generalization of representation-learning models. To address this challenge, we propose a Sharpness-aware SLF (SSLF) model. SSLF embodies two key ideas: (1) acquiring second-order information via Hessian-vector products; and (2) injecting a sharpness term into the curvature (Hessian) through the designed Hessian-vector products. Experiments on multiple industrial datasets demonstrate that the proposed model consistently outperforms state-of-the-art baselines.

