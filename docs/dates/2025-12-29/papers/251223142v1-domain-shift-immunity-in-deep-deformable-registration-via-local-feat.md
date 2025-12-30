---
layout: default
title: Domain-Shift Immunity in Deep Deformable Registration via Local Feature Representations
---

# Domain-Shift Immunity in Deep Deformable Registration via Local Feature Representations
**arXiv**：[2512.23142v1](https://arxiv.org/abs/2512.23142) · [PDF](https://arxiv.org/pdf/2512.23142.pdf)  
**作者**：Mingzhen Shao, Sarang Joshi  

**一句话要点**：提出UniReg框架，通过局部特征表示实现深度可变形配准的域偏移免疫

**关键词**：可变形图像配准, 域偏移免疫, 局部特征表示, 深度学习, 多模态配准, 特征提取

## 3 点简述
- 核心问题：深度可变形配准模型对域偏移的敏感性机制未明，传统方法依赖大数据训练
- 方法要点：设计UniReg框架，分离特征提取与变形估计，使用预训练特征提取器增强局部特征一致性
- 实验或效果：在单数据集训练下，UniReg实现跨域和多模态的鲁棒性能，媲美基于优化的方法

## 摘要（原文）

> Deep learning has advanced deformable image registration, surpassing traditional optimization-based methods in both accuracy and efficiency. However, learning-based models are widely believed to be sensitive to domain shift, with robustness typically pursued through large and diverse training datasets, without explaining the underlying mechanisms. In this work, we show that domain-shift immunity is an inherent property of deep deformable registration models, arising from their reliance on local feature representations rather than global appearance for deformation estimation. To isolate and validate this mechanism, we introduce UniReg, a universal registration framework that decouples feature extraction from deformation estimation using fixed, pre-trained feature extractors and a UNet-based deformation network. Despite training on a single dataset, UniReg exhibits robust cross-domain and multi-modal performance comparable to optimization-based methods. Our analysis further reveals that failures of conventional CNN-based models under modality shift originate from dataset-induced biases in early convolutional layers. These findings identify local feature consistency as the key driver of robustness in learning-based deformable registration and motivate backbone designs that preserve domain-invariant local features.

