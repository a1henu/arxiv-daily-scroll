---
layout: default
title: Towards Explainable Quantum AI: Informing the Encoder Selection of Quantum Neural Networks via Visualization
---

# Towards Explainable Quantum AI: Informing the Encoder Selection of Quantum Neural Networks via Visualization
**arXiv**：[2512.14181v1](https://arxiv.org/abs/2512.14181) · [PDF](https://arxiv.org/pdf/2512.14181.pdf)  
**作者**：Shaolun Ruan, Feng Liang, Rohan Ramakrishna, Chao Ren, Rudai Yan, Qiang Guan, Jiannan Li, Yong Wang  

**一句话要点**：提出XQAI-Eyes可视化工具以解决量子神经网络编码器选择难题

**关键词**：量子神经网络, 编码器选择, 可视化工具, 量子人工智能, 特征映射, 模式保留

## 3 点简述
- 核心问题：量子神经网络编码器选择缺乏系统指导，难以评估编码状态和分析特征区分能力
- 方法要点：开发XQAI-Eyes工具，通过可视化比较经典数据特征与编码量子状态，支持跨类混合态分析
- 实验或效果：在多数据集和编码器设计中评估，展示工具能辅助探索编码器设计与性能关系，并推导出基于模式保留和特征映射的编码器选择实践

## 摘要（原文）

> Quantum Neural Networks (QNNs) represent a promising fusion of quantum computing and neural network architectures, offering speed-ups and efficient processing of high-dimensional, entangled data. A crucial component of QNNs is the encoder, which maps classical input data into quantum states. However, choosing suitable encoders remains a significant challenge, largely due to the lack of systematic guidance and the trial-and-error nature of current approaches. This process is further impeded by two key challenges: (1) the difficulty in evaluating encoded quantum states prior to training, and (2) the lack of intuitive methods for analyzing an encoder's ability to effectively distinguish data features. To address these issues, we introduce a novel visualization tool, XQAI-Eyes, which enables QNN developers to compare classical data features with their corresponding encoded quantum states and to examine the mixed quantum states across different classes. By bridging classical and quantum perspectives, XQAI-Eyes facilitates a deeper understanding of how encoders influence QNN performance. Evaluations across diverse datasets and encoder designs demonstrate XQAI-Eyes's potential to support the exploration of the relationship between encoder design and QNN effectiveness, offering a holistic and transparent approach to optimizing quantum encoders. Moreover, domain experts used XQAI-Eyes to derive two key practices for quantum encoder selection, grounded in the principles of pattern preservation and feature mapping.

