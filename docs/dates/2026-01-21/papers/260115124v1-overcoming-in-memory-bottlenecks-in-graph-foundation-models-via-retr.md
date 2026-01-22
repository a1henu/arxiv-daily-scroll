---
layout: default
title: Overcoming In-Memory Bottlenecks in Graph Foundation Models via Retrieval-Augmented Generation
---

# Overcoming In-Memory Bottlenecks in Graph Foundation Models via Retrieval-Augmented Generation
**arXiv**：[2601.15124v1](https://arxiv.org/abs/2601.15124) · [PDF](https://arxiv.org/pdf/2601.15124.pdf)  
**作者**：Haonan Yuan, Qingyun Sun, Jiacheng Tao, Xingcheng Fu, Jianxin Li  

**一句话要点**：提出RAG-GFM以解决图基础模型中的内存瓶颈问题

**关键词**：图基础模型, 检索增强生成, 内存瓶颈, 双模态检索, 跨域分类

## 3 点简述
- 图基础模型受限于内存瓶颈，知识编码到参数中导致语义容量受限和压缩冲突
- 通过检索增强生成，构建双模态统一检索模块，外部化图知识并设计双视图对齐目标
- 在五个基准数据集上，RAG-GFM在跨域节点和图分类中优于13个基线，实现高效适应

## 摘要（原文）

> Graph Foundation Models (GFMs) have emerged as a frontier in graph learning, which are expected to deliver transferable representations across diverse tasks. However, GFMs remain constrained by in-memory bottlenecks: they attempt to encode knowledge into model parameters, which limits semantic capacity, introduces heavy lossy compression with conflicts, and entangles graph representation with the knowledge in ways that hinder efficient adaptation, undermining scalability and interpretability. In this work,we propose RAG-GFM, a Retrieval-Augmented Generation aided Graph Foundation Model that offloads knowledge from parameters and complements parameterized learning. To externalize graph knowledge, we build a dual-modal unified retrieval module, where a semantic store from prefix-structured text and a structural store from centrality-based motif. To preserve heterogeneous information, we design a dual-view alignment objective that contrasts both modalities to capture both content and relational patterns. To enable efficient downstream adaptation, we perform in-context augmentation to enrich supporting instances with retrieved texts and motifs as contextual evidence. Extensive experiments on five benchmark graph datasets demonstrate that RAG-GFM consistently outperforms 13 state-of-the-art baselines in both cross-domain node and graph classification, achieving superior effectiveness and efficiency.

