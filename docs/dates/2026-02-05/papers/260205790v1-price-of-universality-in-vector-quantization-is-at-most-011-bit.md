---
layout: default
title: Price of universality in vector quantization is at most 0.11 bit
---

# Price of universality in vector quantization is at most 0.11 bit
**arXiv**：[2602.05790v1](https://arxiv.org/abs/2602.05790) · [PDF](https://arxiv.org/pdf/2602.05790.pdf)  
**作者**：Alina Harbuzova, Or Ordentlich, Yury Polyanskiy  

**一句话要点**：证明存在通用码本，在向量量化中比最优自适应码本最多损失0.11比特/维

**关键词**：向量量化, 权重量化, 通用码本, 信息论, 低精度计算, 大语言模型

## 3 点简述
- 研究大语言模型权重量化中，码本依赖输入统计不实用的问题
- 证明存在通用码本，对所有输入统计均接近最优，损失≤0.11比特/维
- 存在性证明非构造性，但为低精度存储格式提供理论依据

## 摘要（原文）

> Fast computation of a matrix product $W^\top X$ is a workhorse of modern LLMs. To make their deployment more efficient, a popular approach is that of using a low-precision approximation $\widehat W$ in place of true $W$ ("weight-only quantization''). Information theory demonstrates that an optimal algorithm for reducing precision of $W$ depends on the (second order) statistics of $X$ and requires a careful alignment of vector quantization codebook with PCA directions of $X$ (a process known as "waterfilling allocation''). Dependence of the codebook on statistics of $X$, however, is highly impractical. This paper proves that there exist a universal codebook that is simultaneously near-optimal for all possible statistics of $X$, in the sense of being at least as good as an $X$-adapted waterfilling codebook with rate reduced by 0.11 bit per dimension. Such universal codebook would be an ideal candidate for the low-precision storage format, a topic of active modern research, but alas the existence proof is non-constructive.
>   Equivalently, our result shows existence of a net in $\mathbb{R}^n$ that is a nearly-optimal covering of a sphere simultaneously with respect to all Hilbert norms.

