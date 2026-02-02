---
layout: default
title: MTDrive: Multi-turn Interactive Reinforcement Learning for Autonomous Driving
---

# MTDrive: Multi-turn Interactive Reinforcement Learning for Autonomous Driving
**arXiv**：[2601.22930v1](https://arxiv.org/abs/2601.22930) · [PDF](https://arxiv.org/pdf/2601.22930.pdf)  
**作者**：Xidong Li, Mingyu Guo, Chenchao Xu, Bailin Li, Wenjing Zhu, Yangang Zou, Rui Chen, Zehuan Wang  

**一句话要点**：提出MTDrive多轮交互强化学习框架，以迭代优化自动驾驶轨迹规划。

**关键词**：自动驾驶, 轨迹规划, 多轮交互, 强化学习, 多模态大语言模型, 奖励稀疏性

## 3 点简述
- 核心问题：现有单轮推理方法难以处理自动驾驶中复杂场景的迭代优化需求。
- 方法要点：引入多轮组相对策略优化（mtGRPO），通过跨轮次相对优势缓解奖励稀疏性。
- 实验或效果：在NAVSIM基准测试中表现优于现有方法，训练吞吐量提升2.5倍。

## 摘要（原文）

> Trajectory planning is a core task in autonomous driving, requiring the prediction of safe and comfortable paths across diverse scenarios. Integrating Multi-modal Large Language Models (MLLMs) with Reinforcement Learning (RL) has shown promise in addressing "long-tail" scenarios. However, existing methods are constrained to single-turn reasoning, limiting their ability to handle complex tasks requiring iterative refinement. To overcome this limitation, we present MTDrive, a multi-turn framework that enables MLLMs to iteratively refine trajectories based on environmental feedback. MTDrive introduces Multi-Turn Group Relative Policy Optimization (mtGRPO), which mitigates reward sparsity by computing relative advantages across turns. We further construct an interactive trajectory understanding dataset from closed-loop simulation to support multi-turn training. Experiments on the NAVSIM benchmark demonstrate superior performance compared to existing methods, validating the effectiveness of our multi-turn reasoning paradigm. Additionally, we implement system-level optimizations to reduce data transfer overhead caused by high-resolution images and multi-turn sequences, achieving 2.5x training throughput. Our data, models, and code will be made available soon.

