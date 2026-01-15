---
layout: default
title: ReGraM: Region-First Knowledge Graph Reasoning for Medical Question Answering
---

# ReGraM: Region-First Knowledge Graph Reasoning for Medical Question Answering
**arXiv**：[2601.09280v1](https://arxiv.org/abs/2601.09280) · [PDF](https://arxiv.org/pdf/2601.09280.pdf)  
**作者**：Chaerin Lee, Sohee Park, Hyunsik Na, Daseon Choi  

**一句话要点**：提出ReGraM框架，通过区域优先知识图谱推理提升医疗问答的事实准确性

**关键词**：医疗问答, 知识图谱推理, 区域优先推理, 多跳推理, 事实准确性

## 3 点简述
- 核心问题：现有医疗问答方法依赖全图谱遍历或大规模检索，导致噪声多、多跳推理不稳定
- 方法要点：构建查询对齐子图，在局部区域内进行多证据感知的逐步推理
- 实验或效果：在七个基准测试中优于基线，准确率提升最高8.04%，幻觉率降低42.9%

## 摘要（原文）

> Recent studies in medical question answering (Medical QA) have actively explored the integration of large language models (LLMs) with biomedical knowledge graphs (KGs) to improve factual accuracy. However, most existing approaches still rely on traversing the entire KG or performing large-scale retrieval, which introduces substantial noise and leads to unstable multi-hop reasoning. We argue that the core challenge lies not in expanding access to knowledge, but in identifying and reasoning over the appropriate subset of evidence for each query. ReGraM is a region-first knowledge graph reasoning framework that addresses this challenge by constructing a query-aligned subgraph and performing stepwise reasoning constrained to this localized region under multiple evidence aware modes. By focusing inference on only the most relevant portion of the KG, ReGraM departs from the assumption that all relations are equally useful an assumption that rarely holds in domain-specific medical settings. Experiments on seven medical QA benchmarks demonstrate that ReGraM consistently outperforms a strong baseline (KGARevion), achieving an 8.04% absolute accuracy gain on MCQ, a 4.50% gain on SAQ, and a 42.9% reduction in hallucination rate. Ablation and qualitative analyses further show that aligning region construction with hop-wise reasoning is the primary driver of these improvements. Overall, our results highlight region-first KG reasoning as an effective paradigm for improving factual accuracy and consistency in medical QA.

