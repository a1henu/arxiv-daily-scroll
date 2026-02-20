---
layout: default
title: Bonsai: A Framework for Convolutional Neural Network Acceleration Using Criterion-Based Pruning
---

# Bonsai: A Framework for Convolutional Neural Network Acceleration Using Criterion-Based Pruning
**arXiv**：[2602.17145v1](https://arxiv.org/abs/2602.17145) · [PDF](https://arxiv.org/pdf/2602.17145.pdf)  
**作者**：Joseph Bingham, Sam Helmich  

**一句话要点**：提出Bonsai框架，基于准则的剪枝加速卷积神经网络，解决剪枝方法实现与比较困难问题。

**关键词**：卷积神经网络剪枝, 准则剪枝框架, 模型加速, 滤波器剪枝, 计算优化

## 3 点简述
- 核心问题：CNN规模增大导致计算和内存开销上升，现有剪枝方法缺乏统一实现和比较标准。
- 方法要点：开发Bonsai框架，支持基于准则的迭代剪枝，并引入标准语言比较不同剪枝准则。
- 实验或效果：在VGG类模型上剪枝达79%滤波器，保持或提升精度，计算量减少高达68%。

## 摘要（原文）

> As the need for more accurate and powerful Convolutional Neural Networks (CNNs) increases, so too does the size, execution time, memory footprint, and power consumption. To overcome this, solutions such as pruning have been proposed with their own metrics and methodologies, or criteria, for how weights should be removed. These solutions do not share a common implementation and are difficult to implement and compare. In this work, we introduce Combine, a criterion- based pruning solution and demonstrate that it is fast and effective framework for iterative pruning, demonstrate that criterion have differing effects on different models, create a standard language for comparing criterion functions, and propose a few novel criterion functions. We show the capacity of these criterion functions and the framework on VGG inspired models, pruning up to 79\% of filters while retaining or improving accuracy, and reducing the computations needed by the network by up to 68\%.

