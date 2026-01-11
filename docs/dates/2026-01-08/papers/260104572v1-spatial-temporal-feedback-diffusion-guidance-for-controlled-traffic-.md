---
layout: default
title: Spatial-Temporal Feedback Diffusion Guidance for Controlled Traffic Imputation
---

# Spatial-Temporal Feedback Diffusion Guidance for Controlled Traffic Imputation
**arXiv**：[2601.04572v1](https://arxiv.org/abs/2601.04572) · [PDF](https://arxiv.org/pdf/2601.04572.pdf)  
**作者**：Xiaowei Mao, Huihu Ding, Yan Lin, Tingrui Wu, Shengnan Guo, Dazhuo Qiu, Feiling Fang, Jilin Hu, Huaiyu Wan  

**一句话要点**：提出FENCE方法以解决交通数据缺失值插补中扩散模型引导不足的问题

**关键词**：交通数据插补, 扩散模型, 空间-时间引导, 自适应控制, 缺失值处理

## 3 点简述
- 核心问题：现有扩散模型在空间-时间维度上使用统一引导尺度，对高缺失率节点引导不足，导致插补性能下降。
- 方法要点：FENCE引入动态反馈机制，基于后验似然近似自适应调整引导尺度，并通过聚类节点提供更精确的引导。
- 实验或效果：在真实交通数据集上，FENCE显著提升了插补准确性。

## 摘要（原文）

> Imputing missing values in spatial-temporal traffic data is essential for intelligent transportation systems. Among advanced imputation methods, score-based diffusion models have demonstrated competitive performance. These models generate data by reversing a noising process, using observed values as conditional guidance. However, existing diffusion models typically apply a uniform guidance scale across both spatial and temporal dimensions, which is inadequate for nodes with high missing data rates. Sparse observations provide insufficient conditional guidance, causing the generative process to drift toward the learned prior distribution rather than closely following the conditional observations, resulting in suboptimal imputation performance.
>   To address this, we propose FENCE, a spatial-temporal feedback diffusion guidance method designed to adaptively control guidance scales during imputation. First, FENCE introduces a dynamic feedback mechanism that adjusts the guidance scale based on the posterior likelihood approximations. The guidance scale is increased when generated values diverge from observations and reduced when alignment improves, preventing overcorrection. Second, because alignment to observations varies across nodes and denoising steps, a global guidance scale for all nodes is suboptimal. FENCE computes guidance scales at the cluster level by grouping nodes based on their attention scores, leveraging spatial-temporal correlations to provide more accurate guidance. Experimental results on real-world traffic datasets show that FENCE significantly enhances imputation accuracy.

