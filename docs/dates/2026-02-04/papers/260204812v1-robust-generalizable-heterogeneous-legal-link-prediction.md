---
layout: default
title: Robust Generalizable Heterogeneous Legal Link Prediction
---

# Robust Generalizable Heterogeneous Legal Link Prediction
**arXiv**：[2602.04812v1](https://arxiv.org/abs/2602.04812) · [PDF](https://arxiv.org/pdf/2602.04812.pdf)  
**作者**：Lorenz Wendlinger, Simon Alexander Nonn, Abdullah Al Zubaer, Michael Granitzer  

**一句话要点**：提出基于边丢弃和特征拼接的鲁棒表示学习方法，以改进异构法律引文网络中的链接预测。

**关键词**：异构网络链接预测, 法律引文网络, 鲁棒表示学习, 多语言特征, 非对称解码器, 泛化能力

## 3 点简述
- 核心问题：异构法律引文网络链接预测的鲁棒性和泛化性不足。
- 方法要点：引入边丢弃和特征拼接学习更鲁棒的表示，并设计多语言节点特征与改进的非对称解码器。
- 实验或效果：错误率降低高达45%，并能泛化至新西兰等地理和语言不连续的数据。

## 摘要（原文）

> Recent work has applied link prediction to large heterogeneous legal citation networks \new{with rich meta-features}. We find that this approach can be improved by including edge dropout and feature concatenation for the learning of more robust representations, which reduces error rates by up to 45%. We also propose an approach based on multilingual node features with an improved asymmetric decoder for compatibility, which allows us to generalize and extend the prediction to more, geographically and linguistically disjoint, data from New Zealand. Our adaptations also improve inductive transferability between these disjoint legal systems.

