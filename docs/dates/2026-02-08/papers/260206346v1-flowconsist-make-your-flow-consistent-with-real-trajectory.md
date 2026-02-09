---
layout: default
title: FlowConsist: Make Your Flow Consistent with Real Trajectory
---

# FlowConsist: Make Your Flow Consistent with Real Trajectory
**arXiv**：[2602.06346v1](https://arxiv.org/abs/2602.06346) · [PDF](https://arxiv.org/pdf/2602.06346.pdf)  
**作者**：Tianyi Zhang, Chengcheng Liu, Jinwei Chen, Chun-Le Guo, Chongyi Li, Ming-Ming Cheng, Bo Li, Peng-Tao Jiang  

**一句话要点**：提出FlowConsist训练框架以解决快速流模型中的轨迹漂移和误差累积问题

**关键词**：快速流模型, 轨迹一致性, ODE路径积分, 误差累积, 图像生成

## 3 点简述
- 核心问题：当前快速流模型因随机配对噪声-数据样本构建条件速度导致轨迹漂移，且近似误差随时间步累积
- 方法要点：用模型预测的边际速度替代条件速度，并引入轨迹校正策略对齐生成与真实样本的边际分布
- 实验或效果：在ImageNet 256×256上实现FID 1.52，仅需1步采样，达到新SOTA

## 摘要（原文）

> Fast flow models accelerate the iterative sampling process by learning to directly predict ODE path integrals, enabling one-step or few-step generation. However, we argue that current fast-flow training paradigms suffer from two fundamental issues. First, conditional velocities constructed from randomly paired noise-data samples introduce systematic trajectory drift, preventing models from following a consistent ODE path. Second, the model's approximation errors accumulate over time steps, leading to severe deviations across long time intervals. To address these issues, we propose FlowConsist, a training framework designed to enforce trajectory consistency in fast flows. We propose a principled alternative that replaces conditional velocities with the marginal velocities predicted by the model itself, aligning optimization with the true trajectory. To further address error accumulation over time steps, we introduce a trajectory rectification strategy that aligns the marginal distributions of generated and real samples at every time step along the trajectory. Our method establishes a new state-of-the-art on ImageNet 256$\times$256, achieving an FID of 1.52 with only 1 sampling step.

