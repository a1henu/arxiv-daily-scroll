---
layout: default
title: Bridging Cognitive Neuroscience and Graph Intelligence: Hippocampus-Inspired Multi-View Hypergraph Learning for Web Finance Fraud
---

# Bridging Cognitive Neuroscience and Graph Intelligence: Hippocampus-Inspired Multi-View Hypergraph Learning for Web Finance Fraud
**arXiv**：[2601.11073v1](https://arxiv.org/abs/2601.11073) · [PDF](https://arxiv.org/pdf/2601.11073.pdf)  
**作者**：Rongkun Cui, Nana Zhang, Kun Zhu, Qi Zhang  

**一句话要点**：提出海马体启发的多视图超图学习模型HIMVH，以解决网络金融欺诈检测中的伪装和长尾分布问题。

**关键词**：网络金融欺诈检测, 多视图学习, 超图神经网络, 长尾分布, 认知神经科学启发

## 3 点简述
- 核心问题：现有图神经网络方法难以处理欺诈伪装和长尾数据分布，导致检测性能受限。
- 方法要点：受海马体启发，设计跨视图不一致感知和新颖性感知超图学习模块，捕捉行为异质性和罕见模式。
- 实验或效果：在六个数据集上平均AUC提升6.42%、F1提升9.74%、AP提升39.14%，优于15个先进模型。

## 摘要（原文）

> Online financial services constitute an essential component of contemporary web ecosystems, yet their openness introduces substantial exposure to fraud that harms vulnerable users and weakens trust in digital finance. Such threats have become a significant web harm that erodes societal fairness and affects the well being of online communities. However, existing detection methods based on graph neural networks (GNNs) struggle with two persistent challenges: (1) fraud camouflage, where malicious transactions mimic benign behaviors to evade detection, and (2) long-tailed data distributions, which obscure rare but critical fraudulent cases. To fill these gaps, we propose HIMVH, a Hippocampus-Inspired Multi-View Hypergraph learning model for web finance fraud detection. Specifically, drawing inspiration from the scene conflict monitoring role of the hippocampus, we design a cross-view inconsistency perception module that captures subtle discrepancies and behavioral heterogeneity across multiple transaction views. This module enables the model to identify subtle cross-view conflicts for detecting online camouflaged fraudulent behaviors. Furthermore, inspired by the match-mismatch novelty detection mechanism of the CA1 region, we introduce a novelty-aware hypergraph learning module that measures feature deviations from neighborhood expectations and adaptively reweights messages, thereby enhancing sensitivity to online rare fraud patterns in the long-tailed settings. Extensive experiments on six web-based financial fraud datasets demonstrate that HIMVH achieves 6.42\% improvement in AUC, 9.74\% in F1 and 39.14\% in AP on average over 15 SOTA models.

