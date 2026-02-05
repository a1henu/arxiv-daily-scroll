---
layout: default
title: The Key to State Reduction in Linear Attention: A Rank-based Perspective
---

# The Key to State Reduction in Linear Attention: A Rank-based Perspective
**arXiv**：[2602.04852v1](https://arxiv.org/abs/2602.04852) · [PDF](https://arxiv.org/pdf/2602.04852.pdf)  
**作者**：Philipp Nazari, T. Konstantin Rusch  

**一句话要点**：提出基于秩的结构化剪枝框架以减少线性注意力状态大小，提升计算与内存效率。

**关键词**：线性注意力, 状态剪枝, 结构化剪枝, 秩分析, 硬件优化, 模型压缩

## 3 点简述
- 线性注意力模型在实践中常呈现低秩状态，导致容量未充分利用并可能放大查询噪声。
- 通过理论分析，提出硬件感知的结构化剪枝方法，基于秩揭示QR分解减少键和查询矩阵。
- 实验表明，剪除50%通道仅轻微增加困惑度，在多种任务中验证了框架的有效性。

## 摘要（原文）

> Linear attention offers a computationally efficient yet expressive alternative to softmax attention. However, recent empirical results indicate that the state of trained linear attention models often exhibits a low-rank structure, suggesting that these models underexploit their capacity in practice. To illuminate this phenomenon, we provide a theoretical analysis of the role of rank in linear attention, revealing that low effective rank can affect retrieval error by amplifying query noise. In addition to these theoretical insights, we conjecture that the low-rank states can be substantially reduced post-training with only minimal performance degradation, yielding faster and more memory-efficient models. To this end, we propose a novel hardware-aware approach that structurally prunes key and query matrices, reducing the state size while retaining compatibility with existing CUDA kernels. We adapt several existing pruning strategies to fit our framework and, building on our theoretical analysis, propose a novel structured pruning method based on a rank-revealing QR decomposition. Our empirical results, evaluated across models of varying sizes and on various downstream tasks, demonstrate the effectiveness of our state reduction framework. We highlight that our framework enables the removal of 50% of the query and key channels at only a marginal increase in perplexity. The code for this project can be found at https://github.com/camail-official/LinearAttentionPruning.

