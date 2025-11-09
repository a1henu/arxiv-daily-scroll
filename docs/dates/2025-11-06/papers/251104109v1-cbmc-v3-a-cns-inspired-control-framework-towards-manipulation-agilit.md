---
layout: default
title: CBMC-V3: A CNS-inspired Control Framework Towards Manipulation Agility with SNN
---

# CBMC-V3: A CNS-inspired Control Framework Towards Manipulation Agility with SNN
**arXiv**：[2511.04109v1](https://arxiv.org/abs/2511.04109) · [PDF](https://arxiv.org/pdf/2511.04109.pdf)  
**作者**：Yanbo Pang, Qingkai Li, Mingguo Zhao  

**一句话要点**：提出基于SNN的仿CNS控制框架以提升机械臂在复杂环境中的敏捷操控

**关键词**：脉冲神经网络, 仿生控制, 机械臂操控, 中枢神经系统, 强化学习, 反馈控制

## 3 点简述
- 现有控制算法难以应对动态轨迹和不可预测交互的复杂环境
- 框架采用SNN实现五个CNS模块和三层控制层次，实现反馈与学习
- 仿真与真实平台验证显示优于工业级位置控制的敏捷性

## 摘要（原文）

> As robotic arm applications extend beyond industrial settings into
> healthcare, service, and daily life, existing control algorithms struggle to
> achieve the agile manipulation required for complex environments with dynamic
> trajectories, unpredictable interactions, and diverse objects. This paper
> presents a biomimetic control framework based on Spiking Neural Networks (SNN),
> inspired by the human Central Nervous System (CNS), to achieve agile control in
> such environments. The proposed framework features five control modules
> (cerebral cortex, cerebellum, thalamus, brainstem, spinal cord), three
> hierarchical control levels (first-order, second-order, third-order), and two
> information pathways (ascending, descending). Each module is fully implemented
> using SNN. The spinal cord module uses spike encoding and Leaky
> Integrate-and-Fire (LIF) neurons for feedback control. The brainstem module
> employs a network of LIF and non-spiking LIF neurons to dynamically adjust
> spinal cord parameters via reinforcement learning. The thalamus module
> similarly adjusts the cerebellum's torque outputs. The cerebellum module uses a
> recurrent SNN to learn the robotic arm's dynamics through regression, providing
> feedforward gravity compensation torques. The framework is validated both in
> simulation and on real-world robotic arm platform under various loads and
> trajectories. Results demonstrate that our method outperforms the
> industrial-grade position control in manipulation agility.

