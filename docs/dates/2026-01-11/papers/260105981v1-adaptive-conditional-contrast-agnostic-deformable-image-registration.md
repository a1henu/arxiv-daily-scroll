---
layout: default
title: Adaptive Conditional Contrast-Agnostic Deformable Image Registration with Uncertainty Estimation
---

# Adaptive Conditional Contrast-Agnostic Deformable Image Registration with Uncertainty Estimation
**arXiv**：[2601.05981v1](https://arxiv.org/abs/2601.05981) · [PDF](https://arxiv.org/pdf/2601.05981.pdf)  
**作者**：Yinsong Wang, Xinzhe Luo, Siyi Du, Chen Qin  

**一句话要点**：提出自适应条件对比无关可变形图像配准框架，以解决多对比图像配准的泛化与不确定性估计问题。

**关键词**：可变形图像配准, 对比无关学习, 自适应特征调制, 不确定性估计, 多对比医学图像, 深度学习

## 3 点简述
- 核心问题：多对比图像配准中，传统方法耗时且学习型方法泛化性受限。
- 方法要点：基于随机卷积对比增强，引入自适应条件特征调制器与对比无关不确定性估计。
- 实验或效果：在配准精度和未见对比泛化上优于基线方法，提供可靠不确定性。

## 摘要（原文）

> Deformable multi-contrast image registration is a challenging yet crucial task due to the complex, non-linear intensity relationships across different imaging contrasts. Conventional registration methods typically rely on iterative optimization of the deformation field, which is time-consuming. Although recent learning-based approaches enable fast and accurate registration during inference, their generalizability remains limited to the specific contrasts observed during training. In this work, we propose an adaptive conditional contrast-agnostic deformable image registration framework (AC-CAR) based on a random convolution-based contrast augmentation scheme. AC-CAR can generalize to arbitrary imaging contrasts without observing them during training. To encourage contrast-invariant feature learning, we propose an adaptive conditional feature modulator (ACFM) that adaptively modulates the features and the contrast-invariant latent regularization to enforce the consistency of the learned feature across different imaging contrasts. Additionally, we enable our framework to provide contrast-agnostic registration uncertainty by integrating a variance network that leverages the contrast-agnostic registration encoder to improve the trustworthiness and reliability of AC-CAR. Experimental results demonstrate that AC-CAR outperforms baseline methods in registration accuracy and exhibits superior generalization to unseen imaging contrasts. Code is available at https://github.com/Yinsong0510/AC-CAR.

