---
layout: default
title: Learnable Permutation for Structured Sparsity on Transformer Models
---

# Learnable Permutation for Structured Sparsity on Transformer Models
**arXiv**：[2601.22980v1](https://arxiv.org/abs/2601.22980) · [PDF](https://arxiv.org/pdf/2601.22980.pdf)  
**作者**：Zekai Li, Ji Liu, Guanchen Li, Yixing Xu, Ziqiong Liu, Xuanwu Yin, Dong Li, Emad Barsoum  

**一句话要点**：提出可学习置换框架以优化Transformer模型的结构化稀疏性

**关键词**：结构化稀疏, 权重置换, Transformer模型, 可学习优化, 模型剪枝, 二分匹配

## 3 点简述
- 核心问题：Transformer模型权重置换搜索空间指数增长，现有方法依赖贪心或启发式算法，限制稀疏化效果。
- 方法要点：引入可学习置换成本矩阵、可微分二分匹配求解器和稀疏优化损失函数，实现端到端学习。
- 实验或效果：在视觉和语言Transformer上验证，达到结构化稀疏性的最先进置换结果。

## 摘要（原文）

> Structured sparsity has emerged as a popular model pruning technique, widely adopted in various architectures, including CNNs, Transformer models, and especially large language models (LLMs) in recent years. A promising direction to further improve post-pruning performance is weight permutation, which reorders model weights into patterns more amenable to pruning. However, the exponential growth of the permutation search space with the scale of Transformer architectures forces most methods to rely on greedy or heuristic algorithms, limiting the effectiveness of reordering.
>   In this work, we propose a novel end-to-end learnable permutation framework. Our method introduces a learnable permutation cost matrix to quantify the cost of swapping any two input channels of a given weight matrix, a differentiable bipartite matching solver to obtain the optimal binary permutation matrix given a cost matrix, and a sparsity optimization loss function to directly optimize the permutation operator. We extensively validate our approach on vision and language Transformers, demonstrating that our method achieves state-of-the-art permutation results for structured sparsity.

