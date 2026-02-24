---
layout: default
title: CLCR: Cross-Level Semantic Collaborative Representation for Multimodal Learning
---

# CLCR: Cross-Level Semantic Collaborative Representation for Multimodal Learning
**arXiv**：[2602.19605v1](https://arxiv.org/abs/2602.19605) · [PDF](https://arxiv.org/pdf/2602.19605.pdf)  
**作者**：Chunlei Meng, Guanhong Huang, Rong Fu, Runmin Jian, Zhongxue Gan, Chun Ouyang  

**一句话要点**：提出跨层级语义协同表示（CLCR）以解决多模态学习中语义错位和错误传播问题。

**关键词**：多模态学习, 语义层级, 跨模态交互, 共享私有特征分离, 情感识别, 事件定位

## 3 点简述
- 核心问题：现有方法将多模态数据投影到单一潜在空间，忽略异步多级语义结构，导致语义错位和错误传播。
- 方法要点：CLCR通过语义层级编码器对齐浅、中、深层特征，并在每级使用IntraCED和InterCAD约束跨模态交互，分离共享与私有语义。
- 实验或效果：在六个基准测试中，CLCR在情感识别、事件定位等任务上表现优异，具有良好的泛化能力。

## 摘要（原文）

> Multimodal learning aims to capture both shared and private information from multiple modalities. However, existing methods that project all modalities into a single latent space for fusion often overlook the asynchronous, multi-level semantic structure of multimodal data. This oversight induces semantic misalignment and error propagation, thereby degrading representation quality. To address this issue, we propose Cross-Level Co-Representation (CLCR), which explicitly organizes each modality's features into a three-level semantic hierarchy and specifies level-wise constraints for cross-modal interactions. First, a semantic hierarchy encoder aligns shallow, mid, and deep features across modalities, establishing a common basis for interaction. And then, at each level, an Intra-Level Co-Exchange Domain (IntraCED) factorizes features into shared and private subspaces and restricts cross-modal attention to the shared subspace via a learnable token budget. This design ensures that only shared semantics are exchanged and prevents leakage from private channels. To integrate information across levels, the Inter-Level Co-Aggregation Domain (InterCAD) synchronizes semantic scales using learned anchors, selectively fuses the shared representations, and gates private cues to form a compact task representation. We further introduce regularization terms to enforce separation of shared and private features and to minimize cross-level interference. Experiments on six benchmarks spanning emotion recognition, event localization, sentiment analysis, and action recognition show that CLCR achieves strong performance and generalizes well across tasks.

