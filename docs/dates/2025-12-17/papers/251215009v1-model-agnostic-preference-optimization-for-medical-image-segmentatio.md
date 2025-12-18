---
layout: default
title: Model Agnostic Preference Optimization for Medical Image Segmentation
---

# Model Agnostic Preference Optimization for Medical Image Segmentation
**arXiv**：[2512.15009v1](https://arxiv.org/abs/2512.15009) · [PDF](https://arxiv.org/pdf/2512.15009.pdf)  
**作者**：Yunseong Nam, Jiwon Jang, Dongkyu Won, Sang Hyun Park, Soopil Kim  

**一句话要点**：提出模型无关偏好优化框架以提升医学图像分割的边界贴合与泛化能力

**关键词**：医学图像分割, 偏好优化, 模型无关训练, Dropout驱动采样, 边界贴合增强, 泛化能力提升

## 3 点简述
- 医学图像分割中偏好优化方法常受限于模型特定性和低多样性预测采样
- MAPO利用Dropout驱动的随机分割假设构建偏好一致梯度，无需直接真值监督
- 实验表明MAPO在多种数据集上增强边界贴合、减少过拟合并优化训练稳定性

## 摘要（原文）

> Preference optimization offers a scalable supervision paradigm based on relative preference signals, yet prior attempts in medical image segmentation remain model-specific and rely on low-diversity prediction sampling. In this paper, we propose MAPO (Model-Agnostic Preference Optimization), a training framework that utilizes Dropout-driven stochastic segmentation hypotheses to construct preference-consistent gradients without direct ground-truth supervision. MAPO is fully architecture- and dimensionality-agnostic, supporting 2D/3D CNN and Transformer-based segmentation pipelines. Comprehensive evaluations across diverse medical datasets reveal that MAPO consistently enhances boundary adherence, reduces overfitting, and yields more stable optimization dynamics compared to conventional supervised training.

