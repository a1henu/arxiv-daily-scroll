---
layout: default
title: SpikingGamma: Surrogate-Gradient Free and Temporally Precise Online Training of Spiking Neural Networks with Smoothed Delays
---

# SpikingGamma: Surrogate-Gradient Free and Temporally Precise Online Training of Spiking Neural Networks with Smoothed Delays
**arXiv**：[2602.01978v1](https://arxiv.org/abs/2602.01978) · [PDF](https://arxiv.org/pdf/2602.01978.pdf)  
**作者**：Roel Koopman, Sebastian Otte, Sander Bohté  

**一句话要点**：提出SpikingGamma模型，通过内部递归记忆与sigma-delta脉冲编码，实现无代理梯度的在线训练，以解决脉冲神经网络在精细时间分辨率下的训练挑战。

**关键词**：脉冲神经网络, 在线训练, 无代理梯度, 时间模式学习, 神经形态硬件映射

## 3 点简述
- 核心问题：当前脉冲神经网络训练方法在精细时间分辨率下扩展性差，在线近似不稳定且难以精确捕捉时间模式。
- 方法要点：结合内部递归记忆结构和sigma-delta脉冲编码，支持直接误差反向传播，无需代理梯度。
- 实验或效果：模型能在线学习精细时间模式，在复杂任务上达到竞争性准确度，且对时间分辨率不敏感。

## 摘要（原文）

> Neuromorphic hardware implementations of Spiking Neural Networks (SNNs) promise energy-efficient, low-latency AI through sparse, event-driven computation. Yet, training SNNs under fine temporal discretization remains a major challenge, hindering both low-latency responsiveness and the mapping of software-trained SNNs to efficient hardware. In current approaches, spiking neurons are modeled as self-recurrent units, embedded into recurrent networks to maintain state over time, and trained with BPTT or RTRL variants based on surrogate gradients. These methods scale poorly with temporal resolution, while online approximations often exhibit instability for long sequences and tend to fail at capturing temporal patterns precisely. To address these limitations, we develop spiking neurons with internal recursive memory structures that we combine with sigma-delta spike-coding. We show that this SpikingGamma model supports direct error backpropagation without surrogate gradients, can learn fine temporal patterns with minimal spiking in an online manner, and scale feedforward SNNs to complex tasks and benchmarks with competitive accuracy, all while being insensitive to the temporal resolution of the model. Our approach offers both an alternative to current recurrent SNNs trained with surrogate gradients, and a direct route for mapping SNNs to neuromorphic hardware.

