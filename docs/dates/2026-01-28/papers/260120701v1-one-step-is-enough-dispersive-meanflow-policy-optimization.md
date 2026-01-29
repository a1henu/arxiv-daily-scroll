---
layout: default
title: One Step Is Enough: Dispersive MeanFlow Policy Optimization
---

# One Step Is Enough: Dispersive MeanFlow Policy Optimization
**arXiv**：[2601.20701v1](https://arxiv.org/abs/2601.20701) · [PDF](https://arxiv.org/pdf/2601.20701.pdf)  
**作者**：Guowei Zou, Haitao Wang, Hejun Wu, Yukun Qian, Yuhang Wang, Weibing Li  

**一句话要点**：提出Dispersive MeanFlow Policy Optimization以实现实时机器人控制中的一步生成策略。

**关键词**：一步生成策略, 实时机器人控制, MeanFlow推理, 分散正则化, 强化学习微调

## 3 点简述
- 核心问题：现有基于扩散和流匹配的生成策略需多步采样，限制实时控制部署。
- 方法要点：结合MeanFlow单步推理、分散正则化和强化学习微调，实现一步生成。
- 实验或效果：在机器人操作和运动基准测试中表现竞争或更优，推理速度提升5-20倍，满足>120Hz实时需求。

## 摘要（原文）

> Real-time robotic control demands fast action generation. However, existing generative policies based on diffusion and flow matching require multi-step
>   sampling, fundamentally limiting deployment in time-critical scenarios. We propose Dispersive MeanFlow Policy Optimization (DMPO), a unified framework that
>   enables true one-step generation through three key components: MeanFlow for mathematically-derived single-step inference without knowledge distillation,
>   dispersive regularization to prevent representation collapse, and reinforcement learning (RL) fine-tuning to surpass expert demonstrations. Experiments
>   across RoboMimic manipulation and OpenAI Gym locomotion benchmarks demonstrate competitive or superior performance compared to multi-step baselines. With
>   our lightweight model architecture and the three key algorithmic components working in synergy, DMPO exceeds real-time control requirements (>120Hz) with
>   5-20x inference speedup, reaching hundreds of Hertz on high-performance GPUs. Physical deployment on a Franka-Emika-Panda robot validates real-world
>   applicability.

