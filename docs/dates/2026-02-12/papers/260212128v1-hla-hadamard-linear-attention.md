---
layout: default
title: HLA: Hadamard Linear Attention
---

# HLA: Hadamard Linear Attention
**arXiv**：[2602.12128v1](https://arxiv.org/abs/2602.12128) · [PDF](https://arxiv.org/pdf/2602.12128.pdf)  
**作者**：Hanno Ackermann, Hong Cai, Mohsen Ghafoorian, Amirhossein Habibian  

**一句话要点**：提出Hadamard线性注意力以高效近似软注意力，应用于大规模视频生成扩散变换器。

**关键词**：线性注意力, 软注意力近似, 扩散变换器, 视频生成, 计算效率

## 3 点简述
- 核心问题：标准注意力计算成本高，线性注意力近似软注意力但为低阶有理函数。
- 方法要点：HLA在计算成对相似度后应用非线性，实现高阶有理函数近似，无需耗时张量重塑。
- 实验或效果：应用于大规模视频生成扩散变换器，处理大量令牌，验证有效性。

## 摘要（原文）

> The attention mechanism is an important reason for the success of transformers. It relies on computing pairwise relations between tokens. To reduce the high computational cost of standard quadratic attention, linear attention has been proposed as an efficient approximation. It employs kernel functions that are applied independently to the inputs before the pairwise similarities are calculated. That allows for an efficient computational procedure which, however, amounts to a low-degree rational function approximating softmax.
>   We propose Hadamard Linear Attention (HLA). Unlike previous works on linear attention, the nonlinearity in HLA is not applied separately to queries and keys, but, analogously to standard softmax attention, after the pairwise similarities have been computed. It will be shown that the proposed nonlinearity amounts to a higher-degree rational function to approximate softmax. An efficient computational scheme for the proposed method is derived that is similar to that of standard linear attention. In contrast to other approaches, no time-consuming tensor reshaping is necessary to apply the proposed algorithm. The effectiveness of the approach is demonstrated by applying it to a large diffusion transformer model for video generation, an application that involves very large amounts of tokens.

