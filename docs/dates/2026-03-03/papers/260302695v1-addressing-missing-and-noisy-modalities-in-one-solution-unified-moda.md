---
layout: default
title: Addressing Missing and Noisy Modalities in One Solution: Unified Modality-Quality Framework for Low-quality Multimodal Data
---

# Addressing Missing and Noisy Modalities in One Solution: Unified Modality-Quality Framework for Low-quality Multimodal Data
**arXiv**：[2603.02695v1](https://arxiv.org/abs/2603.02695) · [PDF](https://arxiv.org/pdf/2603.02695.pdf)  
**作者**：Sijie Mai, Shiqin Han, Haifeng Hu  

**一句话要点**：提出统一模态-质量框架以解决低质量多模态数据中的缺失和噪声问题

**关键词**：多模态情感计算, 模态质量估计, 表示增强, 专家混合, 鲁棒性提升

## 3 点简述
- 核心问题：现实多模态数据常含缺失或噪声模态，影响模型鲁棒性，现有方法多分开处理
- 方法要点：通过质量估计器、增强器和质量感知专家混合模块，统一处理低质量模态，提升表示质量
- 实验或效果：在完整、缺失和噪声模态设置下，UMQ在多个数据集上优于先进基线

## 摘要（原文）

> Multimodal data encountered in real-world scenarios are typically of low quality, with noisy modalities and missing modalities being typical forms that severely hinder model performance and robustness. However, prior works often handle noisy and missing modalities separately. In contrast, we jointly address missing and noisy modalities to enhance model robustness in low-quality data scenarios. We regard both noisy and missing modalities as a unified low-quality modality problem, and propose a unified modality-quality (UMQ) framework to enhance low-quality representations for multimodal affective computing. Firstly, we train a quality estimator with explicit supervised signals via a rank-guided training strategy that compares the relative quality of different representations by adding a ranking constraint, avoiding training noise caused by inaccurate absolute quality labels. Then, a quality enhancer for each modality is constructed, which uses the sample-specific information provided by other modalities and the modality-specific information provided by the defined modality baseline representation to enhance the quality of unimodal representations. Finally, we propose a quality-aware mixture-of-experts module with particular routing mechanism to enable multiple modality-quality problems to be addressed more specifically. UMQ consistently outperforms state-of-the-art baselines on multiple datasets under the settings of complete, missing, and noisy modalities.

