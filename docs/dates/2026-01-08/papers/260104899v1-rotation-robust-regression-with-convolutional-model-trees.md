---
layout: default
title: Rotation-Robust Regression with Convolutional Model Trees
---

# Rotation-Robust Regression with Convolutional Model Trees
**arXiv**：[2601.04899v1](https://arxiv.org/abs/2601.04899) · [PDF](https://arxiv.org/pdf/2601.04899.pdf)  
**作者**：Hongyi Li, William Ward Armstrong, Jun Xu  

**一句话要点**：提出卷积模型树结合几何感知偏置与方向搜索，以增强图像回归在平面旋转下的鲁棒性。

**关键词**：旋转鲁棒学习, 卷积模型树, 几何感知偏置, 方向搜索, 图像回归, MNIST实验

## 3 点简述
- 研究图像输入在平面旋转下的鲁棒学习问题，使用卷积模型树作为基础框架。
- 引入卷积平滑、倾斜主导约束和重要性剪枝等几何感知偏置，量化其对旋转鲁棒性的影响。
- 评估部署时方向搜索策略，通过选择离散旋转提升严重旋转下的性能，但可能对标准方向有害。

## 摘要（原文）

> We study rotation-robust learning for image inputs using Convolutional Model Trees (CMTs) [1], whose split and leaf coefficients can be structured on the image grid and transformed geometrically at deployment time. In a controlled MNIST setting with a rotation-invariant regression target, we introduce three geometry-aware inductive biases for split directions -- convolutional smoothing, a tilt dominance constraint, and importance-based pruning -- and quantify their impact on robustness under in-plane rotations. We further evaluate a deployment-time orientation search that selects a discrete rotation maximizing a forest-level confidence proxy without updating model parameters. Orientation search improves robustness under severe rotations but can be harmful near the canonical orientation when confidence is misaligned with correctness. Finally, we observe consistent trends on MNIST digit recognition implemented as one-vs-rest regression, highlighting both the promise and limitations of confidence-based orientation selection for model-tree ensembles.

