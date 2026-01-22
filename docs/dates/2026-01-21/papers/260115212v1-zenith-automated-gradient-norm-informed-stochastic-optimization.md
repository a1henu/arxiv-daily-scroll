---
layout: default
title: ZENITH: Automated Gradient Norm Informed Stochastic Optimization
---

# ZENITH: Automated Gradient Norm Informed Stochastic Optimization
**arXiv**：[2601.15212v1](https://arxiv.org/abs/2601.15212) · [PDF](https://arxiv.org/pdf/2601.15212.pdf)  
**作者**：Dhrubo Saha  

**一句话要点**：提出ZENITH优化器，利用梯度范数演化自动调整学习率，提升计算机视觉模型训练效率与性能。

**关键词**：自适应优化器, 梯度范数, 学习率调度, 计算机视觉, 模型训练

## 3 点简述
- 问题：现有自适应优化器存在计算开销大、与正则化不兼容及学习率选择次优等问题。
- 方法：基于梯度范数的时间演化自动调整学习率，实现零开销优化。
- 效果：在图像分类、目标检测等任务中，以更短时间达到更高准确率，且兼容正则化。

## 摘要（原文）

> Training deep computer vision models requires manual oversight or hyperparameter tuning of the learning rate (LR) schedule. While existing adaptive optimizers schedule the LR automatically, they suffer from computational and memory overhead, incompatibility with regularization, and suboptimal LR choices. In this work, we introduce the ZENITH (Zero-overhead Evolution using Norm-Informed Training History) optimizer, which adapts the LR using the temporal evolution of the gradient norm. Image classification experiments spanning 6 CNN architectures and 6 benchmarks demonstrate that ZENITH achieves higher test accuracy in lower wall-clock time than baselines. It also yielded superior mAP in object detection, keypoint detection, and instance segmentation on MS COCO using the R-CNN family of models. Furthermore, its compatibility with regularization enables even better generalization.

