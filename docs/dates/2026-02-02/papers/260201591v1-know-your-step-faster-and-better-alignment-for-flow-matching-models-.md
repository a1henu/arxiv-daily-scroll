---
layout: default
title: Know Your Step: Faster and Better Alignment for Flow Matching Models via Step-aware Advantages
---

# Know Your Step: Faster and Better Alignment for Flow Matching Models via Step-aware Advantages
**arXiv**：[2602.01591v1](https://arxiv.org/abs/2602.01591) · [PDF](https://arxiv.org/pdf/2602.01591.pdf)  
**作者**：Zhixiong Yue, Zixuan Ni, Feiyang Ye, Jinshan Zhang, Sheng Shen, Zhenpeng Mi  

**一句话要点**：提出TAFS-GRPO框架以解决流匹配模型在少步文本到图像生成中奖励稀疏和对齐不足的问题

**关键词**：流匹配模型, 文本到图像生成, 强化学习对齐, 少步生成, 温度退火采样, 组相对策略优化

## 3 点简述
- 现有基于强化学习的流匹配模型依赖多步去噪，奖励信号稀疏且不精确，导致对齐效果不佳
- TAFS-GRPO通过温度退火采样和组相对策略优化，引入自适应时间噪声和步感知优势，提供密集步特定奖励
- 实验表明该方法在少步文本到图像生成中性能强，显著提升生成图像与人类偏好的对齐度

## 摘要（原文）

> Recent advances in flow matching models, particularly with reinforcement learning (RL), have significantly enhanced human preference alignment in few step text to image generators. However, existing RL based approaches for flow matching models typically rely on numerous denoising steps, while suffering from sparse and imprecise reward signals that often lead to suboptimal alignment. To address these limitations, we propose Temperature Annealed Few step Sampling with Group Relative Policy Optimization (TAFS GRPO), a novel framework for training flow matching text to image models into efficient few step generators well aligned with human preferences. Our method iteratively injects adaptive temporal noise onto the results of one step samples. By repeatedly annealing the model's sampled outputs, it introduces stochasticity into the sampling process while preserving the semantic integrity of each generated image. Moreover, its step aware advantage integration mechanism combines the GRPO to avoid the need for the differentiable of reward function and provide dense and step specific rewards for stable policy optimization. Extensive experiments demonstrate that TAFS GRPO achieves strong performance in few step text to image generation and significantly improves the alignment of generated images with human preferences. The code and models of this work will be available to facilitate further research.

