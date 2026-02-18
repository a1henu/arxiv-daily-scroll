---
layout: default
title: Efficient Knowledge Transfer for Jump-Starting Control Policy Learning of Multirotors through Physics-Aware Neural Architectures
---

# Efficient Knowledge Transfer for Jump-Starting Control Policy Learning of Multirotors through Physics-Aware Neural Architectures
**arXiv**：[2602.15533v1](https://arxiv.org/abs/2602.15533) · [PDF](https://arxiv.org/pdf/2602.15533.pdf)  
**作者**：Welf Rehberg, Mihir Kulkarni, Philipp Weiss, Kostas Alexis  

**一句话要点**：提出基于物理感知神经架构的库初始化方案，以加速多旋翼控制策略学习

**关键词**：多旋翼控制, 强化学习, 知识迁移, 物理感知神经网络, 策略初始化, 控制分配网络

## 3 点简述
- 核心问题：机器人控制策略训练效率低，需跨配置知识迁移以加速学习。
- 方法要点：结合强化学习控制器和监督控制分配网络，利用策略评估相似性度量从库中选择初始化策略。
- 实验或效果：仿真与真实实验显示，平均节省73.5%环境交互，实现高效跨配置迁移。

## 摘要（原文）

> Efficiently training control policies for robots is a major challenge that can greatly benefit from utilizing knowledge gained from training similar systems through cross-embodiment knowledge transfer. In this work, we focus on accelerating policy training using a library-based initialization scheme that enables effective knowledge transfer across multirotor configurations. By leveraging a physics-aware neural control architecture that combines a reinforcement learning-based controller and a supervised control allocation network, we enable the reuse of previously trained policies. To this end, we utilize a policy evaluation-based similarity measure that identifies suitable policies for initialization from a library. We demonstrate that this measure correlates with the reduction in environment interactions needed to reach target performance and is therefore suited for initialization. Extensive simulation and real-world experiments confirm that our control architecture achieves state-of-the-art control performance, and that our initialization scheme saves on average up to $73.5\%$ of environment interactions (compared to training a policy from scratch) across diverse quadrotor and hexarotor designs, paving the way for efficient cross-embodiment transfer in reinforcement learning.

