---
layout: default
title: Masked Diffusion for Generative Recommendation
---

# Masked Diffusion for Generative Recommendation
**arXiv**：[2511.23021v1](https://arxiv.org/abs/2511.23021) · [PDF](https://arxiv.org/pdf/2511.23021.pdf)  
**作者**：Kulin Shah, Bhuvesh Kumar, Neil Shah, Liam Collins  

**一句话要点**：提出掩码扩散方法以改进生成式推荐中的语义ID序列建模

**关键词**：生成式推荐, 语义ID, 掩码扩散, 并行解码, 序列建模

## 3 点简述
- 现有基于语义ID的自回归生成式推荐存在推理成本高、数据利用效率低和短上下文偏置问题
- 采用掩码扩散模型，通过离散掩码噪声学习序列分布，实现条件独立并行解码
- 实验表明该方法在数据受限和粗粒度召回方面优于自回归模型，支持并行推理

## 摘要（原文）

> Generative recommendation (GR) with semantic IDs (SIDs) has emerged as a promising alternative to traditional recommendation approaches due to its performance gains, capitalization on semantic information provided through language model embeddings, and inference and storage efficiency. Existing GR with SIDs works frame the probability of a sequence of SIDs corresponding to a user's interaction history using autoregressive modeling. While this has led to impressive next item prediction performances in certain settings, these autoregressive GR with SIDs models suffer from expensive inference due to sequential token-wise decoding, potentially inefficient use of training data and bias towards learning short-context relationships among tokens. Inspired by recent breakthroughs in NLP, we propose to instead model and learn the probability of a user's sequence of SIDs using masked diffusion. Masked diffusion employs discrete masking noise to facilitate learning the sequence distribution, and models the probability of masked tokens as conditionally independent given the unmasked tokens, allowing for parallel decoding of the masked tokens. We demonstrate through thorough experiments that our proposed method consistently outperforms autoregressive modeling. This performance gap is especially pronounced in data-constrained settings and in terms of coarse-grained recall, consistent with our intuitions. Moreover, our approach allows the flexibility of predicting multiple SIDs in parallel during inference while maintaining superior performance to autoregressive modeling.

