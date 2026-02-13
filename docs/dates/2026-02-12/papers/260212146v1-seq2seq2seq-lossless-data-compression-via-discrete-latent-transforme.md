---
layout: default
title: Seq2Seq2Seq: Lossless Data Compression via Discrete Latent Transformers and Reinforcement Learning
---

# Seq2Seq2Seq: Lossless Data Compression via Discrete Latent Transformers and Reinforcement Learning
**arXiv**：[2602.12146v1](https://arxiv.org/abs/2602.12146) · [PDF](https://arxiv.org/pdf/2602.12146.pdf)  
**作者**：Mahdi Khodabandeh, Ghazal Shabani, Arash Yousefi Jordehi, Seyed Abolghasem Mirroshandel  

**一句话要点**：提出基于强化学习和T5架构的无损压缩方法，以提升复杂数据的压缩效率。

**关键词**：无损压缩, 强化学习, T5模型, 令牌序列, 压缩比优化

## 3 点简述
- 传统压缩方法难以有效利用复杂数据的结构和冗余，导致压缩效率受限。
- 采用强化学习优化T5模型，将数据压缩为令牌序列而非向量表示，保留原始结构。
- 实验显示压缩比显著优于传统方法，无需外部知识，适用于多种应用场景。

## 摘要（原文）

> Efficient lossless compression is essential for minimizing storage costs and transmission overhead while preserving data integrity. Traditional compression techniques, such as dictionary-based and statistical methods, often struggle to optimally exploit the structure and redundancy in complex data formats. Recent advancements in deep learning have opened new avenues for compression; however, many existing approaches depend on dense vector representations that obscure the underlying token structure. To address these limitations, we propose a novel lossless compression method that leverages Reinforcement Learning applied to a T5 language model architecture. This approach enables the compression of data into sequences of tokens rather than traditional vector representations. Unlike auto-encoders, which typically encode information into continuous latent spaces, our method preserves the token-based structure, aligning more closely with the original data format. This preservation allows for higher compression ratios while maintaining semantic integrity. By training the model using an off-policy Reinforcement Learning algorithm, we optimize sequence length to minimize redundancy and enhance compression efficiency. Our method introduces an efficient and adaptive data compression system built upon advanced Reinforcement Learning techniques, functioning independently of external grammatical or world knowledge. This approach shows significant improvements in compression ratios compared to conventional methods. By leveraging the latent information within language models, our system effectively compresses data without requiring explicit content understanding, paving the way for more robust and practical compression solutions across various applications.

