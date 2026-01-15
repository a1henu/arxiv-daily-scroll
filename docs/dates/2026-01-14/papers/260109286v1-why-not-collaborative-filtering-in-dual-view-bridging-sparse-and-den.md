---
layout: default
title: Why not Collaborative Filtering in Dual View? Bridging Sparse and Dense Models
---

# Why not Collaborative Filtering in Dual View? Bridging Sparse and Dense Models
**arXiv**：[2601.09286v1](https://arxiv.org/abs/2601.09286) · [PDF](https://arxiv.org/pdf/2601.09286.pdf)  
**作者**：Hanze Guo, Jianxun Lian, Xiao Zhou  

**一句话要点**：提出SaD框架以解决推荐系统中稀疏数据下稠密模型信号噪声比受限的问题

**关键词**：协同过滤, 稀疏稠密模型, 信号噪声比, 双向对齐, 推荐系统, 矩阵分解

## 3 点简述
- 核心问题：稠密嵌入模型在处理冷门物品时因数据稀疏导致信号噪声比存在理论上限
- 方法要点：通过双向对齐机制整合稠密嵌入的语义表达与稀疏交互模式的结构可靠性
- 实验或效果：在真实基准测试中实现最先进性能，并可在现有推荐模型中即插即用

## 摘要（原文）

> Collaborative Filtering (CF) remains the cornerstone of modern recommender systems, with dense embedding--based methods dominating current practice. However, these approaches suffer from a critical limitation: our theoretical analysis reveals a fundamental signal-to-noise ratio (SNR) ceiling when modeling unpopular items, where parameter-based dense models experience diminishing SNR under severe data sparsity. To overcome this bottleneck, we propose SaD (Sparse and Dense), a unified framework that integrates the semantic expressiveness of dense embeddings with the structural reliability of sparse interaction patterns. We theoretically show that aligning these dual views yields a strictly superior global SNR. Concretely, SaD introduces a lightweight bidirectional alignment mechanism: the dense view enriches the sparse view by injecting semantic correlations, while the sparse view regularizes the dense model through explicit structural signals. Extensive experiments demonstrate that, under this dual-view alignment, even a simple matrix factorization--style dense model can achieve state-of-the-art performance. Moreover, SaD is plug-and-play and can be seamlessly applied to a wide range of existing recommender models, highlighting the enduring power of collaborative filtering when leveraged from dual perspectives. Further evaluations on real-world benchmarks show that SaD consistently outperforms strong baselines, ranking first on the BarsMatch leaderboard. The code is publicly available at https://github.com/harris26-G/SaD.

