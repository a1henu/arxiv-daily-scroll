---
layout: default
title: SLD: Segmentation-Based Landmark Detection for Spinal Ligaments
---

# SLD: Segmentation-Based Landmark Detection for Spinal Ligaments
**arXiv**：[2601.16782v1](https://arxiv.org/abs/2601.16782) · [PDF](https://arxiv.org/pdf/2601.16782.pdf)  
**作者**：Lara Blomenkamp, Ivanna Kramer, Sabine Bauer, Theresa Schöche  

**一句话要点**：提出基于分割的脊柱韧带标志点检测方法，以提升生物力学建模精度与泛化能力。

**关键词**：脊柱韧带检测, 3D椎骨分割, 生物力学建模, 标志点识别, 医学图像分析

## 3 点简述
- 核心问题：现有自动化方法在脊柱韧带标志点检测中区域受限或精度不足，影响生物力学模型可靠性。
- 方法要点：先进行基于形状的3D椎骨分割，再应用领域特定规则识别不同类型韧带附着点。
- 实验或效果：在两个独立脊柱数据集上验证，平均绝对误差0.7毫米，均方根误差1.1毫米，优于现有方法。

## 摘要（原文）

> In biomechanical modeling, the representation of ligament attachments is crucial for a realistic simulation of the forces acting between the vertebrae. These forces are typically modeled as vectors connecting ligament landmarks on adjacent vertebrae, making precise identification of these landmarks a key requirement for constructing reliable spine models. Existing automated detection methods are either limited to specific spinal regions or lack sufficient accuracy. This work presents a novel approach for detecting spinal ligament landmarks, which first performs shape-based segmentation of 3D vertebrae and subsequently applies domain-specific rules to identify different types of attachment points. The proposed method outperforms existing approaches by achieving high accuracy and demonstrating strong generalization across all spinal regions. Validation on two independent spinal datasets from multiple patients yielded a mean absolute error (MAE) of 0.7 mm and a root mean square error (RMSE) of 1.1 mm.

