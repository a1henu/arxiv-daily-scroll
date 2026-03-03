---
layout: default
title: SageBwd: A Trainable Low-bit Attention
---

# SageBwd: A Trainable Low-bit Attention
**arXiv**：[2603.02170v1](https://arxiv.org/abs/2603.02170) · [PDF](https://arxiv.org/pdf/2603.02170.pdf)  
**作者**：Jintao Zhang, Marco Chen, Haoxu Wang, Kai Jiang, Ion Stoica, Joseph E. Gonzalez, Jianfei Chen, Jun Zhu  

**一句话要点**：提出SageBwd可训练低比特注意力，在预训练中匹配全精度注意力性能。

**关键词**：低比特注意力, 量化训练, 注意力机制, 预训练优化, 计算效率

## 3 点简述
- 核心问题：低比特注意力在预训练中性能落后于全精度注意力。
- 方法要点：量化七个注意力矩阵乘法中的六个，并采用QK-norm和K-smoothing确保稳定性。
- 实验或效果：通过减少每步令牌数，SageBwd在预训练中达到全精度注意力性能。

## 摘要（原文）

> Low-bit attention, such as SageAttention, has emerged as an effective approach for accelerating model inference, but its applicability to training remains poorly understood. In prior work, we introduced SageBwd, a trainable INT8 attention that quantizes six of seven attention matrix multiplications while preserving fine-tuning performance. However, SageBwd exhibited a persistent performance gap to full-precision attention (FPA) during pre-training. In this work, we investigate why this gap occurs and demonstrate that SageBwd matches full-precision attention during pretraining. Through experiments and theoretical analysis, we reach a few important insights and conclusions: (i) QK-norm is necessary for stable training at large tokens per step, (ii) quantization errors primarily arise from the backward-pass score gradient dS, (iii) reducing tokens per step enables SageBwd to match FPA performance in pre-training, and (iv) K-smoothing remains essential for training stability, while Q-smoothing provides limited benefit during pre-training.

