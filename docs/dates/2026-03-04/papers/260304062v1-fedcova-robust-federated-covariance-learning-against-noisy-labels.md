---
layout: default
title: FedCova: Robust Federated Covariance Learning Against Noisy Labels
---

# FedCova: Robust Federated Covariance Learning Against Noisy Labels
**arXiv**：[2603.04062v1](https://arxiv.org/abs/2603.04062) · [PDF](https://arxiv.org/pdf/2603.04062.pdf)  
**作者**：Xiangyu Zhong, Xiaojun Yuan, Ying-Jun Angela Zhang  

**一句话要点**：提出FedCova框架，通过联邦协方差学习增强模型内在鲁棒性以应对噪声标签问题。

**关键词**：联邦学习, 噪声标签, 协方差学习, 特征编码, 鲁棒性增强, 子空间分类

## 3 点简述
- 核心问题：分布式数据中的噪声标签导致联邦学习模型过拟合和性能下降。
- 方法要点：基于互信息最大化设计损失特征编码目标，利用特征协方差构建子空间增强分类器。
- 实验或效果：在CIFAR-10/100和Clothing1M数据集上验证了优于现有方法的鲁棒性。

## 摘要（原文）

> Noisy labels in distributed datasets induce severe local overfitting and consequently compromise the global model in federated learning (FL). Most existing solutions rely on selecting clean devices or aligning with public clean datasets, rather than endowing the model itself with robustness. In this paper, we propose FedCova, a dependency-free federated covariance learning framework that eliminates such external reliances by enhancing the model's intrinsic robustness via a new perspective on feature covariances. Specifically, FedCova encodes data into a discriminative but resilient feature space to tolerate label noise. Built on mutual information maximization, we design a novel objective for federated lossy feature encoding that relies solely on class feature covariances with an error tolerance term. Leveraging feature subspaces characterized by covariances, we construct a subspace-augmented federated classifier. FedCova unifies three key processes through the covariance: (1) training the network for feature encoding, (2) constructing a classifier directly from the learned features, and (3) correcting noisy labels based on feature subspaces. We implement FedCova across both symmetric and asymmetric noisy settings under heterogeneous data distribution. Experimental results on CIFAR-10/100 and real-world noisy dataset Clothing1M demonstrate the superior robustness of FedCova compared with the state-of-the-art methods.

