---
layout: default
title: Disentangled Mode-Specific Representations for Tensor Time Series via Contrastive Learning
---

# Disentangled Mode-Specific Representations for Tensor Time Series via Contrastive Learning
**arXiv**：[2602.23663v1](https://arxiv.org/abs/2602.23663) · [PDF](https://arxiv.org/pdf/2602.23663.pdf)  
**作者**：Kohei Obata, Taichi Murayama, Zheng Chen, Yasuko Matsubara, Yasushi Sakurai  

**一句话要点**：提出MoST方法，通过对比学习解耦多模态张量时间序列的表示，提升分类与预测性能。

**关键词**：张量时间序列, 对比学习, 表示学习, 多模态分析, 解耦表示

## 3 点简述
- 核心问题：多模态张量时间序列结构复杂，难以学习丰富表示。
- 方法要点：使用张量切片降低复杂度，通过对比学习解耦模态特定与不变特征。
- 实验或效果：在真实数据集上，MoST在分类和预测准确率上优于现有方法。

## 摘要（原文）

> Multi-mode tensor time series (TTS) can be found in many domains, such as search engines and environmental monitoring systems. Learning representations of a TTS benefits various applications, but it is also challenging since the complexities inherent in the tensor hinder the realization of rich representations. In this paper, we propose a novel representation learning method designed specifically for TTS, namely MoST. Specifically, MoST uses a tensor slicing approach to reduce the complexity of the TTS structure and learns representations that can be disentangled into individual non-temporal modes. Each representation captures mode-specific features, which are the relationship between variables within the same mode, and mode-invariant features, which are in common in representations of different modes. We employ a contrastive learning framework to learn parameters; the loss function comprises two parts intended to learn representation in a mode-specific way and mode-invariant way, effectively exploiting disentangled representations as augmentations. Extensive experiments on real-world datasets show that MoST consistently outperforms the state-of-the-art methods in terms of classification and forecasting accuracy. Code is available at https://github.com/KoheiObata/MoST.

