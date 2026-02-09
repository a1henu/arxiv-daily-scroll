---
layout: default
title: Force Generative Imitation Learning: Bridging Position Trajectory and Force Commands through Control Technique
---

# Force Generative Imitation Learning: Bridging Position Trajectory and Force Commands through Control Technique
**arXiv**：[2602.06620v1](https://arxiv.org/abs/2602.06620) · [PDF](https://arxiv.org/pdf/2602.06620.pdf)  
**作者**：Hiroshi Sato, Sho Sakaino, Toshiaki Tsuji  

**一句话要点**：提出力生成模仿学习，通过控制技术桥接位置轨迹与力命令以提升泛化能力。

**关键词**：力生成模仿学习, 位置轨迹, 力命令, 反馈控制, 机器人书写, 泛化能力

## 3 点简述
- 核心问题：接触任务中位置轨迹易得但力命令未知，且硬件依赖性强。
- 方法要点：构建力生成模型从位置轨迹估计力命令，引入无记忆模型实现稳定反馈控制。
- 实验或效果：在未见轨迹上有效生成力命令，改善机器人书写任务的泛化性能。

## 摘要（原文）

> In contact-rich tasks, while position trajectories are often easy to obtain, appropriate force commands are typically unknown. Although it is conceivable to generate force commands using a pretrained foundation model such as Vision-Language-Action (VLA) models, force control is highly dependent on the specific hardware of the robot, which makes the application of such models challenging. To bridge this gap, we propose a force generative model that estimates force commands from given position trajectories. However, when dealing with unseen position trajectories, the model struggles to generate accurate force commands. To address this, we introduce a feedback control mechanism. Our experiments reveal that feedback control does not converge when the force generative model has memory. We therefore adopt a model without memory, enabling stable feedback control. This approach allows the system to generate force commands effectively, even for unseen position trajectories, improving generalization for real-world robot writing tasks.

