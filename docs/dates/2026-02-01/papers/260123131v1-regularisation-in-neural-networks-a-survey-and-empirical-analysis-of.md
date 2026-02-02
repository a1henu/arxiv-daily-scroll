---
layout: default
title: Regularisation in neural networks: a survey and empirical analysis of approaches
---

# Regularisation in neural networks: a survey and empirical analysis of approaches
**arXiv**：[2601.23131v1](https://arxiv.org/abs/2601.23131) · [PDF](https://arxiv.org/pdf/2601.23131.pdf)  
**作者**：Christiaan P. Opperman, Anna S. Bosman, Katherine M. Malan  

**一句话要点**：综述正则化技术并实证分析其效果，揭示数据集依赖性

**关键词**：正则化技术, 神经网络泛化, 实证分析, 数据集依赖性, 分类任务

## 3 点简述
- 核心问题：正则化技术是否总能提升神经网络泛化能力，实践假设需验证
- 方法要点：提出四类正则化分类法，包括数据、架构、训练和损失函数策略
- 实验或效果：在十个数值和图像数据集上实证，正则化效果因数据集而异

## 摘要（原文）

> Despite huge successes on a wide range of tasks, neural networks are known to sometimes struggle to generalise to unseen data. Many approaches have been proposed over the years to promote the generalisation ability of neural networks, collectively known as regularisation techniques. These are used as common practice under the assumption that any regularisation added to the pipeline would result in a performance improvement. In this study, we investigate whether this assumption holds in practice. First, we provide a broad review of regularisation techniques, including modern theories such as double descent. We propose a taxonomy of methods under four broad categories, namely: (1) data-based strategies, (2) architecture strategies, (3) training strategies, and (4) loss function strategies. Notably, we highlight the contradictions and correspondences between the approaches in these broad classes. Further, we perform an empirical comparison of the various regularisation techniques on classification tasks for ten numerical and image datasets applied to the multi-layer perceptron and convolutional neural network architectures. Results show that the efficacy of regularisation is dataset-dependent. For example, the use of a regularisation term only improved performance on numeric datasets, whereas batch normalisation improved performance on image datasets only. Generalisation is crucial to machine learning; thus, understanding the effects of applying regularisation techniques, and considering the connections between them is essential to the appropriate use of these methods in practice.

