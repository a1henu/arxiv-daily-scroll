---
layout: default
title: SLA2: Sparse-Linear Attention with Learnable Routing and QAT
---

# SLA2: Sparse-Linear Attention with Learnable Routing and QAT
**arXiv**：[2602.12675v1](https://arxiv.org/abs/2602.12675) · [PDF](https://arxiv.org/pdf/2602.12675.pdf)  
**作者**：Jintao Zhang, Haoxu Wang, Kai Jiang, Kaiwen Zheng, Youhe Jiang, Ion Stoica, Jianfei Chen, Jun Zhu, Joseph E. Gonzalez  

**一句话要点**：提出SLA2以改进扩散模型中的稀疏-线性注意力，通过可学习路由和量化感知微调提升效率与质量。

**关键词**：稀疏-线性注意力, 可学习路由, 量化感知微调, 视频扩散模型, 注意力加速

## 3 点简述
- SLA依赖启发式分割，基于注意力权重大小分配计算，可能非最优。
- SLA2引入可学习路由器动态选择稀疏或线性注意力，并使用可学习比率更直接结合分支。
- 实验显示在视频扩散模型中，SLA2实现97%注意力稀疏度，加速18.6倍且保持生成质量。

## 摘要（原文）

> Sparse-Linear Attention (SLA) combines sparse and linear attention to accelerate diffusion models and has shown strong performance in video generation. However, (i) SLA relies on a heuristic split that assigns computations to the sparse or linear branch based on attention-weight magnitude, which can be suboptimal. Additionally, (ii) after formally analyzing the attention error in SLA, we identify a mismatch between SLA and a direct decomposition into sparse and linear attention. We propose SLA2, which introduces (I) a learnable router that dynamically selects whether each attention computation should use sparse or linear attention, (II) a more faithful and direct sparse-linear attention formulation that uses a learnable ratio to combine the sparse and linear attention branches, and (III) a sparse + low-bit attention design, where low-bit attention is introduced via quantization-aware fine-tuning to reduce quantization error. Experiments show that on video diffusion models, SLA2 can achieve 97% attention sparsity and deliver an 18.6x attention speedup while preserving generation quality.

