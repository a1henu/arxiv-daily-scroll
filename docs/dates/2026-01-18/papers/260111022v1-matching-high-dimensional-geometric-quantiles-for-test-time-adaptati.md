---
layout: default
title: Matching High-Dimensional Geometric Quantiles for Test-Time Adaptation of Transformers and Convolutional Networks Alike
---

# Matching High-Dimensional Geometric Quantiles for Test-Time Adaptation of Transformers and Convolutional Networks Alike
**arXiv**：[2601.11022v1](https://arxiv.org/abs/2601.11022) · [PDF](https://arxiv.org/pdf/2601.11022.pdf)  
**作者**：Sravan Danda, Aditya Challa, Shlok Mehendale, Snehanshu Saha  

**一句话要点**：提出基于高维几何分位数匹配的测试时适配方法，以解决分布偏移问题，适用于多种网络架构。

**关键词**：测试时适配, 分布偏移, 分位数匹配, 架构无关, 适配器网络, 图像分类

## 3 点简述
- 核心问题：测试数据分布与训练数据分布存在轻微偏移，现有测试时适配方法依赖特定架构，通用性不足。
- 方法要点：通过添加适配器网络预处理输入图像，使用分位数损失匹配高维几何分位数，实现架构无关的分布校正。
- 实验或效果：在CIFAR10-C、CIFAR100-C和TinyImageNet-C数据集上验证，适用于卷积和Transformer网络。

## 摘要（原文）

> Test-time adaptation (TTA) refers to adapting a classifier for the test data when the probability distribution of the test data slightly differs from that of the training data of the model. To the best of our knowledge, most of the existing TTA approaches modify the weights of the classifier relying heavily on the architecture. It is unclear as to how these approaches are extendable to generic architectures. In this article, we propose an architecture-agnostic approach to TTA by adding an adapter network pre-processing the input images suitable to the classifier. This adapter is trained using the proposed quantile loss. Unlike existing approaches, we correct for the distribution shift by matching high-dimensional geometric quantiles. We prove theoretically that under suitable conditions minimizing quantile loss can learn the optimal adapter. We validate our approach on CIFAR10-C, CIFAR100-C and TinyImageNet-C by training both classic convolutional and transformer networks on CIFAR10, CIFAR100 and TinyImageNet datasets.

