---
layout: default
title: Revisiting Incremental Stochastic Majorization-Minimization Algorithms with Applications to Mixture of Experts
---

# Revisiting Incremental Stochastic Majorization-Minimization Algorithms with Applications to Mixture of Experts
**arXiv**：[2601.19811v1](https://arxiv.org/abs/2601.19811) · [PDF](https://arxiv.org/pdf/2601.19811.pdf)  
**作者**：TrungKhang Tran, TrungTin Nguyen, Gersende Fort, Tung Doan, Hien Duy Nguyen, Binh T. Nguyen, Florence Forbes, Christopher Drovandi  

**一句话要点**：提出增量随机主化最小化算法，用于流数据下的专家混合模型优化

**关键词**：增量随机优化, 主化最小化算法, 专家混合模型, 流数据处理, 收敛性分析

## 3 点简述
- 针对流数据场景，传统批量算法需重复遍历全数据集而效率低下
- 提出增量随机MM算法，放宽EM算法限制，理论证明收敛到平稳点
- 在软max门控专家混合回归中优于主流随机优化器，并在真实生物信息数据验证

## 摘要（原文）

> Processing high-volume, streaming data is increasingly common in modern statistics and machine learning, where batch-mode algorithms are often impractical because they require repeated passes over the full dataset. This has motivated incremental stochastic estimation methods, including the incremental stochastic Expectation-Maximization (EM) algorithm formulated via stochastic approximation. In this work, we revisit and analyze an incremental stochastic variant of the Majorization-Minimization (MM) algorithm, which generalizes incremental stochastic EM as a special case. Our approach relaxes key EM requirements, such as explicit latent-variable representations, enabling broader applicability and greater algorithmic flexibility. We establish theoretical guarantees for the incremental stochastic MM algorithm, proving consistency in the sense that the iterates converge to a stationary point characterized by a vanishing gradient of the objective. We demonstrate these advantages on a softmax-gated mixture of experts (MoE) regression problem, for which no stochastic EM algorithm is available. Empirically, our method consistently outperforms widely used stochastic optimizers, including stochastic gradient descent, root mean square propagation, adaptive moment estimation, and second-order clipped stochastic optimization. These results support the development of new incremental stochastic algorithms, given the central role of softmax-gated MoE architectures in contemporary deep neural networks for heterogeneous data modeling. Beyond synthetic experiments, we also validate practical effectiveness on two real-world datasets, including a bioinformatics study of dent maize genotypes under drought stress that integrates high-dimensional proteomics with ecophysiological traits, where incremental stochastic MM yields stable gains in predictive performance.

