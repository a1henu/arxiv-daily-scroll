---
layout: default
title: When Gradient Optimization Is Not Enough: $\dagger$ Dispersive and Anchoring Geometric Regularizer for Multimodal Learning
---

# When Gradient Optimization Is Not Enough: $\dagger$ Dispersive and Anchoring Geometric Regularizer for Multimodal Learning
**arXiv**：[2601.21670v1](https://arxiv.org/abs/2601.21670) · [PDF](https://arxiv.org/pdf/2601.21670.pdf)  
**作者**：Zixuan Xia, Hao Wang, Pengcheng Weng, Yanyu Qian, Yangxin Xu, William Dan, Fei Wang  

**一句话要点**：提出几何感知正则化框架以解决多模态学习中的表示几何病理问题

**关键词**：多模态学习, 表示几何, 正则化框架, 模态内分散, 模态间锚定, 几何病理

## 3 点简述
- 核心问题：多模态学习存在表示几何病理，如模态内表示塌缩和样本级跨模态不一致
- 方法要点：引入轻量级正则化，包括模态内分散和模态间锚定约束，无需修改架构
- 实验或效果：在多个基准上提升多模态和单模态性能，有效缓解模态权衡

## 摘要（原文）

> Multimodal learning aims to integrate complementary information from heterogeneous modalities, yet strong optimization alone does not guaranty well-structured representations. Even under carefully balanced training schemes, multimodal models often exhibit geometric pathologies, including intra-modal representation collapse and sample-level cross-modal inconsistency, which degrade both unimodal robustness and multimodal fusion.
>   We identify representation geometry as a missing control axis in multimodal learning and propose \regName, a lightweight geometry-aware regularization framework. \regName enforces two complementary constraints on intermediate embeddings: an intra-modal dispersive regularization that promotes representation diversity, and an inter-modal anchoring regularization that bounds sample-level cross-modal drift without rigid alignment. The proposed regularizer is plug-and-play, requires no architectural modifications, and is compatible with various training paradigms.
>   Extensive experiments across multiple multimodal benchmarks demonstrate consistent improvements in both multimodal and unimodal performance, showing that explicitly regulating representation geometry effectively mitigates modality trade-offs.

