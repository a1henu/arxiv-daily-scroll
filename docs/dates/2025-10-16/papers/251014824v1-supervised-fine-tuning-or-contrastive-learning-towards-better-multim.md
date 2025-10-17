---
layout: default
title: Supervised Fine-Tuning or Contrastive Learning? Towards Better Multimodal LLM Reranking
---

# Supervised Fine-Tuning or Contrastive Learning? Towards Better Multimodal LLM Reranking
**arXiv**：[2510.14824v1](https://arxiv.org/abs/2510.14824) · [PDF](https://arxiv.org/pdf/2510.14824.pdf)  
**作者**：Ziqi Dai, Xin Zhang, Mingxin Li, Yanzhao Zhang, Dingkun Long, Pengjun Xie, Meishan Zhang, Wenjie Li, Min Zhang  

**一句话要点**：比较监督微调与对比学习在LLM重排序中的效果，发现SFT更优。

**关键词**：LLM重排序, 监督微调, 对比学习, 多模态检索, 权重分析

## 3 点简述
- 核心问题：LLM重排序中，监督微调与对比学习哪种目标更有效？
- 方法要点：分解目标为权重和方向，提出统一分析框架。
- 实验效果：SFT权重更强，在MRB基准上达到新SOTA。

## 摘要（原文）

> In information retrieval, training reranking models mainly focuses on two
> types of objectives: metric learning (e.g. contrastive loss to increase the
> predicted scores on relevant query-document pairs) and classification (binary
> label prediction of relevance vs. irrelevance). For BERT-style encoders,
> various studies have shown that contrastive learning (CL) can be more effective
> than discriminative (classification) learning. However, for large language
> models (LLMs), classification via supervised fine-tuning (SFT), which predicts
> ''yes'' (resp. ''no'') token for relevant (resp. irrelevant) pairs, appears
> more promising as it aligns well with the generative nature of LLMs. This
> divergence raises a central question: which objective is intrinsically better
> suited to LLM-based reranking, and what mechanism underlies the difference? In
> this work, we conduct a comprehensive comparison and analysis between CL and
> SFT for reranking, taking the universal multimodal retrieval (UMR) as the
> experimental playground. We first decompose the objectives into two components:
> weight, which controls the magnitude of those updates, and direction, which
> guides the model updates, then present a unified framework for understanding
> their interactions. Through probing experiments, we find that SFT provides a
> substantially stronger weighting scheme than CL, whereas the preferred scoring
> direction shows no clear winner. Taken together, these results point to a
> consistent advantage of SFT over CL for LLM reranking. To further validate our
> findings, we conduct large-scale training with SFT and present new
> state-of-the-art rerankers on the MRB benchmark. We also provide ablations on
> SFT settings and expect our findings to benefit future research and
> applications in this area.

