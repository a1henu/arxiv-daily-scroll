---
layout: default
title: CAF-Mamba: Mamba-Based Cross-Modal Adaptive Attention Fusion for Multimodal Depression Detection
---

# CAF-Mamba: Mamba-Based Cross-Modal Adaptive Attention Fusion for Multimodal Depression Detection
**arXiv**：[2601.21648v1](https://arxiv.org/abs/2601.21648) · [PDF](https://arxiv.org/pdf/2601.21648.pdf)  
**作者**：Bowen Zhou, Marc-André Fiedler, Ayoub Al-Hamadi  

**一句话要点**：提出CAF-Mamba框架，基于Mamba实现跨模态自适应注意力融合，用于多模态抑郁症检测。

**关键词**：多模态抑郁症检测, 跨模态融合, 自适应注意力, Mamba模型, 心理健康分析

## 3 点简述
- 核心问题：现有方法依赖有限特征，忽视显式跨模态交互，融合方式简单。
- 方法要点：结合显式和隐式跨模态交互，通过模态注意力动态调整贡献。
- 实验或效果：在LMVD和D-Vlog数据集上超越现有方法，达到最优性能。

## 摘要（原文）

> Depression is a prevalent mental health disorder that severely impairs daily functioning and quality of life. While recent deep learning approaches for depression detection have shown promise, most rely on limited feature types, overlook explicit cross-modal interactions, and employ simple concatenation or static weighting for fusion. To overcome these limitations, we propose CAF-Mamba, a novel Mamba-based cross-modal adaptive attention fusion framework. CAF-Mamba not only captures cross-modal interactions explicitly and implicitly, but also dynamically adjusts modality contributions through a modality-wise attention mechanism, enabling more effective multimodal fusion. Experiments on two in-the-wild benchmark datasets, LMVD and D-Vlog, demonstrate that CAF-Mamba consistently outperforms existing methods and achieves state-of-the-art performance.

