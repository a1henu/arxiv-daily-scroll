---
layout: default
title: A New Perspective on Transformers in Online Reinforcement Learning for Continuous Control
---

# A New Perspective on Transformers in Online Reinforcement Learning for Continuous Control
**arXiv**：[2510.13367v1](https://arxiv.org/abs/2510.13367) · [PDF](https://arxiv.org/pdf/2510.13367.pdf)  
**作者**：Nikita Kachaev, Daniil Zelezetsky, Egor Cherepanov, Alexey K. Kovelev, Aleksandr I. Panov  

**一句话要点**：提出Transformer架构与训练策略，用于在线无模型强化学习的连续控制任务。

**关键词**：在线强化学习, Transformer架构, 连续控制, 模型设计策略, 序列数据处理

## 3 点简述
- 核心问题：Transformer在在线无模型强化学习中应用不足，因对训练设置和模型设计敏感。
- 方法要点：研究输入条件、组件共享和序列数据切片等关键设计问题。
- 实验或效果：在完全和部分可观测任务中实现竞争性能，适用于向量和图像设置。

## 摘要（原文）

> Despite their effectiveness and popularity in offline or model-based
> reinforcement learning (RL), transformers remain underexplored in online
> model-free RL due to their sensitivity to training setups and model design
> decisions such as how to structure the policy and value networks, share
> components, or handle temporal information. In this paper, we show that
> transformers can be strong baselines for continuous control in online
> model-free RL. We investigate key design questions: how to condition inputs,
> share components between actor and critic, and slice sequential data for
> training. Our experiments reveal stable architectural and training strategies
> enabling competitive performance across fully and partially observable tasks,
> and in both vector- and image-based settings. These findings offer practical
> guidance for applying transformers in online RL.

