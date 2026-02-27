---
layout: default
title: Simple Models, Real Swimming: Digital Twins for Tendon-Driven Underwater Robots
---

# Simple Models, Real Swimming: Digital Twins for Tendon-Driven Underwater Robots
**arXiv**：[2602.23283v1](https://arxiv.org/abs/2602.23283) · [PDF](https://arxiv.org/pdf/2602.23283.pdf)  
**作者**：Mike Y. Michelis, Nana Obayashi, Josie Hughes, Robert K. Katzschmann  

**一句话要点**：提出基于简化流体模型的数字孪生方法，用于肌腱驱动水下机器人高效仿真与控制。

**关键词**：软体机器人, 水下游泳仿真, 数字孪生, 简化流体模型, 强化学习, 肌腱驱动

## 3 点简述
- 核心问题：软体机器人游泳运动建模复杂，现有方法计算成本高，难以支持实时控制与强化学习。
- 方法要点：在MuJoCo中实现无状态简化流体模型，仅用两条真实轨迹识别五个流体参数，匹配实验行为。
- 实验或效果：模型泛化至未见驱动，超越经典理论，仿真快于实时，强化学习目标跟踪成功率93%。

## 摘要（原文）

> Mimicking the graceful motion of swimming animals remains a core challenge in soft robotics due to the complexity of fluid-structure interaction and the difficulty of controlling soft, biomimetic bodies. Existing modeling approaches are often computationally expensive and impractical for complex control or reinforcement learning needed for realistic motions to emerge in robotic systems. In this work, we present a tendon-driven fish robot modeled in an efficient underwater swimmer environment using a simplified, stateless hydrodynamics formulation implemented in the widespread robotics framework MuJoCo. With just two real-world swimming trajectories, we identify five fluid parameters that allow a matching to experimental behavior and generalize across a range of actuation frequencies. We show that this stateless fluid model can generalize to unseen actuation and outperform classical analytical models such as the elongated body theory. This simulation environment runs faster than real-time and can easily enable downstream learning algorithms such as reinforcement learning for target tracking, reaching a 93% success rate. Due to the simplicity and ease of use of the model and our open-source simulation environment, our results show that even simple, stateless models -- when carefully matched to physical data -- can serve as effective digital twins for soft underwater robots, opening up new directions for scalable learning and control in aquatic environments.

