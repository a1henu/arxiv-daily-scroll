---
layout: default
title: MDG: Masked Denoising Generation for Multi-Agent Behavior Modeling in Traffic Environments
---

# MDG: Masked Denoising Generation for Multi-Agent Behavior Modeling in Traffic Environments
**arXiv**：[2511.17496v1](https://arxiv.org/abs/2511.17496) · [PDF](https://arxiv.org/pdf/2511.17496.pdf)  
**作者**：Zhiyu Huang, Zewei Zhou, Tianhui Cai, Yun Zhang, Jiaqi Ma  

**一句话要点**：提出MDG框架以解决交通环境中多智能体行为建模的效率与通用性问题

**关键词**：多智能体行为建模, 掩码去噪生成, 交通环境模拟, 轨迹生成, 自动驾驶仿真

## 3 点简述
- 现有扩散和自回归方法受限于迭代采样或任务特定设计，影响效率与复用
- MDG通过独立噪声时空张量重构，实现局部去噪和可控轨迹生成
- 在Waymo和nuPlan基准上实现竞争性闭环性能，并提供高效开环生成

## 摘要（原文）

> Modeling realistic and interactive multi-agent behavior is critical to autonomous driving and traffic simulation. However, existing diffusion and autoregressive approaches are limited by iterative sampling, sequential decoding, or task-specific designs, which hinder efficiency and reuse. We propose Masked Denoising Generation (MDG), a unified generative framework that reformulates multi-agent behavior modeling as the reconstruction of independently noised spatiotemporal tensors. Instead of relying on diffusion time steps or discrete tokenization, MDG applies continuous, per-agent and per-timestep noise masks that enable localized denoising and controllable trajectory generation in a single or few forward passes. This mask-driven formulation generalizes across open-loop prediction, closed-loop simulation, motion planning, and conditional generation within one model. Trained on large-scale real-world driving datasets, MDG achieves competitive closed-loop performance on the Waymo Sim Agents and nuPlan Planning benchmarks, while providing efficient, consistent, and controllable open-loop multi-agent trajectory generation. These results position MDG as a simple yet versatile paradigm for multi-agent behavior modeling.

