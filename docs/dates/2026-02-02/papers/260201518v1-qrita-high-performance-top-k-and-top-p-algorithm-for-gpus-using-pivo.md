---
layout: default
title: Qrita: High-performance Top-k and Top-p Algorithm for GPUs using Pivot-based Truncation and Selection
---

# Qrita: High-performance Top-k and Top-p Algorithm for GPUs using Pivot-based Truncation and Selection
**arXiv**：[2602.01518v1](https://arxiv.org/abs/2602.01518) · [PDF](https://arxiv.org/pdf/2602.01518.pdf)  
**作者**：Jongseok Park, Sunga Kim, Alvin Cheung, Ion Stoica  

**一句话要点**：提出Qrita算法，基于枢轴选择策略高效实现大语言模型中的Top-k和Top-p截断操作。

**关键词**：Top-k算法, Top-p算法, GPU优化, 枢轴选择, 大语言模型采样, Triton实现

## 3 点简述
- 核心问题：现有Top-k和Top-p实现依赖排序或随机方法，在GPU上计算和内存开销大或输出不确定。
- 方法要点：采用高斯sigma截断减少搜索空间，结合四元枢轴搜索处理重复项，确保确定性输出。
- 实验或效果：在vLLM等引擎上评估，Qrita实现最高2倍吞吐量、一半内存使用，输出与排序算法相同。

## 摘要（原文）

> Top-k and Top-p are the dominant truncation operators in the sampling of large language models. Despite their widespread use, implementing them efficiently over large vocabularies remains a significant challenge. Existing approaches often rely on sorting, which incur significant computation and memory overhead on GPUs, or stochastic approaches, which alter the algorithm output. In this work, we propose Qrita, an efficient Top-k and Top-p algorithm based on a pivot-based selection strategy. Based on RTop-k, which uses a pivot-based search for node selection in graph neural networks, Qrita extends the concept of pivot-based search to both Top-k and Top-p with two key techniques: 1. Gaussian-based sigma-truncation, which greatly reduces the search space of the target elements, and 2. Quaternary pivot search with duplication handling, which halves the pivot search iteration and guarantees deterministic output. We provide the full implementation of Qrita using Triton, a popular GPU programming language. Our evaluation of Qrita against the Top-k and Top-p kernels of high performance LLM execution engines such as vLLM, SGLang, and Flashinfer show that Qrita achieves up to 2 times throughput and half memory use while providing the same output to the the sorting-based algorithms.

