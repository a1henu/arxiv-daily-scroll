---
layout: default
title: Beyond SGD, Without SVD: Proximal Subspace Iteration LoRA with Diagonal Fractional K-FAC
---

# Beyond SGD, Without SVD: Proximal Subspace Iteration LoRA with Diagonal Fractional K-FAC
**arXiv**：[2602.16456v1](https://arxiv.org/abs/2602.16456) · [PDF](https://arxiv.org/pdf/2602.16456.pdf)  
**作者**：Abdulla Jasem Almansoori, Maria Ivanova, Andrey Veprikov, Aleksandr Beznosikov, Samuel Horváth, Martin Takáč  

**一句话要点**：提出LoRSum方法以解决LoRA优化中低秩投影与全步训练之间的差距

**关键词**：低秩适应, 优化算法, 内存效率, 梯度下降, 结构化度量, 模型微调

## 3 点简述
- 核心问题：LoRA微调中低秩投影与全步训练存在性能差距，需高效优化方法
- 方法要点：将LoRA优化建模为近端子问题，通过交替最小二乘更新实现内存高效求解
- 实验或效果：在合成任务、CIFAR-100和语言模型微调中匹配或改进LoRA基线，保持参数效率

## 摘要（原文）

> Low-Rank Adaptation (LoRA) fine-tunes large models by learning low-rank updates on top of frozen weights, dramatically reducing trainable parameters and memory. In this work, we address the gap between training with full steps with low-rank projections (SVDLoRA) and LoRA fine-tuning. We propose LoRSum, a memory-efficient subroutine that closes this gap for gradient descent by casting LoRA optimization as a proximal sub-problem and solving it efficiently with alternating least squares updates, which we prove to be an implicit block power method. We recover several recently proposed preconditioning methods for LoRA as special cases, and show that LoRSum can also be used for updating a low-rank momentum. In order to address full steps with preconditioned gradient descent, we propose a scaled variant of LoRSum that uses structured metrics such as K-FAC and Shampoo, and we show that storing the diagonal of these metrics still allows them to perform well while remaining memory-efficient. Experiments on a synthetic task, CIFAR-100, and language-model fine-tuning on GLUE, SQuAD v2, and WikiText-103, show that our method can match or improve LoRA baselines given modest compute overhead, while avoiding full-matrix SVD projections and retaining LoRA-style parameter efficiency.

