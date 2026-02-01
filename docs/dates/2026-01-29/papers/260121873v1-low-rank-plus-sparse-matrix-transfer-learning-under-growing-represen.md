---
layout: default
title: Low-Rank Plus Sparse Matrix Transfer Learning under Growing Representations and Ambient Dimensions
---

# Low-Rank Plus Sparse Matrix Transfer Learning under Growing Representations and Ambient Dimensions
**arXiv**：[2601.21873v1](https://arxiv.org/abs/2601.21873) · [PDF](https://arxiv.org/pdf/2601.21873.pdf)  
**作者**：Jinhang Chai, Xuyuan Liu, Elynn Chen, Yujun Yan  

**一句话要点**：提出基于低秩加稀疏矩阵分解的迁移学习框架，以处理表示和维度增长下的结构化矩阵估计问题。

**关键词**：迁移学习, 低秩矩阵, 稀疏矩阵, 表示增长, 维度增长, 结构化估计

## 3 点简述
- 研究表示和维度同时增长时的迁移学习，目标参数分解为嵌入源组件、低秩创新和稀疏编辑。
- 提出锚定交替投影估计器，保留迁移子空间，仅估计低维创新和稀疏修改，并建立确定性误差界。
- 应用于马尔可夫转移矩阵和结构化协方差估计，理论分析和实验验证了迁移增益。

## 摘要（原文）

> Learning systems often expand their ambient features or latent representations over time, embedding earlier representations into larger spaces with limited new latent structure. We study transfer learning for structured matrix estimation under simultaneous growth of the ambient dimension and the intrinsic representation, where a well-estimated source task is embedded as a subspace of a higher-dimensional target task.
>   We propose a general transfer framework in which the target parameter decomposes into an embedded source component, low-dimensional low-rank innovations, and sparse edits, and develop an anchored alternating projection estimator that preserves transferred subspaces while estimating only low-dimensional innovations and sparse modifications. We establish deterministic error bounds that separate target noise, representation growth, and source estimation error, yielding strictly improved rates when rank and sparsity increments are small.
>   We demonstrate the generality of the framework by applying it to two canonical problems. For Markov transition matrix estimation from a single trajectory, we derive end-to-end theoretical guarantees under dependent noise. For structured covariance estimation under enlarged dimensions, we provide complementary theoretical analysis in the appendix and empirically validate consistent transfer gains.

