---
layout: default
title: Winning the Lottery by Preserving Network Training Dynamics with Concrete Ticket Search
---

# Winning the Lottery by Preserving Network Training Dynamics with Concrete Ticket Search
**arXiv**：[2512.07142v1](https://arxiv.org/abs/2512.07142) · [PDF](https://arxiv.org/pdf/2512.07142.pdf)  
**作者**：Tanay Arora, Christof Teuscher  

**一句话要点**：提出Concrete Ticket Search算法，通过整体优化解决初始化剪枝的性能差距问题。

**关键词**：彩票票假设, 初始化剪枝, 组合优化, 知识蒸馏, 稀疏网络, 训练动态

## 3 点简述
- 核心问题：初始化剪枝方法依赖一阶显著性指标，忽略权重间依赖，导致精度-稀疏度权衡不佳。
- 方法要点：使用Concrete松弛和梯度平衡方案，将子网络发现建模为组合优化问题，无需敏感超参数调优。
- 实验或效果：在图像分类任务中，CTS生成子网络通过健全性检查，精度接近或超过LTR，计算成本大幅降低。

## 摘要（原文）

> The Lottery Ticket Hypothesis asserts the existence of highly sparse, trainable subnetworks ('winning tickets') within dense, randomly initialized neural networks. However, state-of-the-art methods of drawing these tickets, like Lottery Ticket Rewinding (LTR), are computationally prohibitive, while more efficient saliency-based Pruning-at-Initialization (PaI) techniques suffer from a significant accuracy-sparsity trade-off and fail basic sanity checks. In this work, we argue that PaI's reliance on first-order saliency metrics, which ignore inter-weight dependencies, contributes substantially to this performance gap, especially in the sparse regime. To address this, we introduce Concrete Ticket Search (CTS), an algorithm that frames subnetwork discovery as a holistic combinatorial optimization problem. By leveraging a Concrete relaxation of the discrete search space and a novel gradient balancing scheme (GRADBALANCE) to control sparsity, CTS efficiently identifies high-performing subnetworks near initialization without requiring sensitive hyperparameter tuning. Motivated by recent works on lottery ticket training dynamics, we further propose a knowledge distillation-inspired family of pruning objectives, finding that minimizing the reverse Kullback-Leibler divergence between sparse and dense network outputs (CTS-KL) is particularly effective. Experiments on varying image classification tasks show that CTS produces subnetworks that robustly pass sanity checks and achieve accuracy comparable to or exceeding LTR, while requiring only a small fraction of the computation. For example, on ResNet-20 on CIFAR10, it reaches 99.3% sparsity with 74.0% accuracy in 7.9 minutes, while LTR attains the same sparsity with 68.3% accuracy in 95.2 minutes. CTS's subnetworks outperform saliency-based methods across all sparsities, but its advantage over LTR is most pronounced in the highly sparse regime.

