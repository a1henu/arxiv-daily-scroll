---
layout: default
title: RANKVIDEO: Reasoning Reranking for Text-to-Video Retrieval
---

# RANKVIDEO: Reasoning Reranking for Text-to-Video Retrieval
**arXiv**：[2602.02444v1](https://arxiv.org/abs/2602.02444) · [PDF](https://arxiv.org/pdf/2602.02444.pdf)  
**作者**：Tyler Skow, Alexander Martin, Benjamin Van Durme, Rama Chellappa, Reno Kriz  

**一句话要点**：提出RANKVIDEO推理重排序方法以提升文本到视频检索性能

**关键词**：文本到视频检索, 推理重排序, 两阶段训练, 数据合成, 多目标优化, 检索性能提升

## 3 点简述
- 核心问题：视频检索中基于推理的重排序方法研究不足，影响检索精度。
- 方法要点：采用两阶段课程训练，结合感知监督微调和多目标重排序训练，并利用数据合成构建推理密集型查询-视频对。
- 实验或效果：在MultiVENT 2.0基准测试中，平均提升nDCG@10达31%，优于纯文本和视觉语言重排序方法，且效率更高。

## 摘要（原文）

> Reranking is a critical component of modern retrieval systems, which typically pair an efficient first-stage retriever with a more expressive model to refine results. While large reasoning models have driven rapid progress in text-centric reranking, reasoning-based reranking for video retrieval remains underexplored. To address this gap, we introduce RANKVIDEO, a reasoning-based reranker for video retrieval that explicitly reasons over query-video pairs using video content to assess relevance. RANKVIDEO is trained using a two-stage curriculum consisting of perception-grounded supervised fine-tuning followed by reranking training that combines pointwise, pairwise, and teacher confidence distillation objectives, and is supported by a data synthesis pipeline for constructing reasoning-intensive query-video pairs. Experiments on the large-scale MultiVENT 2.0 benchmark demonstrate that RANKVIDEO consistently improves retrieval performance within a two-stage framework, yielding an average improvement of 31% on nDCG@10 and outperforming text-only and vision-language reranking alternatives, while more efficient.

