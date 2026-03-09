---
layout: default
title: Omni-Masked Gradient Descent: Memory-Efficient Optimization via Mask Traversal with Improved Convergence
---

# Omni-Masked Gradient Descent: Memory-Efficient Optimization via Mask Traversal with Improved Convergence
**arXiv**：[2603.05960v1](https://arxiv.org/abs/2603.05960) · [PDF](https://arxiv.org/pdf/2603.05960.pdf)  
**作者**：Hui Yang, Tao Ren, Jinyang Jiang, Wan Tian, Yijie Peng  

**一句话要点**：提出Omni-Masked梯度下降以解决GPU内存瓶颈下大模型训练的内存效率问题

**关键词**：内存高效优化, 梯度下降, 非凸收敛分析, 大语言模型训练, 掩码遍历

## 3 点简述
- 核心问题：现有内存高效优化方法缺乏收敛保证或仅达标准迭代复杂度
- 方法要点：基于掩码遍历的优化方法，理论分析改进迭代复杂度至~O(ε^{-3})
- 实验或效果：轻量级即插即用，在微调和预训练任务中优于基线

## 摘要（原文）

> Memory-efficient optimization methods have recently gained increasing attention for scaling full-parameter training of large language models under the GPU-memory bottleneck. Existing approaches either lack clear convergence guarantees, or only achieve the standard ${\mathcal{O}}(ε^{-4})$ iteration complexity in the nonconvex settings. We propose Omni-Masked Gradient Descent (OMGD), an optimization method based on mask traversal for memory efficient training, and provide a nonconvex convergence analysis that establishes a strictly improved iteration complexity of $\tilde{\mathcal{O}}(ε^{-3})$ for finding an $ε$-approximate stationary point. Empirically, OMGD is a lightweight, plug-and-play approach that integrates seamlessly into most mainstream optimizers, yielding consistent improvements over competitive baselines in both fine-tuning and pre-training tasks.

