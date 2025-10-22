---
layout: default
title: OpenInsGaussian: Open-vocabulary Instance Gaussian Segmentation with Context-aware Cross-view Fusion
---

# OpenInsGaussian: Open-vocabulary Instance Gaussian Segmentation with Context-aware Cross-view Fusion
**arXiv**：[2510.18253v1](https://arxiv.org/abs/2510.18253) · [PDF](https://arxiv.org/pdf/2510.18253.pdf)  
**作者**：Tianyu Huang, Runnan Chen, Dongting Hu, Fengming Huang, Mingming Gong, Tongliang Liu  

**一句话要点**：提出OpenInsGaussian框架，通过上下文感知特征提取和注意力驱动融合，提升开放词汇3D高斯分割性能。

**关键词**：3D场景理解, 高斯分割, 开放词汇分割, 多视图融合, 上下文感知特征

## 3 点简述
- 现有方法在预处理中缺乏上下文线索，多视图特征融合不一致且细节缺失。
- 采用上下文感知特征提取增强掩码语义，注意力驱动特征聚合优化多视图融合。
- 在基准数据集上实现最先进结果，显著优于现有基线，验证方法的鲁棒性和通用性。

## 摘要（原文）

> Understanding 3D scenes is pivotal for autonomous driving, robotics, and
> augmented reality. Recent semantic Gaussian Splatting approaches leverage
> large-scale 2D vision models to project 2D semantic features onto 3D scenes.
> However, they suffer from two major limitations: (1) insufficient contextual
> cues for individual masks during preprocessing and (2) inconsistencies and
> missing details when fusing multi-view features from these 2D models. In this
> paper, we introduce \textbf{OpenInsGaussian}, an \textbf{Open}-vocabulary
> \textbf{Ins}tance \textbf{Gaussian} segmentation framework with Context-aware
> Cross-view Fusion. Our method consists of two modules: Context-Aware Feature
> Extraction, which augments each mask with rich semantic context, and
> Attention-Driven Feature Aggregation, which selectively fuses multi-view
> features to mitigate alignment errors and incompleteness. Through extensive
> experiments on benchmark datasets, OpenInsGaussian achieves state-of-the-art
> results in open-vocabulary 3D Gaussian segmentation, outperforming existing
> baselines by a large margin. These findings underscore the robustness and
> generality of our proposed approach, marking a significant step forward in 3D
> scene understanding and its practical deployment across diverse real-world
> scenarios.

