---
layout: default
title: Variance & Greediness: A comparative study of metric-learning losses
---

# Variance & Greediness: A comparative study of metric-learning losses
**arXiv**：[2601.21450v1](https://arxiv.org/abs/2601.21450) · [PDF](https://arxiv.org/pdf/2601.21450.pdf)  
**作者**：Donghuo Zeng, Hao Niu, Zhi Li, Masato Taya  

**一句话要点**：提出VARIANCE和GREEDINESS诊断框架，比较七种度量学习损失在图像检索中的几何与优化特性。

**关键词**：度量学习, 图像检索, 损失函数分析, 嵌入几何, 优化动态, 诊断框架

## 3 点简述
- 核心问题：度量学习对嵌入几何和优化动态的影响缺乏深入理解。
- 方法要点：引入VARIANCE（类内/类间方差）和GREEDINESS（活跃比和梯度范数）框架，分析七种损失。
- 实验或效果：Triplet和SCL在细粒度检索中表现更优，而Contrastive和InfoNCE加速收敛但可能简化结构。

## 摘要（原文）

> Metric learning is central to retrieval, yet its effects on embedding geometry and optimization dynamics are not well understood. We introduce a diagnostic framework, VARIANCE (intra-/inter-class variance) and GREEDINESS (active ratio and gradient norms), to compare seven representative losses, i.e., Contrastive, Triplet, N-pair, InfoNCE, ArcFace, SCL, and CCL, across five image-retrieval datasets. Our analysis reveals that Triplet and SCL preserve higher within-class variance and clearer inter-class margins, leading to stronger top-1 retrieval in fine-grained settings. In contrast, Contrastive and InfoNCE compact embeddings are achieved quickly through many small updates, accelerating convergence but potentially oversimplifying class structures. N-pair achieves a large mean separation but with uneven spacing. These insights reveal a form of efficiency-granularity trade-off and provide practical guidance: prefer Triplet/SCL when diversity preservation and hard-sample discrimination are critical, and Contrastive/InfoNCE when faster embedding compaction is desired.

