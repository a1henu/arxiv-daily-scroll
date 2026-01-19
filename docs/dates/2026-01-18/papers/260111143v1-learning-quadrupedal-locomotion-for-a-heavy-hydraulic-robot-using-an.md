---
layout: default
title: Learning Quadrupedal Locomotion for a Heavy Hydraulic Robot Using an Actuator Model
---

# Learning Quadrupedal Locomotion for a Heavy Hydraulic Robot Using an Actuator Model
**arXiv**：[2601.11143v1](https://arxiv.org/abs/2601.11143) · [PDF](https://arxiv.org/pdf/2601.11143.pdf)  
**作者**：Minho Lee, Hyeonseok Kim, Jin Tak Kim, Sangshin Park, Jeong Hyun Lee, Jungsan Cho, Jemin Hwangbo  

**一句话要点**：提出基于液压动力学的解析执行器模型，以解决重型液压四足机器人仿真到现实迁移的挑战。

**关键词**：液压机器人, 仿真到现实迁移, 强化学习, 执行器建模, 四足机器人, 重型机器人

## 3 点简述
- 核心问题：大型液压机器人仿真到现实迁移困难，源于执行器响应慢和复杂流体动力学。
- 方法要点：开发快速解析执行器模型，预测12个执行器扭矩，适用于强化学习环境。
- 实验或效果：模型在数据有限场景优于神经网络模型，成功部署于300公斤机器人实现稳定运动。

## 摘要（原文）

> The simulation-to-reality (sim-to-real) transfer of large-scale hydraulic robots presents a significant challenge in robotics because of the inherent slow control response and complex fluid dynamics. The complex dynamics result from the multiple interconnected cylinder structure and the difference in fluid rates of the cylinders. These characteristics complicate detailed simulation for all joints, making it unsuitable for reinforcement learning (RL) applications. In this work, we propose an analytical actuator model driven by hydraulic dynamics to represent the complicated actuators. The model predicts joint torques for all 12 actuators in under 1 microsecond, allowing rapid processing in RL environments. We compare our model with neural network-based actuator models and demonstrate the advantages of our model in data-limited scenarios. The locomotion policy trained in RL with our model is deployed on a hydraulic quadruped robot, which is over 300 kg. This work is the first demonstration of a successful transfer of stable and robust command-tracking locomotion with RL on a heavy hydraulic quadruped robot, demonstrating advanced sim-to-real transferability.

