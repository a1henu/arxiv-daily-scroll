---
layout: default
title: Mitigating Bias in Concept Bottleneck Models for Fair and Interpretable Image Classification
---

# Mitigating Bias in Concept Bottleneck Models for Fair and Interpretable Image Classification
**arXiv**：[2603.05899v1](https://arxiv.org/abs/2603.05899) · [PDF](https://arxiv.org/pdf/2603.05899.pdf)  
**作者**：Schrasing Tong, Antoine Salaun, Vincent Yuan, Annabel Adeyeri, Lalana Kagal  

**一句话要点**：提出三种偏差缓解技术以提升概念瓶颈模型的公平性和可解释性

**关键词**：概念瓶颈模型, 公平性, 可解释性, 偏差缓解, 图像分类, 对抗性去偏

## 3 点简述
- 概念瓶颈模型在图像分类中可能泄露敏感属性信息，导致公平性不足
- 采用top-k概念过滤、移除偏差概念和对抗性去偏三种方法减少信息泄露
- 实验表明在公平性与性能权衡上优于先前工作，实现更公平可解释的分类

## 摘要（原文）

> Ensuring fairness in image classification prevents models from perpetuating and amplifying bias. Concept bottleneck models (CBMs) map images to high-level, human-interpretable concepts before making predictions via a sparse, one-layer classifier. This structure enhances interpretability and, in theory, supports fairness by masking sensitive attribute proxies such as facial features. However, CBM concepts have been known to leak information unrelated to concept semantics and early results reveal only marginal reductions in gender bias on datasets like ImSitu. We propose three bias mitigation techniques to improve fairness in CBMs: 1. Decreasing information leakage using a top-k concept filter, 2. Removing biased concepts, and 3. Adversarial debiasing. Our results outperform prior work in terms of fairness-performance tradeoffs, indicating that our debiased CBM provides a significant step towards fair and interpretable image classification.

