---
layout: default
title: LoRIF: Low-Rank Influence Functions for Scalable Training Data Attribution
---

# LoRIF: Low-Rank Influence Functions for Scalable Training Data Attribution
**arXiv**：[2601.21929v1](https://arxiv.org/abs/2601.21929) · [PDF](https://arxiv.org/pdf/2601.21929.pdf)  
**作者**：Shuangqi Li, Hieu Le, Jingyi Xu, Mathieu Salzmann  

**一句话要点**：提出LoRIF以解决大规模训练数据归因中的存储与计算瓶颈问题

**关键词**：训练数据归因, 低秩近似, 梯度计算, 可扩展性, Hessian近似, 存储优化

## 3 点简述
- 核心问题：梯度计算导致存储和I/O瓶颈，影响训练数据归因的可扩展性。
- 方法要点：利用梯度低秩结构，存储低秩因子并近似Hessian项，降低存储和内存需求。
- 实验或效果：在0.1B至70B参数模型上，相比LoGRA实现高达20倍存储减少和查询加速，归因质量相当或更优。

## 摘要（原文）

> Training data attribution (TDA) identifies which training examples most influenced a model's prediction. The best-performing TDA methods exploits gradients to define an influence function. To overcome the scalability challenge arising from gradient computation, the most popular strategy is random projection (e.g., TRAK, LoGRA). However, this still faces two bottlenecks when scaling to large training sets and high-quality attribution: \emph{(i)} storing and loading projected per-example gradients for all $N$ training examples, where query latency is dominated by I/O; and \emph{(ii)} forming the $D \times D$ inverse Hessian approximation, which costs $O(D^2)$ memory. Both bottlenecks scale with the projection dimension $D$, yet increasing $D$ is necessary for attribution quality -- creating a quality-scalability tradeoff. We introduce \textbf{LoRIF (Low-Rank Influence Functions)}, which exploits low-rank structures of gradient to address both bottlenecks. First, we store rank-$c$ factors of the projected per-example gradients rather than full matrices, reducing storage and query-time I/O from $O(D)$ to $O(c\sqrt{D})$ per layer per sample. Second, we use truncated SVD with the Woodbury identity to approximate the Hessian term in an $r$-dimensional subspace, reducing memory from $O(D^2)$ to $O(Dr)$. On models from 0.1B to 70B parameters trained on datasets with millions of examples, LoRIF achieves up to 20$\times$ storage reduction and query-time speedup compared to LoGRA, while matching or exceeding its attribution quality. LoRIF makes gradient-based TDA practical at frontier scale.

