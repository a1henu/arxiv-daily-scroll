---
layout: default
title: Morphology-Aware Graph Reinforcement Learning for Tensegrity Robot Locomotion
---

# Morphology-Aware Graph Reinforcement Learning for Tensegrity Robot Locomotion
**arXiv**：[2510.26067v1](https://arxiv.org/abs/2510.26067) · [PDF](https://arxiv.org/pdf/2510.26067.pdf)  
**作者**：Chi Zhang, Mingrui Li, Wenzhe Tong, Xiaonan Huang  

**一句话要点**：提出形态感知图强化学习框架，以解决张拉整体机器人运动控制问题

**关键词**：张拉整体机器人, 强化学习, 图神经网络, 运动控制, 策略迁移

## 3 点简述
- 张拉整体机器人因欠驱动和高度耦合动力学，面临运动控制挑战
- 集成图神经网络到SAC算法，利用物理拓扑图捕捉组件耦合
- 在物理机器人上验证，样本效率高、鲁棒性强，策略可直接迁移到硬件

## 摘要（原文）

> Tensegrity robots combine rigid rods and elastic cables, offering high
> resilience and deployability but posing major challenges for locomotion control
> due to their underactuated and highly coupled dynamics. This paper introduces a
> morphology-aware reinforcement learning framework that integrates a graph
> neural network (GNN) into the Soft Actor-Critic (SAC) algorithm. By
> representing the robot's physical topology as a graph, the proposed GNN-based
> policy captures coupling among components, enabling faster and more stable
> learning than conventional multilayer perceptron (MLP) policies. The method is
> validated on a physical 3-bar tensegrity robot across three locomotion
> primitives, including straight-line tracking and bidirectional turning. It
> shows superior sample efficiency, robustness to noise and stiffness variations,
> and improved trajectory accuracy. Notably, the learned policies transfer
> directly from simulation to hardware without fine-tuning, achieving stable
> real-world locomotion. These results demonstrate the advantages of
> incorporating structural priors into reinforcement learning for tensegrity
> robot control.

