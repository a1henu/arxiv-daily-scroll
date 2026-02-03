---
layout: default
title: Uncertainty-Aware Image Classification In Biomedical Imaging Using Spectral-normalized Neural Gaussian Processes
---

# Uncertainty-Aware Image Classification In Biomedical Imaging Using Spectral-normalized Neural Gaussian Processes
**arXiv**：[2602.02370v1](https://arxiv.org/abs/2602.02370) · [PDF](https://arxiv.org/pdf/2602.02370.pdf)  
**作者**：Uma Meleti, Jeffrey J. Nirschl  

**一句话要点**：提出谱归一化神经高斯过程以改进生物医学图像分类中的不确定性估计和分布外检测。

**关键词**：不确定性估计, 分布外检测, 数字病理学, 谱归一化, 高斯过程, 生物医学图像分类

## 3 点简述
- 核心问题：当前深度学习模型在数字病理学中过度自信且校准不佳，限制临床信任。
- 方法要点：通过谱归一化和高斯过程层替换，实现轻量级修改以提升单模型不确定性估计。
- 实验或效果：在三个生物医学分类任务上评估，SNGP保持分布内性能，显著改善不确定性估计和分布外检测。

## 摘要（原文）

> Accurate histopathologic interpretation is key for clinical decision-making; however, current deep learning models for digital pathology are often overconfident and poorly calibrated in out-of-distribution (OOD) settings, which limit trust and clinical adoption. Safety-critical medical imaging workflows benefit from intrinsic uncertainty-aware properties that can accurately reject OOD input. We implement the Spectral-normalized Neural Gaussian Process (SNGP), a set of lightweight modifications that apply spectral normalization and replace the final dense layer with a Gaussian process layer to improve single-model uncertainty estimation and OOD detection. We evaluate SNGP vs. deterministic and MonteCarlo dropout on six datasets across three biomedical classification tasks: white blood cells, amyloid plaques, and colorectal histopathology. SNGP has comparable in-distribution performance while significantly improving uncertainty estimation and OOD detection. Thus, SNGP or related models offer a useful framework for uncertainty-aware classification in digital pathology, supporting safe deployment and building trust with pathologists.

