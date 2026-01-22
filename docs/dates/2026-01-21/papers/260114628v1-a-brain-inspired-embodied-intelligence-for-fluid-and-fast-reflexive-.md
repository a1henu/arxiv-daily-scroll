---
layout: default
title: A Brain-inspired Embodied Intelligence for Fluid and Fast Reflexive Robotics Control
---

# A Brain-inspired Embodied Intelligence for Fluid and Fast Reflexive Robotics Control
**arXiv**：[2601.14628v1](https://arxiv.org/abs/2601.14628) · [PDF](https://arxiv.org/pdf/2601.14628.pdf)  
**作者**：Weiyu Guo, He Zhang, Pengteng Li, Tiefu Cai, Ziyang Chen, Yandong Guo, Xiao He, Yongkui Yang, Ying Sun, Hui Xiong  

**一句话要点**：提出神经形态视觉-语言-动作框架以解决机器人动态稳定性和快速反射控制问题

**关键词**：神经形态计算, 仿生机器人控制, 动态稳定性, 快速反射, 节能设计, 物理部署

## 3 点简述
- 当前机器人策略难以模拟生物运动的动态稳定性和快速反射响应
- 采用仿生系统设计，结合高层规划、小脑稳定和脊髓快速执行模块
- 在物理机器人上实现状态记忆、节能和毫秒级安全反射，无需额外数据

## 摘要（原文）

> Recent advances in embodied intelligence have leveraged massive scaling of data and model parameters to master natural-language command following and multi-task control. In contrast, biological systems demonstrate an innate ability to acquire skills rapidly from sparse experience. Crucially, current robotic policies struggle to replicate the dynamic stability, reflexive responsiveness, and temporal memory inherent in biological motion. Here we present Neuromorphic Vision-Language-Action (NeuroVLA), a framework that mimics the structural organization of the bio-nervous system between the cortex, cerebellum, and spinal cord. We adopt a system-level bio-inspired design: a high-level model plans goals, an adaptive cerebellum module stabilizes motion using high-frequency sensors feedback, and a bio-inspired spinal layer executes lightning-fast actions generation. NeuroVLA represents the first deployment of a neuromorphic VLA on physical robotics, achieving state-of-the-art performance. We observe the emergence of biological motor characteristics without additional data or special guidance: it stops the shaking in robotic arms, saves significant energy(only 0.4w on Neuromorphic Processor), shows temporal memory ability and triggers safety reflexes in less than 20 milliseconds.

