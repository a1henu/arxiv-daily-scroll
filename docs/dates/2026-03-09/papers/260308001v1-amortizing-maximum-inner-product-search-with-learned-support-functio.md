---
layout: default
title: Amortizing Maximum Inner Product Search with Learned Support Functions
---

# Amortizing Maximum Inner Product Search with Learned Support Functions
**arXiv**：[2603.08001v1](https://arxiv.org/abs/2603.08001) · [PDF](https://arxiv.org/pdf/2603.08001.pdf)  
**作者**：Theo X. Olausson, João Monteiro, Michal Klein, Marco Cuturi  

**一句话要点**：提出基于学习的摊销最大内积搜索方法，通过近似支持函数直接预测最优键向量。

**关键词**：最大内积搜索, 支持函数, 输入凸神经网络, 摊销计算, 查询分布, 数据库压缩

## 3 点简述
- 核心问题：最大内积搜索（MIPS）是机器学习中的关键子程序，需高效匹配查询与固定键集。
- 方法要点：利用支持函数的凸性和1-齐次性，训练神经网络直接预测MIPS解，包括SupportNet和KeyNet两种互补方法。
- 实验或效果：学习模型实现高匹配率，为基于查询分布压缩数据库开辟新方向。

## 摘要（原文）

> Maximum inner product search (MIPS) is a crucial subroutine in machine learning, requiring the identification of key vectors that align best with a given query. We propose amortized MIPS: a learning-based approach that trains neural networks to directly predict MIPS solutions, amortizing the computational cost of matching queries (drawn from a fixed distribution) to a fixed set of keys. Our key insight is that the MIPS value function, the maximal inner product between a query and keys, is also known as the support function of the set of keys. Support functions are convex, 1-homogeneous and their gradient w.r.t. the query is exactly the optimal key in the database. We approximate the support function using two complementary approaches: (1) we train an input-convex neural network (SupportNet) to model the support function directly; the optimal key can be recovered via (autodiff) gradient computation, and (2) we regress directly the optimal key from the query using a vector valued network (KeyNet), bypassing gradient computation entirely at inference time. To learn a SupportNet, we combine score regression with gradient matching losses, and propose homogenization wrappers that enforce the positive 1-homogeneity of a neural network, theoretically linking function values to gradients. To train a KeyNet, we introduce a score consistency loss derived from the Euler theorem for homogeneous functions. Our experiments show that learned SupportNet or KeyNet achieve high match rates and open up new directions to compress databases with a specific query distribution in mind.

