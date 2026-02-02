---
layout: default
title: Understanding Generalization from Embedding Dimension and Distributional Convergence
---

# Understanding Generalization from Embedding Dimension and Distributional Convergence
**arXiv**：[2601.22756v1](https://arxiv.org/abs/2601.22756) · [PDF](https://arxiv.org/pdf/2601.22756.pdf)  
**作者**：Junjie Yu, Zhuoli Ouyang, Haotian Deng, Chen Wei, Wenxiao Ma, Jianyu Zhang, Zihan Deng, Quanying Liu  

**一句话要点**：提出基于嵌入维度与分布收敛的泛化理论，从表示视角解释过参数化网络的泛化性能。

**关键词**：泛化理论, 嵌入维度, 分布收敛, 表示学习, Wasserstein距离, Lipschitz常数

## 3 点简述
- 核心问题：过参数化深度网络泛化性能与参数数量无关，需新理论解释。
- 方法要点：通过嵌入分布内在维度和下游映射敏感性，推导嵌入依赖的泛化误差界。
- 实验或效果：跨架构和数据集验证理论，嵌入维度与泛化性能强相关。

## 摘要（原文）

> Deep neural networks often generalize well despite heavy over-parameterization, challenging classical parameter-based analyses. We study generalization from a representation-centric perspective and analyze how the geometry of learned embeddings controls predictive performance for a fixed trained model. We show that population risk can be bounded by two factors: (i) the intrinsic dimension of the embedding distribution, which determines the convergence rate of empirical embedding distribution to the population distribution in Wasserstein distance, and (ii) the sensitivity of the downstream mapping from embeddings to predictions, characterized by Lipschitz constants. Together, these yield an embedding-dependent error bound that does not rely on parameter counts or hypothesis class complexity. At the final embedding layer, architectural sensitivity vanishes and the bound is dominated by embedding dimension, explaining its strong empirical correlation with generalization performance. Experiments across architectures and datasets validate the theory and demonstrate the utility of embedding-based diagnostics.

