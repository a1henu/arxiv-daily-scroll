---
layout: default
title: Training-Free Adaptation of Diffusion Models via Doob's $h$-Transform
---

# Training-Free Adaptation of Diffusion Models via Doob's $h$-Transform
**arXiv**：[2602.16198v1](https://arxiv.org/abs/2602.16198) · [PDF](https://arxiv.org/pdf/2602.16198.pdf)  
**作者**：Qijie Zhu, Zeqi Ye, Han Liu, Zhaoran Wang, Minshuo Chen  

**一句话要点**：提出DOIT方法，基于Doob's h-Transform实现免训练扩散模型适应，适用于不可微奖励场景。

**关键词**：扩散模型适应, Doob's h-Transform, 免训练优化, 不可微奖励, 测度传输, 离线强化学习

## 3 点简述
- 现有扩散模型适应方法依赖额外训练或可微奖励，计算开销大且理论保障不足。
- DOIT通过测度传输框架，利用Doob's h-Transform动态校正采样过程，无需修改预训练模型。
- 在D4RL离线RL基准测试中，DOIT优于现有方法，保持采样效率并提供收敛理论保证。

## 摘要（原文）

> Adaptation methods have been a workhorse for unlocking the transformative power of pre-trained diffusion models in diverse applications. Existing approaches often abstract adaptation objectives as a reward function and steer diffusion models to generate high-reward samples. However, these approaches can incur high computational overhead due to additional training, or rely on stringent assumptions on the reward such as differentiability. Moreover, despite their empirical success, theoretical justification and guarantees are seldom established. In this paper, we propose DOIT (Doob-Oriented Inference-time Transformation), a training-free and computationally efficient adaptation method that applies to generic, non-differentiable rewards. The key framework underlying our method is a measure transport formulation that seeks to transport the pre-trained generative distribution to a high-reward target distribution. We leverage Doob's $h$-transform to realize this transport, which induces a dynamic correction to the diffusion sampling process and enables efficient simulation-based computation without modifying the pre-trained model. Theoretically, we establish a high probability convergence guarantee to the target high-reward distribution via characterizing the approximation error in the dynamic Doob's correction. Empirically, on D4RL offline RL benchmarks, our method consistently outperforms state-of-the-art baselines while preserving sampling efficiency.

