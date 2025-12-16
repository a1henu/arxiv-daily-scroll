---
layout: default
title: Alada: Alternating Adaptation of Momentum Method for Memory-Efficient Matrix Optimization
---

# Alada: Alternating Adaptation of Momentum Method for Memory-Efficient Matrix Optimization
**arXiv**：[2512.13034v1](https://arxiv.org/abs/2512.13034) · [PDF](https://arxiv.org/pdf/2512.13034.pdf)  
**作者**：Xiaoyu He, Yu Cai, Jin Jia, Canxi Huang, Wenqing Chen, Zibin Zheng  

**一句话要点**：提出Alada自适应动量方法，用于大规模矩阵优化的内存高效训练。

**关键词**：自适应动量方法, 矩阵优化, 内存高效训练, 秩一分解, 自然语言处理, 大规模模型训练

## 3 点简述
- 核心问题：大规模矩阵优化中梯度二阶矩估计的内存开销高。
- 方法要点：采用秩一分解交替更新因子，减少估计误差和内存占用。
- 实验或效果：在自然语言处理任务中，相比Adam及其变体，内存开销降低且训练稳健。

## 摘要（原文）

> This work proposes Alada, an adaptive momentum method for stochastic optimization over large-scale matrices. Alada employs a rank-one factorization approach to estimate the second moment of gradients, where factors are updated alternatively to minimize the estimation error. Alada achieves sublinear memory overheads and can be readily extended to optimizing tensor-shaped variables.We also equip Alada with a first moment estimation rule, which enhances the algorithm's robustness without incurring additional memory overheads. The theoretical performance of Alada aligns with that of traditional methods such as Adam. Numerical studies conducted on several natural language processing tasks demonstrate the reduction in memory overheads and the robustness in training large models relative to Adam and its variants.

