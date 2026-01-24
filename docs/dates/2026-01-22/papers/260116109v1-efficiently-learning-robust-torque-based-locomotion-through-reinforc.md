---
layout: default
title: Efficiently Learning Robust Torque-based Locomotion Through Reinforcement with Model-Based Supervision
---

# Efficiently Learning Robust Torque-based Locomotion Through Reinforcement with Model-Based Supervision
**arXiv**：[2601.16109v1](https://arxiv.org/abs/2601.16109) · [PDF](https://arxiv.org/pdf/2601.16109.pdf)  
**作者**：Yashuai Yan, Tobias Egle, Christian Ott, Dongheui Lee  

**一句话要点**：提出结合模型控制与残差强化学习的框架，以提升双足机器人在不确定性下的鲁棒行走能力。

**关键词**：双足机器人控制, 残差强化学习, 模型监督, 域随机化, 鲁棒行走, 仿真到真实迁移

## 3 点简述
- 核心问题：双足机器人在真实世界中面临动力学建模不准确和传感器噪声等不确定性，影响行走鲁棒性。
- 方法要点：利用模型控制器作为基础策略，通过域随机化的残差强化学习训练校正策略，并引入基于模型的监督损失进行高效学习。
- 实验或效果：在随机化条件下展示改进的鲁棒性和泛化能力，为仿真到真实迁移提供可扩展方案。

## 摘要（原文）

> We propose a control framework that integrates model-based bipedal locomotion with residual reinforcement learning (RL) to achieve robust and adaptive walking in the presence of real-world uncertainties. Our approach leverages a model-based controller, comprising a Divergent Component of Motion (DCM) trajectory planner and a whole-body controller, as a reliable base policy. To address the uncertainties of inaccurate dynamics modeling and sensor noise, we introduce a residual policy trained through RL with domain randomization. Crucially, we employ a model-based oracle policy, which has privileged access to ground-truth dynamics during training, to supervise the residual policy via a novel supervised loss. This supervision enables the policy to efficiently learn corrective behaviors that compensate for unmodeled effects without extensive reward shaping. Our method demonstrates improved robustness and generalization across a range of randomized conditions, offering a scalable solution for sim-to-real transfer in bipedal locomotion.

