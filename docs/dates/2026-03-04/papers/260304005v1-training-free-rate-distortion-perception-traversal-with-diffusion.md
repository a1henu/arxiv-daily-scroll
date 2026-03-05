---
layout: default
title: Training-Free Rate-Distortion-Perception Traversal With Diffusion
---

# Training-Free Rate-Distortion-Perception Traversal With Diffusion
**arXiv**：[2603.04005v1](https://arxiv.org/abs/2603.04005) · [PDF](https://arxiv.org/pdf/2603.04005.pdf)  
**作者**：Yuhan Wang, Suzhi Bi, Ying-Jun Angela Zhang  

**一句话要点**：提出基于预训练扩散模型的无训练框架，以遍历率失真感知权衡曲面

**关键词**：率失真感知权衡, 扩散模型, 无训练压缩, 反向信道编码, 概率流ODE, 感知质量优化

## 3 点简述
- 核心问题：现有神经压缩方法需重训练以调整率失真感知权衡，灵活性不足
- 方法要点：结合反向信道编码模块与分数缩放概率流ODE解码器，实现无训练遍历
- 实验或效果：理论证明高斯情况下的最优性，多数据集验证框架的灵活性与有效性

## 摘要（原文）

> The rate-distortion-perception (RDP) tradeoff characterizes the fundamental limits of lossy compression by jointly considering bitrate, reconstruction fidelity, and perceptual quality. While recent neural compression methods have improved perceptual performance, they typically operate at fixed points on the RDP surface, requiring retraining to target different tradeoffs. In this work, we propose a training-free framework that leverages pre-trained diffusion models to traverse the entire RDP surface. Our approach integrates a reverse channel coding (RCC) module with a novel score-scaled probability flow ODE decoder. We theoretically prove that the proposed diffusion decoder is optimal for the distortion-perception tradeoff under AWGN observations and that the overall framework with the RCC module achieves the optimal RDP function in the Gaussian case. Empirical results across multiple datasets demonstrate the framework's flexibility and effectiveness in navigating the ternary RDP tradeoff using pre-trained diffusion models. Our results establish a practical and theoretically grounded approach to adaptive, perception-aware compression.

