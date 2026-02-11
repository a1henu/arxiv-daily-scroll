---
layout: default
title: Computationally Efficient Replicable Learning of Parities
---

# Computationally Efficient Replicable Learning of Parities
**arXiv**：[2602.09499v1](https://arxiv.org/abs/2602.09499) · [PDF](https://arxiv.org/pdf/2602.09499.pdf)  
**作者**：Moshe Noivirt, Jessica Sorrell, Eliad Tsfadia  

**一句话要点**：提出高效可复制算法，实现任意分布下奇偶函数的可复制学习

**关键词**：可复制学习, 差分隐私, 统计查询模型, 奇偶函数学习, 高效算法, 机器学习理论

## 3 点简述
- 研究可复制学习与差分隐私、统计查询模型的计算关系，填补高效算法空白
- 设计高效可复制算法，基于向量集输出覆盖多数向量的线性子空间作为核心构建块
- 首次在任意分布下高效可复制学习奇偶函数，超越统计查询模型能力，接近差分隐私学习

## 摘要（原文）

> We study the computational relationship between replicability (Impagliazzo et al. [STOC `22], Ghazi et al. [NeurIPS `21]) and other stability notions. Specifically, we focus on replicable PAC learning and its connections to differential privacy (Dwork et al. [TCC 2006]) and to the statistical query (SQ) model (Kearns [JACM `98]). Statistically, it was known that differentially private learning and replicable learning are equivalent and strictly more powerful than SQ-learning. Yet, computationally, all previously known efficient (i.e., polynomial-time) replicable learning algorithms were confined to SQ-learnable tasks or restricted distributions, in contrast to differentially private learning.
>   Our main contribution is the first computationally efficient replicable algorithm for realizable learning of parities over arbitrary distributions, a task that is known to be hard in the SQ-model, but possible under differential privacy. This result provides the first evidence that efficient replicable learning over general distributions strictly extends efficient SQ-learning, and is closer in power to efficient differentially private learning, despite computational separations between replicability and privacy. Our main building block is a new, efficient, and replicable algorithm that, given a set of vectors, outputs a subspace of their linear span that covers most of them.

