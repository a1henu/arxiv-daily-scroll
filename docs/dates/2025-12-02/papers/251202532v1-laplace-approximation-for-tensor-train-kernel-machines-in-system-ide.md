---
layout: default
title: Laplace Approximation For Tensor Train Kernel Machines In System Identification
---

# Laplace Approximation For Tensor Train Kernel Machines In System Identification
**arXiv**：[2512.02532v1](https://arxiv.org/abs/2512.02532) · [PDF](https://arxiv.org/pdf/2512.02532.pdf)  
**作者**：Albert Saiapin, Kim Batselier  

**一句话要点**：提出贝叶斯张量列车核机器，结合拉普拉斯近似与变分推理，用于系统识别中的可扩展高斯过程回归。

**关键词**：张量列车核机器, 拉普拉斯近似, 变分推理, 系统识别, 高斯过程回归, 贝叶斯建模

## 3 点简述
- 核心问题：张量列车模型在贝叶斯扩展中，不确定哪个核心应进行贝叶斯处理。
- 方法要点：对选定张量列车核心应用拉普拉斯近似估计后验分布，并用变分推理处理精度超参数。
- 实验或效果：核心选择与张量列车秩和特征结构无关，变分推理替代交叉验证，训练速度提升高达65倍。

## 摘要（原文）

> To address the scalability limitations of Gaussian process (GP) regression, several approximation techniques have been proposed. One such method is based on tensor networks, which utilizes an exponential number of basis functions without incurring exponential computational cost. However, extending this model to a fully probabilistic formulation introduces several design challenges. In particular, for tensor train (TT) models, it is unclear which TT-core should be treated in a Bayesian manner. We introduce a Bayesian tensor train kernel machine that applies Laplace approximation to estimate the posterior distribution over a selected TT-core and employs variational inference (VI) for precision hyperparameters. Experiments show that core selection is largely independent of TT-ranks and feature structure, and that VI replaces cross-validation while offering up to 65x faster training. The method's effectiveness is demonstrated on an inverse dynamics problem.

