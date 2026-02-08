---
layout: default
title: AP-OOD: Attention Pooling for Out-of-Distribution Detection
---

# AP-OOD: Attention Pooling for Out-of-Distribution Detection
**arXiv**：[2602.06031v1](https://arxiv.org/abs/2602.06031) · [PDF](https://arxiv.org/pdf/2602.06031.pdf)  
**作者**：Claus Hofmann, Christian Huber, Bernhard Lehner, Daniel Klotz, Sepp Hochreiter, Werner Zellinger  

**一句话要点**：提出AP-OOD方法，利用注意力池化提升自然语言分布外检测性能。

**关键词**：分布外检测, 注意力池化, 自然语言处理, 半监督学习, 词嵌入聚合

## 3 点简述
- 核心问题：如何有效聚合语言模型词嵌入以计算分布外分数。
- 方法要点：采用注意力池化超越平均聚合，半监督利用有限异常数据。
- 实验或效果：在XSUM和WMT15任务上显著降低FPR95，达到新SOTA。

## 摘要（原文）

> Out-of-distribution (OOD) detection, which maps high-dimensional data into a scalar OOD score, is critical for the reliable deployment of machine learning models. A key challenge in recent research is how to effectively leverage and aggregate token embeddings from language models to obtain the OOD score. In this work, we propose AP-OOD, a novel OOD detection method for natural language that goes beyond simple average-based aggregation by exploiting token-level information. AP-OOD is a semi-supervised approach that flexibly interpolates between unsupervised and supervised settings, enabling the use of limited auxiliary outlier data. Empirically, AP-OOD sets a new state of the art in OOD detection for text: in the unsupervised setting, it reduces the FPR95 (false positive rate at 95% true positives) from 27.84% to 4.67% on XSUM summarization, and from 77.08% to 70.37% on WMT15 En-Fr translation.

