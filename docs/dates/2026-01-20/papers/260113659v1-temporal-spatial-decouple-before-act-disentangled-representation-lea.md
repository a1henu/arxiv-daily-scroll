---
layout: default
title: Temporal-Spatial Decouple before Act: Disentangled Representation Learning for Multimodal Sentiment Analysis
---

# Temporal-Spatial Decouple before Act: Disentangled Representation Learning for Multimodal Sentiment Analysis
**arXiv**：[2601.13659v1](https://arxiv.org/abs/2601.13659) · [PDF](https://arxiv.org/pdf/2601.13659.pdf)  
**作者**：Chunlei Meng, Ziyang Zhou, Lucas He, Xiaojing Du, Chun Ouyang, Zhongxue Gan  

**一句话要点**：提出TSDA方法，通过时空解耦与对齐解决多模态情感分析中的时空异构性问题。

**关键词**：多模态情感分析, 时空解耦, 特征对齐, 去相关正则化, 跨模态学习

## 3 点简述
- 核心问题：现有方法忽略时空异构性，导致信息不对称和性能受限。
- 方法要点：在交互前将各模态解耦为时空特征，并进行跨模态对齐与去相关正则化。
- 实验或效果：实验表明TSDA优于基线，消融分析验证了设计的必要性和可解释性。

## 摘要（原文）

> Multimodal Sentiment Analysis integrates Linguistic, Visual, and Acoustic. Mainstream approaches based on modality-invariant and modality-specific factorization or on complex fusion still rely on spatiotemporal mixed modeling. This ignores spatiotemporal heterogeneity, leading to spatiotemporal information asymmetry and thus limited performance. Hence, we propose TSDA, Temporal-Spatial Decouple before Act, which explicitly decouples each modality into temporal dynamics and spatial structural context before any interaction. For every modality, a temporal encoder and a spatial encoder project signals into separate temporal and spatial body. Factor-Consistent Cross-Modal Alignment then aligns temporal features only with their temporal counterparts across modalities, and spatial features only with their spatial counterparts. Factor specific supervision and decorrelation regularization reduce cross factor leakage while preserving complementarity. A Gated Recouple module subsequently recouples the aligned streams for task. Extensive experiments show that TSDA outperforms baselines. Ablation analysis studies confirm the necessity and interpretability of the design.

