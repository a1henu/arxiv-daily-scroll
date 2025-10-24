---
layout: default
title: VAMOS: A Hierarchical Vision-Language-Action Model for Capability-Modulated and Steerable Navigation
---

# VAMOS: A Hierarchical Vision-Language-Action Model for Capability-Modulated and Steerable Navigation
**arXiv**：[2510.20818v1](https://arxiv.org/abs/2510.20818) · [PDF](https://arxiv.org/pdf/2510.20818.pdf)  
**作者**：Mateo Guaman Castro, Sidharth Rajagopal, Daniel Gorbatov, Matt Schmittle, Rohan Baijal, Octi Zhang, Rosario Scalise, Sidharth Talia, Emma Romig, Celso de Melo, Byron Boots, Abhishek Gupta  

**一句话要点**：提出VAMOS分层视觉-语言-动作模型，实现能力调制和可引导的机器人导航

**关键词**：机器人导航, 分层模型, 视觉-语言-动作, 具身接地, 跨具身泛化, 自然语言引导

## 3 点简述
- 核心问题：机器人导航需泛化多环境并适应特定物理约束，如四足与轮式机器人能力差异。
- 方法要点：分层设计分离语义规划与具身接地，高层规划器提出路径，具身模型评估可行性。
- 实验效果：真实世界测试显示高成功率，支持跨具身导航和自然语言引导，提升可靠性。

## 摘要（原文）

> A fundamental challenge in robot navigation lies in learning policies that
> generalize across diverse environments while conforming to the unique physical
> constraints and capabilities of a specific embodiment (e.g., quadrupeds can
> walk up stairs, but rovers cannot). We propose VAMOS, a hierarchical VLA that
> decouples semantic planning from embodiment grounding: a generalist planner
> learns from diverse, open-world data, while a specialist affordance model
> learns the robot's physical constraints and capabilities in safe, low-cost
> simulation. We enabled this separation by carefully designing an interface that
> lets a high-level planner propose candidate paths directly in image space that
> the affordance model then evaluates and re-ranks. Our real-world experiments
> show that VAMOS achieves higher success rates in both indoor and complex
> outdoor navigation than state-of-the-art model-based and end-to-end learning
> methods. We also show that our hierarchical design enables cross-embodied
> navigation across legged and wheeled robots and is easily steerable using
> natural language. Real-world ablations confirm that the specialist model is key
> to embodiment grounding, enabling a single high-level planner to be deployed
> across physically distinct wheeled and legged robots. Finally, this model
> significantly enhances single-robot reliability, achieving 3X higher success
> rates by rejecting physically infeasible plans. Website:
> https://vamos-vla.github.io/

