---
layout: default
title: Decomposing Query-Key Feature Interactions Using Contrastive Covariances
---

# Decomposing Query-Key Feature Interactions Using Contrastive Covariances
**arXiv**：[2602.04752v1](https://arxiv.org/abs/2602.04752) · [PDF](https://arxiv.org/pdf/2602.04752.pdf)  
**作者**：Andrew Lee, Yonatan Belinkov, Fernanda Viégas, Martin Wattenberg  

**一句话要点**：提出对比协方差方法以分解Transformer注意力头中的查询-键空间为可解释组件

**关键词**：Transformer注意力机制, 查询-键空间分解, 可解释性分析, 对比协方差方法, 低秩子空间, 特征对齐

## 3 点简述
- 核心问题：Transformer注意力头中模型为何关注特定令牌缺乏解释工具
- 方法要点：使用对比协方差分解查询-键空间为低秩、可解释子空间
- 实验或效果：在简化设置和大语言模型中识别语义和绑定特征，并归因注意力分数

## 摘要（原文）

> Despite the central role of attention heads in Transformers, we lack tools to understand why a model attends to a particular token. To address this, we study the query-key (QK) space -- the bilinear joint embedding space between queries and keys. We present a contrastive covariance method to decompose the QK space into low-rank, human-interpretable components. It is when features in keys and queries align in these low-rank subspaces that high attention scores are produced. We first study our method both analytically and empirically in a simplified setting. We then apply our method to large language models to identify human-interpretable QK subspaces for categorical semantic features and binding features. Finally, we demonstrate how attention scores can be attributed to our identified features.

