---
layout: default
title: Simple Yet Effective Selective Imputation for Incomplete Multi-view Clustering
---

# Simple Yet Effective Selective Imputation for Incomplete Multi-view Clustering
**arXiv**：[2512.10327v1](https://arxiv.org/abs/2512.10327) · [PDF](https://arxiv.org/pdf/2512.10327.pdf)  
**作者**：Cai Xu, Jinlong Liu, Yilin Zhang, Ziyu Guan, Wei Zhao  

**一句话要点**：提出选择性插补方法以解决不完整多视图聚类中的噪声与偏差问题

**关键词**：不完整多视图聚类, 选择性插补, 变分自编码器, 高斯混合先验, 数据驱动方法, 插件模块

## 3 点简述
- 核心问题：不完整多视图数据中，盲目插补引入噪声，而免插补方法在严重不完整时缺乏跨视图互补性。
- 方法要点：基于信息量评估选择性插补，结合变分自编码器与高斯混合先验学习聚类友好表示。
- 实验或效果：在更现实的不平衡缺失场景下，优于基于插补和免插补方法，可作为插件模块集成。

## 摘要（原文）

> Incomplete multi-view data, where different views suffer from missing and unbalanced observations, pose significant challenges for clustering. Existing imputation-based methods attempt to estimate missing views to restore data associations, but indiscriminate imputation often introduces noise and bias, especially when the available information is insufficient. Imputation-free methods avoid this risk by relying solely on observed data, but struggle under severe incompleteness due to the lack of cross-view complementarity. To address this issue, we propose Informativeness-based Selective imputation Multi-View Clustering (ISMVC). Our method evaluates the imputation-relevant informativeness of each missing position based on intra-view similarity and cross-view consistency, and selectively imputes only when sufficient support is available. Furthermore, we integrate this selection with a variational autoencoder equipped with a mixture-of-Gaussians prior to learn clustering-friendly latent representations. By performing distribution-level imputation, ISMVC not only stabilizes the aggregation of posterior distributions but also explicitly models imputation uncertainty, enabling robust fusion and preventing overconfident reconstructions. Compared with existing cautious imputation strategies that depend on training dynamics or model feedback, our method is lightweight, data-driven, and model-agnostic. It can be readily integrated into existing IMC models as a plug-in module. Extensive experiments on multiple benchmark datasets under a more realistic and challenging unbalanced missing scenario demonstrate that our method outperforms both imputation-based and imputation-free approaches.

