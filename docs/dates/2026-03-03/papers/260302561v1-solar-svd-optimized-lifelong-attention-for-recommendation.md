---
layout: default
title: SOLAR: SVD-Optimized Lifelong Attention for Recommendation
---

# SOLAR: SVD-Optimized Lifelong Attention for Recommendation
**arXiv**：[2603.02561v1](https://arxiv.org/abs/2603.02561) · [PDF](https://arxiv.org/pdf/2603.02561.pdf)  
**作者**：Chenghao Zhang, Chao Feng, Yuanhao Pu, Xunyong Yang, Wenhui Yu, Xiang Li, Yongqi Liu, Lantao Hu, Kaiqiao Zhan, Han Li, Kun Gai  

**一句话要点**：提出SOLAR框架，利用SVD-Attention降低注意力复杂度，支持推荐系统中大规模序列建模。

**关键词**：推荐系统, 注意力机制, 低秩矩阵, 序列建模, SVD优化

## 3 点简述
- 核心问题：传统注意力机制在长序列建模中计算复杂度高，导致推荐系统需截断或启发式处理。
- 方法要点：引入SVD-Attention，基于低秩矩阵结构，理论无损地降低复杂度并保留softmax机制。
- 实验或效果：在快手在线推荐场景中，SOLAR实现0.68%视频观看量提升及其他业务指标改进。

## 摘要（原文）

> Attention mechanism remains the defining operator in Transformers since it provides expressive global credit assignment, yet its $O(N^2 d)$ time and memory cost in sequence length $N$ makes long-context modeling expensive and often forces truncation or other heuristics. Linear attention reduces complexity to $O(N d^2)$ by reordering computation through kernel feature maps, but this reformulation drops the softmax mechanism and shifts the attention score distribution. In recommender systems, low-rank structure in matrices is not a rare case, but rather the default inductive bias in its representation learning, particularly explicit in the user behavior sequence modeling. Leveraging this structure, we introduce SVD-Attention, which is theoretically lossless on low-rank matrices and preserves softmax while reducing attention complexity from $O(N^2 d)$ to $O(Ndr)$. With SVD-Attention, we propose SOLAR, SVD-Optimized Lifelong Attention for Recommendation, a sequence modeling framework that supports behavior sequences of ten-thousand scale and candidate sets of several thousand items in cascading process without any filtering. In Kuaishou's online recommendation scenario, SOLAR delivers a 0.68\% Video Views gain together with additional business metrics improvements.

