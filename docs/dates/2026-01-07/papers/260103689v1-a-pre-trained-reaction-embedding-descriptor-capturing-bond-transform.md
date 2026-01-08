---
layout: default
title: A Pre-trained Reaction Embedding Descriptor Capturing Bond Transformation Patterns
---

# A Pre-trained Reaction Embedding Descriptor Capturing Bond Transformation Patterns
**arXiv**：[2601.03689v1](https://arxiv.org/abs/2601.03689) · [PDF](https://arxiv.org/pdf/2601.03689.pdf)  
**作者**：Weiqi Liu, Fenglei Cao, Yuan Qi, Li-Cheng Xu  

**一句话要点**：提出RXNEmb反应级描述符，基于预训练模型捕获键变换模式，用于反应指纹与分析。

**关键词**：反应描述符, 预训练模型, 键变换模式, 反应指纹, 数据驱动分析

## 3 点简述
- 核心问题：数据驱动反应预测模型缺乏通用反应级描述符，难以桥接化学与数字表示。
- 方法要点：从RXNGraphormer模型衍生RXNEmb，通过预训练区分真实与虚构反应，学习键形成与断裂模式。
- 实验或效果：在USPTO-50k数据集上重新聚类，可视化反应空间多样性，注意力分析提供机理洞察。

## 摘要（原文）

> With the rise of data-driven reaction prediction models, effective reaction descriptors are crucial for bridging the gap between real-world chemistry and digital representations. However, general-purpose, reaction-wise descriptors remain scarce. This study introduces RXNEmb, a novel reaction-level descriptor derived from RXNGraphormer, a model pre-trained to distinguish real reactions from fictitious ones with erroneous bond changes, thereby learning intrinsic bond formation and cleavage patterns. We demonstrate its utility by data-driven re-clustering of the USPTO-50k dataset, yielding a classification that more directly reflects bond-change similarities than rule-based categories. Combined with dimensionality reduction, RXNEmb enables visualization of reaction space diversity. Furthermore, attention weight analysis reveals the model's focus on chemically critical sites, providing mechanistic insight. RXNEmb serves as a powerful, interpretable tool for reaction fingerprinting and analysis, paving the way for more data-centric approaches in reaction analysis and discovery.

