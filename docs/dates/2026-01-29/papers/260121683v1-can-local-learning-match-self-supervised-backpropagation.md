---
layout: default
title: Can Local Learning Match Self-Supervised Backpropagation?
---

# Can Local Learning Match Self-Supervised Backpropagation?
**arXiv**：[2601.21683v1](https://arxiv.org/abs/2601.21683) · [PDF](https://arxiv.org/pdf/2601.21683.pdf)  
**作者**：Wu S. Zihan, Ariane Delrocq, Wulfram Gerstner, Guillaume Bellec  

**一句话要点**：提出局部自监督学习算法变体，以在深度非线性网络中近似全局反向传播自监督学习

**关键词**：局部自监督学习, 反向传播自监督学习, 深度神经网络, 梯度更新匹配, 图像数据集基准

## 3 点简述
- 核心问题：局部自监督学习在深度网络中难以构建有效表示，与全局反向传播自监督学习存在差距
- 方法要点：基于深度线性网络理论，开发局部自监督算法变体以匹配全局更新，并应用于非线性卷积网络
- 实验或效果：在CIFAR-10等数据集上，改进梯度相似性的变体性能提升，最佳变体匹配全局算法性能

## 摘要（原文）

> While end-to-end self-supervised learning with backpropagation (global BP-SSL) has become central for training modern AI systems, theories of local self-supervised learning (local-SSL) have struggled to build functional representations in deep neural networks. To establish a link between global and local rules, we first develop a theory for deep linear networks: we identify conditions for local-SSL algorithms (like Forward-forward or CLAPP) to implement exactly the same weight update as a global BP-SSL. Starting from the theoretical insights, we then develop novel variants of local-SSL algorithms to approximate global BP-SSL in deep non-linear convolutional neural networks. Variants that improve the similarity between gradient updates of local-SSL with those of global BP-SSL also show better performance on image datasets (CIFAR-10, STL-10, and Tiny ImageNet). The best local-SSL rule with the CLAPP loss function matches the performance of a comparable global BP-SSL with InfoNCE or CPC-like loss functions, and improves upon state-of-the-art for local SSL on these benchmarks.

