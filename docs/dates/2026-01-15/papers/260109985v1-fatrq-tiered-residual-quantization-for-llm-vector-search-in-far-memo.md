---
layout: default
title: FaTRQ: Tiered Residual Quantization for LLM Vector Search in Far-Memory-Aware ANNS Systems
---

# FaTRQ: Tiered Residual Quantization for LLM Vector Search in Far-Memory-Aware ANNS Systems
**arXiv**：[2601.09985v1](https://arxiv.org/abs/2601.09985) · [PDF](https://arxiv.org/pdf/2601.09985.pdf)  
**作者**：Tianqi Zhang, Flavio Ponzina, Tajana Rosing  

**一句话要点**：提出FaTRQ系统，通过分层残差量化消除远内存读取，加速近似最近邻搜索

**关键词**：近似最近邻搜索, 分层残差量化, 远内存感知, 检索增强生成, 向量量化, CXL加速器

## 3 点简述
- 现代ANNS系统依赖从慢存储读取全精度向量进行二次精炼，导致查询延迟主导
- FaTRQ采用分层残差量化，将残差编码为三元值存储在远内存，通过渐进距离估计器进行本地精炼
- 实验显示存储效率提升2.4倍，吞吐量最高提升9倍，优于现有GPU ANNS系统

## 摘要（原文）

> Approximate Nearest-Neighbor Search (ANNS) is a key technique in retrieval-augmented generation (RAG), enabling rapid identification of the most relevant high-dimensional embeddings from massive vector databases. Modern ANNS engines accelerate this process using prebuilt indexes and store compressed vector-quantized representations in fast memory. However, they still rely on a costly second-pass refinement stage that reads full-precision vectors from slower storage like SSDs. For modern text and multimodal embeddings, these reads now dominate the latency of the entire query. We propose FaTRQ, a far-memory-aware refinement system using tiered memory that eliminates the need to fetch full vectors from storage. It introduces a progressive distance estimator that refines coarse scores using compact residuals streamed from far memory. Refinement stops early once a candidate is provably outside the top-k. To support this, we propose tiered residual quantization, which encodes residuals as ternary values stored efficiently in far memory. A custom accelerator is deployed in a CXL Type-2 device to perform low-latency refinement locally. Together, FaTRQ improves the storage efficiency by 2.4$\times$ and improves the throughput by up to 9$ \times$ than SOTA GPU ANNS system.

