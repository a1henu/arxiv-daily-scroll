---
layout: default
title: Group and Exclusive Sparse Regularization-based Continual Learning of CNNs
---

# Group and Exclusive Sparse Regularization-based Continual Learning of CNNs
**arXiv**：[2601.03658v1](https://arxiv.org/abs/2601.03658) · [PDF](https://arxiv.org/pdf/2601.03658.pdf)  
**作者**：Basile Tousside, Janis Mohr, Jörg Frochte  

**一句话要点**：提出基于组稀疏与排他稀疏正则化的持续学习方法，以解决卷积神经网络在顺序学习多任务时的灾难性遗忘问题。

**关键词**：持续学习, 卷积神经网络, 灾难性遗忘, 稀疏正则化, 稳定性与可塑性, 视觉基准测试

## 3 点简述
- 核心问题：固定容量卷积神经网络在顺序学习多任务时易发生灾难性遗忘，需平衡稳定性和可塑性。
- 方法要点：通过稳定性正则项保护对过去任务重要的滤波器，利用可塑性正则项稀疏化网络并调整不重要滤波器以适应新任务。
- 实验或效果：在持续学习视觉基准测试中，整体分类准确率优于现有方法，有效避免灾难性遗忘，减少参数和计算量。

## 摘要（原文）

> We present a regularization-based approach for continual learning (CL) of fixed capacity convolutional neural networks (CNN) that does not suffer from the problem of catastrophic forgetting when learning multiple tasks sequentially. This method referred to as Group and Exclusive Sparsity based Continual Learning (GESCL) avoids forgetting of previous tasks by ensuring the stability of the CNN via a stability regularization term, which prevents filters detected as important for past tasks to deviate too much when learning a new task. On top of that, GESCL makes the network plastic via a plasticity regularization term that leverage the over-parameterization of CNNs to efficiently sparsify the network and tunes unimportant filters making them relevant for future tasks. Doing so, GESCL deals with significantly less parameters and computation compared to CL approaches that either dynamically expand the network or memorize past tasks' data. Experiments on popular CL vision benchmarks show that GESCL leads to significant improvements over state-of-the-art method in terms of overall CL performance, as measured by classification accuracy as well as in terms of avoiding catastrophic forgetting.

