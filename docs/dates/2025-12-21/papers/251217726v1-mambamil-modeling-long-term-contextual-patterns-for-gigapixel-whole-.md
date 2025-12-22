---
layout: default
title: MambaMIL+: Modeling Long-Term Contextual Patterns for Gigapixel Whole Slide Image
---

# MambaMIL+: Modeling Long-Term Contextual Patterns for Gigapixel Whole Slide Image
**arXiv**：[2512.17726v1](https://arxiv.org/abs/2512.17726) · [PDF](https://arxiv.org/pdf/2512.17726.pdf)  
**作者**：Qian Zeng, Yihui Wang, Shu Yang, Yingxue Xu, Fengtao Zhou, Jiabo Ma, Dejia Cai, Zhengyu Zhang, Lijuan Qu, Yu Wang, Li Liang, Hao Chen  

**一句话要点**：提出MambaMIL+框架以解决全切片图像中长序列建模与空间上下文缺失问题

**关键词**：全切片图像分析, 多实例学习, 长序列建模, 空间上下文编码, 计算病理学

## 3 点简述
- 核心问题：全切片图像分辨率高且标注稀疏，传统多实例学习难以建模超长序列与空间上下文
- 方法要点：通过重叠扫描、选择性条纹位置编码和上下文令牌选择机制，增强空间上下文并保持长程依赖
- 实验或效果：在20个基准测试中，使用三种特征提取器均实现最优性能，验证了有效性和鲁棒性

## 摘要（原文）

> Whole-slide images (WSIs) are an important data modality in computational pathology, yet their gigapixel resolution and lack of fine-grained annotations challenge conventional deep learning models. Multiple instance learning (MIL) offers a solution by treating each WSI as a bag of patch-level instances, but effectively modeling ultra-long sequences with rich spatial context remains difficult. Recently, Mamba has emerged as a promising alternative for long sequence learning, scaling linearly to thousands of tokens. However, despite its efficiency, it still suffers from limited spatial context modeling and memory decay, constraining its effectiveness to WSI analysis. To address these limitations, we propose MambaMIL+, a new MIL framework that explicitly integrates spatial context while maintaining long-range dependency modeling without memory forgetting. Specifically, MambaMIL+ introduces 1) overlapping scanning, which restructures the patch sequence to embed spatial continuity and instance correlations; 2) a selective stripe position encoder (S2PE) that encodes positional information while mitigating the biases of fixed scanning orders; and 3) a contextual token selection (CTS) mechanism, which leverages supervisory knowledge to dynamically enlarge the contextual memory for stable long-range modeling. Extensive experiments on 20 benchmarks across diagnostic classification, molecular prediction, and survival analysis demonstrate that MambaMIL+ consistently achieves state-of-the-art performance under three feature extractors (ResNet-50, PLIP, and CONCH), highlighting its effectiveness and robustness for large-scale computational pathology

