---
layout: default
title: Geometrically Constrained Outlier Synthesis
---

# Geometrically Constrained Outlier Synthesis
**arXiv**：[2603.08413v1](https://arxiv.org/abs/2603.08413) · [PDF](https://arxiv.org/pdf/2603.08413.pdf)  
**作者**：Daniil Karzanov, Marcin Detyniecki  

**一句话要点**：提出几何约束异常合成框架以提升图像分类模型的分布外鲁棒性

**关键词**：分布外检测, 几何约束合成, 对比正则化, 能量推断, 流形学习, 统计保证

## 3 点简述
- 核心问题：深度神经网络对分布外样本常表现出过度自信，影响鲁棒性。
- 方法要点：在隐藏特征空间生成尊重分布内流形结构的虚拟异常，结合对比正则化目标。
- 实验效果：在近分布外基准测试中优于现有方法，支持统计有效的异常检测。

## 摘要（原文）

> Deep neural networks for image classification often exhibit overconfidence on out-of-distribution (OOD) samples. To address this, we introduce Geometrically Constrained Outlier Synthesis (GCOS), a training-time regularization framework aimed at improving OOD robustness during inference. GCOS addresses a limitation of prior synthesis methods by generating virtual outliers in the hidden feature space that respect the learned manifold structure of in-distribution (ID) data. The synthesis proceeds in two stages: (i) a dominant-variance subspace extracted from the training features identifies geometrically informed, off-manifold directions; (ii) a conformally-inspired shell, defined by the empirical quantiles of a nonconformity score from a calibration set, adaptively controls the synthesis magnitude to produce boundary samples. The shell ensures that generated outliers are neither trivially detectable nor indistinguishable from in-distribution data, facilitating smoother learning of robust features. This is combined with a contrastive regularization objective that promotes separability of ID and OOD samples in a chosen score space, such as Mahalanobis or energy-based. Experiments demonstrate that GCOS outperforms state-of-the-art methods using standard energy-based inference on near-OOD benchmarks, defined as tasks where outliers share the same semantic domain as in-distribution data. As an exploratory extension, the framework naturally transitions to conformal OOD inference, which translates uncertainty scores into statistically valid p-values and enables thresholds with formal error guarantees, providing a pathway toward more predictable and reliable OOD detection.

