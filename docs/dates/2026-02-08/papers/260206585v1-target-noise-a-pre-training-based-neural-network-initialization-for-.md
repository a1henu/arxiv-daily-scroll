---
layout: default
title: Target noise: A pre-training based neural network initialization for efficient high resolution learning
---

# Target noise: A pre-training based neural network initialization for efficient high resolution learning
**arXiv**：[2602.06585v1](https://arxiv.org/abs/2602.06585) · [PDF](https://arxiv.org/pdf/2602.06585.pdf)  
**作者**：Shaowen Wang, Tariq Alkhalifah  

**一句话要点**：提出基于随机噪声自监督预训练的初始化方法，以提升神经网络优化效率，特别适用于隐式神经表示和深度图像先验网络。

**关键词**：权重初始化, 自监督预训练, 隐式神经表示, 深度图像先验, 优化效率, 随机噪声

## 3 点简述
- 核心问题：传统初始化方法如Xavier和Kaiming依赖随机采样，未利用优化过程信息，导致收敛效率低。
- 方法要点：使用随机噪声作为目标进行自监督预训练，生成结构化参数配置，无需额外数据或架构改动。
- 实验或效果：噪声预训练显著加速后续任务收敛，尤其在隐式神经表示和深度图像先验网络中，能早期捕获高频分量，提升稳定性和速度。

## 摘要（原文）

> Weight initialization plays a crucial role in the optimization behavior and convergence efficiency of neural networks. Most existing initialization methods, such as Xavier and Kaiming initializations, rely on random sampling and do not exploit information from the optimization process itself. We propose a simple, yet effective, initialization strategy based on self-supervised pre-training using random noise as the target. Instead of directly training the network from random weights, we first pre-train it to fit random noise, which leads to a structured and non-random parameter configuration. We show that this noise-driven pre-training significantly improves convergence speed in subsequent tasks, without requiring additional data or changes to the network architecture. The proposed method is particularly effective for implicit neural representations (INRs) and Deep Image Prior (DIP)-style networks, which are known to exhibit a strong low-frequency bias during optimization. After noise-based pre-training, the network is able to capture high-frequency components much earlier in training, leading to faster and more stable convergence. Although random noise contains no semantic information, it serves as an effective self-supervised signal (considering its white spectrum nature) for shaping the initialization of neural networks. Overall, this work demonstrates that noise-based pre-training offers a lightweight and general alternative to traditional random initialization, enabling more efficient optimization of deep neural networks.

