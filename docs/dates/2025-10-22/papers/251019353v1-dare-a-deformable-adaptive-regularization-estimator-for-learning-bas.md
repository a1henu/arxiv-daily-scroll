---
layout: default
title: DARE: A Deformable Adaptive Regularization Estimator for Learning-Based Medical Image Registration
---

# DARE: A Deformable Adaptive Regularization Estimator for Learning-Based Medical Image Registration
**arXiv**：[2510.19353v1](https://arxiv.org/abs/2510.19353) · [PDF](https://arxiv.org/pdf/2510.19353.pdf)  
**作者**：Ahsan Raza Siyal, Markus Haltmeier, Ruth Steiger, Malik Galijasevic, Elke Ruth Gizewski, Astrid Ellen Grams  

**一句话要点**：提出DARE框架以解决医学图像配准中正则化不足问题

**关键词**：医学图像配准, 自适应正则化, 变形场优化, 折叠预防, 深度学习框架

## 3 点简述
- 核心问题：基于深度学习的医学图像配准方法常忽略正则化，影响鲁棒性和解剖合理性
- 方法要点：动态调整弹性正则化，整合应变和剪切能量项，并包含折叠预防机制
- 实验或效果：提高配准精度和解剖合理性，减少非物理伪影如折叠

## 摘要（原文）

> Deformable medical image registration is a fundamental task in medical image
> analysis. While deep learning-based methods have demonstrated superior accuracy
> and computational efficiency compared to traditional techniques, they often
> overlook the critical role of regularization in ensuring robustness and
> anatomical plausibility. We propose DARE (Deformable Adaptive Regularization
> Estimator), a novel registration framework that dynamically adjusts elastic
> regularization based on the gradient norm of the deformation field. Our
> approach integrates strain and shear energy terms, which are adaptively
> modulated to balance stability and flexibility. To ensure physically realistic
> transformations, DARE includes a folding-prevention mechanism that penalizes
> regions with negative deformation Jacobian. This strategy mitigates
> non-physical artifacts such as folding, avoids over-smoothing, and improves
> both registration accuracy and anatomical plausibility

