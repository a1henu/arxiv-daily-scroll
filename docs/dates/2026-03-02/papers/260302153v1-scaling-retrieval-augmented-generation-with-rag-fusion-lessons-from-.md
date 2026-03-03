---
layout: default
title: Scaling Retrieval Augmented Generation with RAG Fusion: Lessons from an Industry Deployment
---

# Scaling Retrieval Augmented Generation with RAG Fusion: Lessons from an Industry Deployment
**arXiv**：[2603.02153v1](https://arxiv.org/abs/2603.02153) · [PDF](https://arxiv.org/pdf/2603.02153.pdf)  
**作者**：Luigi Medrano, Arush Verma, Mukul Chhabra  

**一句话要点**：评估检索融合在生产RAG系统中的实际效果，发现召回增益在重排序和截断后减弱。

**关键词**：检索增强生成, 检索融合, 生产部署, 召回率, 重排序, 系统效率

## 3 点简述
- 核心问题：检索融合在现实生产约束下是否提升RAG系统答案质量，而非仅提高召回率。
- 方法要点：在企业知识库上测试多查询检索和RRF等融合技术，考虑固定检索深度和延迟限制。
- 实验或效果：融合增加原始召回，但重排序后Top-k准确率未提升，Hit@10从0.51降至0.48，且引入额外延迟。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) systems commonly adopt retrieval fusion techniques such as multi-query retrieval and reciprocal rank fusion (RRF) to increase document recall, under the assumption that higher recall leads to better answer quality. While these methods show consistent gains in isolated retrieval benchmarks, their effectiveness under realistic production constraints remains underexplored. In this work, we evaluate retrieval fusion in a production-style RAG pipeline operating over an enterprise knowledge base, with fixed retrieval depth, re-ranking budgets, and latency constraints.
>   Across multiple fusion configurations, we find that retrieval fusion does increase raw recall, but these gains are largely neutralized after re-ranking and truncation. In our setting, fusion variants fail to outperform single-query baselines on KB-level Top-$k$ accuracy, with Hit@10 decreasing from $0.51$ to $0.48$ in several configurations. Moreover, fusion introduces additional latency overhead due to query rewriting and larger candidate sets, without corresponding improvements in downstream effectiveness.
>   Our analysis suggests that recall-oriented fusion techniques exhibit diminishing returns once realistic re-ranking limits and context budgets are applied. We conclude that retrieval-level improvements do not reliably translate into end-to-end gains in production RAG systems, and argue for evaluation frameworks that jointly consider retrieval quality, system efficiency, and downstream impact.

