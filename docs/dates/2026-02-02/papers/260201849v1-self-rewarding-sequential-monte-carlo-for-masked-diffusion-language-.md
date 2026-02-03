---
layout: default
title: Self-Rewarding Sequential Monte Carlo for Masked Diffusion Language Models
---

# Self-Rewarding Sequential Monte Carlo for Masked Diffusion Language Models
**arXiv**：[2602.01849v1](https://arxiv.org/abs/2602.01849) · [PDF](https://arxiv.org/pdf/2602.01849.pdf)  
**作者**：Ziwei Luo, Ziqi Jin, Lei Wang, Lidong Bing, Thomas B. Schön  

**一句话要点**：提出自奖励序列蒙特卡洛方法，以提升掩码扩散语言模型的采样质量与多样性。

**关键词**：掩码扩散语言模型, 序列蒙特卡洛, 采样算法, 自奖励机制, 并行推理

## 3 点简述
- 核心问题：现有掩码扩散语言模型依赖置信度采样，导致生成路径多样性受限和噪声敏感。
- 方法要点：并行启动多个扩散粒子进行轨迹探索，利用轨迹级置信度作为自奖励信号分配权重并迭代重采样。
- 实验或效果：在多个模型和基准上验证，无需额外训练或奖励指导，显著提升采样质量。

## 摘要（原文）

> This work presents self-rewarding sequential Monte Carlo (SMC), an inference-time scaling algorithm enabling effective sampling of masked diffusion language models (MDLMs). Our algorithm stems from the observation that most existing MDLMs rely on a confidence-based sampling strategy, where only tokens with the highest prediction confidence are preserved at each step. This restricts the generation to a noise-sensitive, greedy decoding paradigm, resulting in an inevitable collapse in the diversity of possible paths. We address this problem by launching multiple interacting diffusion processes in parallel, referred to as particles, for trajectory exploration. Importantly, we introduce the trajectory-level confidence as a self-rewarding signal for assigning particle importance weights. During sampling, particles are iteratively weighted and resampled to systematically steer generation towards globally confident, high-quality samples. Our self-rewarding SMC is verified on various masked diffusion language models and benchmarks, achieving significant improvement without extra training or reward guidance, while effectively converting parallel inference capacity into improved sampling quality. Our code is available at https://github.com/Algolzw/self-rewarding-smc.

