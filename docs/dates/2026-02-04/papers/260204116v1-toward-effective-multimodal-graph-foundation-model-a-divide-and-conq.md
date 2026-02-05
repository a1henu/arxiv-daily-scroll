---
layout: default
title: Toward Effective Multimodal Graph Foundation Model: A Divide-and-Conquer Based Approach
---

# Toward Effective Multimodal Graph Foundation Model: A Divide-and-Conquer Based Approach
**arXiv**：[2602.04116v1](https://arxiv.org/abs/2602.04116) · [PDF](https://arxiv.org/pdf/2602.04116.pdf)  
**作者**：Sicheng Liu, Xunkai Li, Daohan Su, Ru Zhang, Hongchao Qin, Ronghua Li, Guoren Wang  

**一句话要点**：提出PLANET框架以解决多模态图基础模型中模态交互与对齐不足的问题

**关键词**：多模态图基础模型, 模态交互, 模态对齐, 分治策略, 图拓扑感知

## 3 点简述
- 核心问题：现有MGFMs未能显式建模模态交互，且模态对齐效果不佳，限制跨模态语义捕获
- 方法要点：采用分治策略，在嵌入粒度通过EDG实现局部模态交互，在节点粒度通过NDR实现全局模态对齐
- 实验或效果：在多种图中心和多模态生成任务上显著优于现有基线方法

## 摘要（原文）

> Graph Foundation Models (GFMs) have achieved remarkable success in generalizing across diverse domains. However, they mainly focus on Text-Attributed Graphs (TAGs), leaving Multimodal-Attributed Graphs (MAGs) largely untapped. Developing Multimodal Graph Foundation Models (MGFMs) allows for leveraging the rich multimodal information in MAGs, and extends applicability to broader types of downstream tasks. While recent MGFMs integrate diverse modality information, our empirical investigation reveals two fundamental limitations of existing MGFMs: (1)they fail to explicitly model modality interaction, essential for capturing intricate cross-modal semantics beyond simple aggregation, and (2)they exhibit sub-optimal modality alignment, which is critical for bridging the significant semantic disparity between distinct modal spaces. To address these challenges, we propose PLANET (graPh topoLogy-aware modAlity iNteraction and alignmEnT), a novel framework employing a Divide-and-Conquer strategy to decouple modality interaction and alignment across distinct granularities. At the embedding granularity, (1)Embedding-wise Domain Gating (EDG) performs local semantic enrichment by adaptively infusing topology-aware cross-modal context, achieving modality interaction. At the node granularity, (2)Node-wise Discretization Retrieval (NDR) ensures global modality alignment by constructing a Discretized Semantic Representation Space (DSRS) to bridge modality gaps. Extensive experiments demonstrate that PLANET significantly outperforms state-of-the-art baselines across diverse graph-centric and multimodal generative tasks.

