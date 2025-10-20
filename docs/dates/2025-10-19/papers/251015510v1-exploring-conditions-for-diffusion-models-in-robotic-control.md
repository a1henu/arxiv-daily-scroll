---
layout: default
title: Exploring Conditions for Diffusion models in Robotic Control
---

# Exploring Conditions for Diffusion models in Robotic Control
**arXiv**：[2510.15510v1](https://arxiv.org/abs/2510.15510) · [PDF](https://arxiv.org/pdf/2510.15510.pdf)  
**作者**：Heeseong Shin, Byeongho Heo, Dongyoon Han, Seungryong Kim, Taekyung Kim  

**一句话要点**：提出ORCA方法，利用可学习提示优化扩散模型在机器人控制中的视觉表示

**关键词**：扩散模型, 机器人控制, 视觉表示学习, 任务自适应, 提示学习

## 3 点简述
- 核心问题：预训练扩散模型在机器人控制中因领域差异，文本条件应用效果不佳。
- 方法要点：引入可学习任务提示和视觉提示，适应控制环境与帧细节。
- 实验或效果：在多个机器人控制基准上实现最优性能，显著超越先前方法。

## 摘要（原文）

> While pre-trained visual representations have significantly advanced
> imitation learning, they are often task-agnostic as they remain frozen during
> policy learning. In this work, we explore leveraging pre-trained text-to-image
> diffusion models to obtain task-adaptive visual representations for robotic
> control, without fine-tuning the model itself. However, we find that naively
> applying textual conditions - a successful strategy in other vision domains -
> yields minimal or even negative gains in control tasks. We attribute this to
> the domain gap between the diffusion model's training data and robotic control
> environments, leading us to argue for conditions that consider the specific,
> dynamic visual information required for control. To this end, we propose ORCA,
> which introduces learnable task prompts that adapt to the control environment
> and visual prompts that capture fine-grained, frame-specific details. Through
> facilitating task-adaptive representations with our newly devised conditions,
> our approach achieves state-of-the-art performance on various robotic control
> benchmarks, significantly surpassing prior methods.

