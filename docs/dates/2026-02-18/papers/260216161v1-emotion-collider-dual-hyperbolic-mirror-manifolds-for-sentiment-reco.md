---
layout: default
title: Emotion Collider: Dual Hyperbolic Mirror Manifolds for Sentiment Recovery via Anti Emotion Reflection
---

# Emotion Collider: Dual Hyperbolic Mirror Manifolds for Sentiment Recovery via Anti Emotion Reflection
**arXiv**：[2602.16161v1](https://arxiv.org/abs/2602.16161) · [PDF](https://arxiv.org/pdf/2602.16161.pdf)  
**作者**：Rong Fu, Ziming Wang, Shuo Yin, Wenxin Zhang, Haiyun Wei, Kun Liu, Xianda Li, Zeli Su, Simon Fong  

**一句话要点**：提出Emotion Collider框架，通过双曲超图融合解决多模态情感建模中的噪声和部分模态缺失问题。

**关键词**：多模态情感建模, 双曲几何, 超图神经网络, 对比学习, 情感恢复

## 3 点简述
- 核心问题：多模态情感建模中，模态噪声或缺失影响情感恢复的鲁棒性和准确性。
- 方法要点：使用Poincare-ball嵌入表示模态层次，通过超图机制双向传递消息进行融合，并在双曲空间进行对比学习以增强类别分离。
- 实验或效果：在标准多模态情感基准测试中，EC-Net提升了准确性，尤其在模态部分可用或受噪声污染时表现更优。

## 摘要（原文）

> Emotional expression underpins natural communication and effective human-computer interaction. We present Emotion Collider (EC-Net), a hyperbolic hypergraph framework for multimodal emotion and sentiment modeling. EC-Net represents modality hierarchies using Poincare-ball embeddings and performs fusion through a hypergraph mechanism that passes messages bidirectionally between nodes and hyperedges. To sharpen class separation, contrastive learning is formulated in hyperbolic space with decoupled radial and angular objectives. High-order semantic relations across time steps and modalities are preserved via adaptive hyperedge construction. Empirical results on standard multimodal emotion benchmarks show that EC-Net produces robust, semantically coherent representations and consistently improves accuracy, particularly when modalities are partially available or contaminated by noise. These findings indicate that explicit hierarchical geometry combined with hypergraph fusion is effective for resilient multimodal affect understanding.

