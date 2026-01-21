---
layout: default
title: Performance and Complexity Trade-off Optimization of Speech Models During Training
---

# Performance and Complexity Trade-off Optimization of Speech Models During Training
**arXiv**：[2601.13704v1](https://arxiv.org/abs/2601.13704) · [PDF](https://arxiv.org/pdf/2601.13704.pdf)  
**作者**：Esteban Gómez, Tom Bäckström  

**一句话要点**：提出基于特征噪声注入的重参数化技术，以在训练中联合优化语音模型的性能与计算复杂度。

**关键词**：语音模型优化, 计算复杂度, 重参数化, 特征噪声注入, 联合优化

## 3 点简述
- 核心问题：传统方法无法在训练中直接优化非可微的计算复杂度，导致性能与复杂度权衡不优。
- 方法要点：通过特征噪声注入实现重参数化，使SGD能联合优化性能与复杂度，动态调整模型大小。
- 实验或效果：在合成示例、语音活动检测和音频反欺骗三个案例中验证了方法的有效性。

## 摘要（原文）

> In speech machine learning, neural network models are typically designed by choosing an architecture with fixed layer sizes and structure. These models are then trained to maximize performance on metrics aligned with the task's objective. While the overall architecture is usually guided by prior knowledge of the task, the sizes of individual layers are often chosen heuristically. However, this approach does not guarantee an optimal trade-off between performance and computational complexity; consequently, post hoc methods such as weight quantization or model pruning are typically employed to reduce computational cost. This occurs because stochastic gradient descent (SGD) methods can only optimize differentiable functions, while factors influencing computational complexity, such as layer sizes and floating-point operations per second (FLOP/s), are non-differentiable and require modifying the model structure during training. We propose a reparameterization technique based on feature noise injection that enables joint optimization of performance and computational complexity during training using SGD-based methods. Unlike traditional pruning methods, our approach allows the model size to be dynamically optimized for a target performance-complexity trade-off, without relying on heuristic criteria to select which weights or structures to remove. We demonstrate the effectiveness of our method through three case studies, including a synthetic example and two practical real-world applications: voice activity detection and audio anti-spoofing. The code related to our work is publicly available to encourage further research.

