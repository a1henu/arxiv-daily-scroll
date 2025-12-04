---
layout: default
title: Autonomous Reinforcement Learning Robot Control with Intel's Loihi 2 Neuromorphic Hardware
---

# Autonomous Reinforcement Learning Robot Control with Intel's Loihi 2 Neuromorphic Hardware
**arXiv**：[2512.03911v1](https://arxiv.org/abs/2512.03911) · [PDF](https://arxiv.org/pdf/2512.03911.pdf)  
**作者**：Kenneth Stewart, Roxana Leontie, Samantha Chapin, Joe Hays, Sumit Bam Shrestha, Carl Glen Henshaw  

**一句话要点**：提出将强化学习ANN转换为SDNN以在Loihi 2上部署，实现机器人低延迟节能控制。

**关键词**：神经形态计算, 强化学习, 机器人控制, Sigma-Delta神经网络, Loihi 2硬件

## 3 点简述
- 核心问题：如何在神经形态硬件上部署强化学习策略以实现高效机器人控制。
- 方法要点：将基于ReLU的ANN转换为SDNN，适配Intel Loihi 2架构进行推理。
- 实验或效果：在Omniverse Isaac Lab中评估Astrobee机器人控制，比较GPU与Loihi 2性能。

## 摘要（原文）

> We present an end-to-end pipeline for deploying reinforcement learning (RL) trained Artificial Neural Networks (ANNs) on neuromorphic hardware by converting them into spiking Sigma-Delta Neural Networks (SDNNs). We demonstrate that an ANN policy trained entirely in simulation can be transformed into an SDNN compatible with Intel's Loihi 2 architecture, enabling low-latency and energy-efficient inference. As a test case, we use an RL policy for controlling the Astrobee free-flying robot, similar to a previously hardware in space-validated controller. The policy, trained with Rectified Linear Units (ReLUs), is converted to an SDNN and deployed on Intel's Loihi 2, then evaluated in NVIDIA's Omniverse Isaac Lab simulation environment for closed-loop control of Astrobee's motion. We compare execution performance between GPU and Loihi 2. The results highlight the feasibility of using neuromorphic platforms for robotic control and establish a pathway toward energy-efficient, real-time neuromorphic computation in future space and terrestrial robotics applications.

