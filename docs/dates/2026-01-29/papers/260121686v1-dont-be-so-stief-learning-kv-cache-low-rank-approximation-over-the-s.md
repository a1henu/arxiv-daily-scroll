---
layout: default
title: Don't be so Stief! Learning KV Cache low-rank approximation over the Stiefel manifold
---

# Don't be so Stief! Learning KV Cache low-rank approximation over the Stiefel manifold
**arXiv**：[2601.21686v1](https://arxiv.org/abs/2601.21686) · [PDF](https://arxiv.org/pdf/2601.21686.pdf)  
**作者**：Luca Benfenati, Matteo Risso, Andrea Vannozzi, Ahmet Caner Yüzügüler, Lukas Cavigelli, Enrico Macii, Daniele Jahier Pagliari, Alessio Burrello  

**一句话要点**：提出StiefAttention方法，通过Stiefel流形学习正交投影基以优化KV缓存压缩，解决长上下文下HBM瓶颈问题。

**关键词**：KV缓存压缩, Stiefel流形优化, 后训练压缩, 长上下文处理, 正交投影学习, 解码层输出重建

## 3 点简述
- KV缓存在长上下文下成为HBM容量和带宽的主要瓶颈，现有后训练压缩方法使用SVD代理目标可能无法准确反映端到端重建误差。
- StiefAttention直接最小化解码层输出重建误差，学习正交投影基，并预计算误差-秩配置文件，支持基于误差预算的灵活层间秩分配。
- 在Llama3-8B上，相同压缩条件下，StiefAttention在C4困惑度和0-shot MMLU准确率上优于EigenAttention，实现更低的相对误差和更高的余弦相似度。

## 摘要（原文）

> Key--value (KV) caching enables fast autoregressive decoding but at long contexts becomes a dominant bottleneck in High Bandwidth Memory (HBM) capacity and bandwidth. A common mitigation is to compress cached keys and values by projecting per-head matrixes to a lower rank, storing only the projections in the HBM. However, existing post-training approaches typically fit these projections using SVD-style proxy objectives, which may poorly reflect end-to-end reconstruction after softmax, value mixing, and subsequent decoder-layer transformations.
>   For these reasons, we introduce StiefAttention, a post-training KV-cache compression method that learns \emph{orthonormal} projection bases by directly minimizing \emph{decoder-layer output reconstruction error}. StiefAttention additionally precomputes, for each layer, an error-rank profile over candidate ranks, enabling flexible layer-wise rank allocation under a user-specified error budget. Noteworthy, on Llama3-8B under the same conditions, StiefAttention outperforms EigenAttention by $11.9$ points on C4 perplexity and $5.4\%$ on 0-shot MMLU accuracy at iso-compression, yielding lower relative error and higher cosine similarity with respect to the original decoder-layer outputs.

