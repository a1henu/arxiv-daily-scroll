---
layout: default
title: Distillation-Guided Structural Transfer for Continual Learning Beyond Sparse Distributed Memory
---

# Distillation-Guided Structural Transfer for Continual Learning Beyond Sparse Distributed Memory
**arXiv**：[2512.15267v1](https://arxiv.org/abs/2512.15267) · [PDF](https://arxiv.org/pdf/2512.15267.pdf)  
**作者**：Huiyan Xue, Xuming Ran, Yaxin Li, Qi Xu, Enhui Li, Yi Xu, Qiang Zhang  

**一句话要点**：提出选择性子网络蒸馏以提升稀疏分布式内存在持续学习中的知识重用与性能

**关键词**：稀疏神经网络, 持续学习, 知识蒸馏, 结构对齐, 选择性蒸馏, 模块化学习

## 3 点简述
- 稀疏神经网络如SDMLP在持续学习中面临模块化刚性导致跨任务知识重用受限的问题
- SSD方法通过激活频率识别神经元，在Top-K子网络和输出logits间进行选择性蒸馏，无需回放或任务标签
- 在Split CIFAR-10等数据集上实验显示SSD提高了准确性、保留率和表示覆盖度

## 摘要（原文）

> Sparse neural systems are gaining traction for efficient continual learning due to their modularity and low interference. Architectures such as Sparse Distributed Memory Multi-Layer Perceptrons (SDMLP) construct task-specific subnetworks via Top-K activation and have shown resilience against catastrophic forgetting. However, their rigid modularity limits cross-task knowledge reuse and leads to performance degradation under high sparsity. We propose Selective Subnetwork Distillation (SSD), a structurally guided continual learning framework that treats distillation not as a regularizer but as a topology-aligned information conduit. SSD identifies neurons with high activation frequency and selectively distills knowledge within previous Top-K subnetworks and output logits, without requiring replay or task labels. This enables structural realignment while preserving sparse modularity. Experiments on Split CIFAR-10, CIFAR-100, and MNIST demonstrate that SSD improves accuracy, retention, and representation coverage, offering a structurally grounded solution for sparse continual learning.

