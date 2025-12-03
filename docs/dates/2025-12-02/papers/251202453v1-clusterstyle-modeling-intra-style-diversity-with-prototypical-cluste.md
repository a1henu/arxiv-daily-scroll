---
layout: default
title: ClusterStyle: Modeling Intra-Style Diversity with Prototypical Clustering for Stylized Motion Generation
---

# ClusterStyle: Modeling Intra-Style Diversity with Prototypical Clustering for Stylized Motion Generation
**arXiv**：[2512.02453v1](https://arxiv.org/abs/2512.02453) · [PDF](https://arxiv.org/pdf/2512.02453.pdf)  
**作者**：Kerui Chen, Jianrong Zhang, Ming Li, Zhonglong Zheng, Hehe Fan  

**一句话要点**：提出ClusterStyle框架，通过原型聚类建模风格内多样性，以提升风格化运动生成效果。

**关键词**：风格化运动生成, 原型聚类, 风格内多样性, 运动风格迁移, Stylistic Modulation Adapter

## 3 点简述
- 核心问题：现有模型难以捕捉风格内多样性，即同一风格对应多种运动变化。
- 方法要点：利用原型集建模全局和局部风格多样性，通过Stylistic Modulation Adapter集成风格特征。
- 实验或效果：在风格化运动生成和运动风格迁移任务中优于现有先进模型。

## 摘要（原文）

> Existing stylized motion generation models have shown their remarkable ability to understand specific style information from the style motion, and insert it into the content motion. However, capturing intra-style diversity, where a single style should correspond to diverse motion variations, remains a significant challenge. In this paper, we propose a clustering-based framework, ClusterStyle, to address this limitation. Instead of learning an unstructured embedding from each style motion, we leverage a set of prototypes to effectively model diverse style patterns across motions belonging to the same style category. We consider two types of style diversity: global-level diversity among style motions of the same category, and local-level diversity within the temporal dynamics of motion sequences. These components jointly shape two structured style embedding spaces, i.e., global and local, optimized via alignment with non-learnable prototype anchors. Furthermore, we augment the pretrained text-to-motion generation model with the Stylistic Modulation Adapter (SMA) to integrate the style features. Extensive experiments demonstrate that our approach outperforms existing state-of-the-art models in stylized motion generation and motion style transfer.

