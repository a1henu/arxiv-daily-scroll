---
layout: default
title: Enhancing Vision-Language Navigation with Multimodal Event Knowledge from Real-World Indoor Tour Videos
---

# Enhancing Vision-Language Navigation with Multimodal Event Knowledge from Real-World Indoor Tour Videos
**arXiv**：[2602.23937v1](https://arxiv.org/abs/2602.23937) · [PDF](https://arxiv.org/pdf/2602.23937.pdf)  
**作者**：Haoxuan Xu, Tianfu Li, Wenbo Chen, Yi Liu, Xingxing Zuo, Yaoxian Song, Haoang Li  

**一句话要点**：提出基于多模态事件知识的增强策略，以解决视觉语言导航中的粗粒度指令和长时程推理问题。

**关键词**：视觉语言导航, 多模态事件知识, 知识图谱构建, 长时程推理, 粗粒度指令处理

## 3 点简述
- 核心问题：视觉语言导航在未见环境中处理模糊粗粒度指令和长时程推理时表现不佳。
- 方法要点：构建大规模多模态时空知识图谱YE-KG，并设计STE-VLN模型通过粗到细层次检索机制融合事件知识。
- 实验或效果：在REVERIE、R2R和R2R-CE基准测试中超越现有方法，验证了策略的有效性。

## 摘要（原文）

> Vision-Language Navigation (VLN) agents often struggle with long-horizon reasoning in unseen environments, particularly when facing ambiguous, coarse-grained instructions. While recent advances use knowledge graph to enhance reasoning, the potential of multimodal event knowledge inspired by human episodic memory remains underexplored. In this work, we propose an event-centric knowledge enhancement strategy for automated process knowledge mining and feature fusion to solve coarse-grained instruction and long-horizon reasoning in VLN task. First, we construct YE-KG, the first large-scale multimodal spatiotemporal knowledge graph, with over 86k nodes and 83k edges, derived from real-world indoor videos. By leveraging multimodal large language models (i.e., LLaVa, GPT4), we extract unstructured video streams into structured semantic-action-effect events to serve as explicit episodic memory. Second, we introduce STE-VLN, which integrates the above graph into VLN models via a Coarse-to-Fine Hierarchical Retrieval mechanism. This allows agents to retrieve causal event sequences and dynamically fuse them with egocentric visual observations. Experiments on REVERIE, R2R, and R2R-CE benchmarks demonstrate the efficiency of our event-centric strategy, outperforming state-of-the-art approaches across diverse action spaces. Our data and code are available on the project website https://sites.google.com/view/y-event-kg/.

