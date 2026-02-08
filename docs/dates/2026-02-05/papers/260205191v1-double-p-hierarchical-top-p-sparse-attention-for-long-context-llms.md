---
layout: default
title: Double-P: Hierarchical Top-P Sparse Attention for Long-Context LLMs
---

# Double-P: Hierarchical Top-P Sparse Attention for Long-Context LLMs
**arXiv**：[2602.05191v1](https://arxiv.org/abs/2602.05191) · [PDF](https://arxiv.org/pdf/2602.05191.pdf)  
**作者**：Wentao Ni, Kangqi Zhang, Zhongming Yu, Oren Nelson, Mingu Lee, Hong Cai, Fatih Porikli, Jongryool Kim, Zhijian Liu, Jishen Zhao  

**一句话要点**：提出Double-P分层稀疏注意力框架，以优化长上下文LLM的推理效率。

**关键词**：长上下文推理, 稀疏注意力, 分层优化, top-p选择, LLM效率, 解码加速

## 3 点简述
- 核心问题：长上下文推理中，注意力计算成为瓶颈，现有稀疏方法无法平衡准确性、选择开销和计算成本。
- 方法要点：采用分层策略，先基于聚类进行粗粒度top-p估计，再自适应细化token级注意力计算。
- 实验或效果：在长上下文基准测试中，实现近零精度损失，计算开销降低1.8倍，端到端解码加速1.3倍。

## 摘要（原文）

> As long-context inference becomes central to large language models (LLMs), attention over growing key-value caches emerges as a dominant decoding bottleneck, motivating sparse attention for scalable inference. Fixed-budget top-k sparse attention cannot adapt to heterogeneous attention distributions across heads and layers, whereas top-p sparse attention directly preserves attention mass and provides stronger accuracy guarantees. Existing top-p methods, however, fail to jointly optimize top-p accuracy, selection overhead, and sparse attention cost, which limits their overall efficiency. We present Double-P, a hierarchical sparse attention framework that optimizes all three stages. Double-P first performs coarse-grained top-p estimation at the cluster level using size-weighted centroids, then adaptively refines computation through a second top-p stage that allocates token-level attention only when needed. Across long-context benchmarks, Double-P consistently achieves near-zero accuracy drop, reducing attention computation overhead by up to 1.8x and delivers up to 1.3x end-to-end decoding speedup over state-of-the-art fixed-budget sparse attention methods.

