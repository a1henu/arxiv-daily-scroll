---
layout: default
title: SPADE: Sparsity Adaptive Depth Estimator for Zero-Shot, Real-Time, Monocular Depth Estimation in Underwater Environments
---

# SPADE: Sparsity Adaptive Depth Estimator for Zero-Shot, Real-Time, Monocular Depth Estimation in Underwater Environments
**arXiv**：[2510.25463v1](https://arxiv.org/abs/2510.25463) · [PDF](https://arxiv.org/pdf/2510.25463.pdf)  
**作者**：Hongjie Zhang, Gideon Billings, Stefan B. Williams  

**一句话要点**：提出SPADE稀疏自适应深度估计器，用于水下环境的零样本实时单目深度估计。

**关键词**：单目深度估计, 水下视觉, 稀疏深度先验, 实时处理, 度量尺度深度, 零样本学习

## 3 点简述
- 核心问题：水下基础设施检查中，人类或遥控车辆面临感知挑战，尤其在复杂结构或浑浊水域。
- 方法要点：结合预训练相对深度估计器与稀疏深度先验，通过两阶段方法生成度量尺度深度图。
- 实验或效果：在嵌入式硬件上运行超15 FPS，精度和泛化性优于现有基线，支持实际应用。

## 摘要（原文）

> Underwater infrastructure requires frequent inspection and maintenance due to
> harsh marine conditions. Current reliance on human divers or remotely operated
> vehicles is limited by perceptual and operational challenges, especially around
> complex structures or in turbid water. Enhancing the spatial awareness of
> underwater vehicles is key to reducing piloting risks and enabling greater
> autonomy. To address these challenges, we present SPADE: SParsity Adaptive
> Depth Estimator, a monocular depth estimation pipeline that combines
> pre-trained relative depth estimator with sparse depth priors to produce dense,
> metric scale depth maps. Our two-stage approach first scales the relative depth
> map with the sparse depth points, then refines the final metric prediction with
> our proposed Cascade Conv-Deformable Transformer blocks. Our approach achieves
> improved accuracy and generalisation over state-of-the-art baselines and runs
> efficiently at over 15 FPS on embedded hardware, promising to support practical
> underwater inspection and intervention. This work has been submitted to IEEE
> Journal of Oceanic Engineering Special Issue of AUV 2026.

