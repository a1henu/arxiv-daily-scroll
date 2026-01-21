---
layout: default
title: Insight: Interpretable Semantic Hierarchies in Vision-Language Encoders
---

# Insight: Interpretable Semantic Hierarchies in Vision-Language Encoders
**arXiv**：[2601.13798v1](https://arxiv.org/abs/2601.13798) · [PDF](https://arxiv.org/pdf/2601.13798.pdf)  
**作者**：Kai Wittenmayer, Sukrut Rao, Amin Parchami-Araghi, Bernt Schiele, Jonas Fischer  

**一句话要点**：提出Insight模型以解决视觉-语言编码器可解释性问题，提供细粒度、空间定位的概念解释。

**关键词**：视觉-语言编码器, 可解释性, 概念提取, 分层稀疏自编码器, 空间定位, 语义表示

## 3 点简述
- 核心问题：视觉-语言基础模型表示不透明，现有方法缺乏空间定位且局限于分类任务。
- 方法要点：利用分层稀疏自编码器和语义强的基础模型自动提取多粒度、可解释概念，通过概念关系改进命名和解释。
- 实验或效果：在基准数据上，Insight在分类和分割任务中性能与不透明模型竞争，同时提供高质量概念解释。

## 摘要（原文）

> Language-aligned vision foundation models perform strongly across diverse downstream tasks. Yet, their learned representations remain opaque, making interpreting their decision-making hard. Recent works decompose these representations into human-interpretable concepts, but provide poor spatial grounding and are limited to image classification tasks. In this work, we propose Insight, a language-aligned concept foundation model that provides fine-grained concepts, which are human-interpretable and spatially grounded in the input image. We leverage a hierarchical sparse autoencoder and a foundation model with strong semantic representations to automatically extract concepts at various granularities. Examining local co-occurrence dependencies of concepts allows us to define concept relationships. Through these relations we further improve concept naming and obtain richer explanations. On benchmark data, we show that Insight provides performance on classification and segmentation that is competitive with opaque foundation models while providing fine-grained, high quality concept-based explanations. Code is available at https://github.com/kawi19/Insight.

