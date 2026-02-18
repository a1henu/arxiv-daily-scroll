---
layout: default
title: Dex4D: Task-Agnostic Point Track Policy for Sim-to-Real Dexterous Manipulation
---

# Dex4D: Task-Agnostic Point Track Policy for Sim-to-Real Dexterous Manipulation
**arXiv**：[2602.15828v1](https://arxiv.org/abs/2602.15828) · [PDF](https://arxiv.org/pdf/2602.15828.pdf)  
**作者**：Yuxuan Kuang, Sungjae Park, Katerina Fragkiadaki, Shubham Tulsiani  

**一句话要点**：提出Dex4D框架，通过任务无关点轨迹策略实现灵巧操作的仿真到现实零样本迁移

**关键词**：灵巧操作, 仿真到现实迁移, 点轨迹策略, 零样本学习, 任务无关技能

## 3 点简述
- 核心问题：灵巧操作中通用策略学习困难，仿真训练需任务特定设计，现实数据收集成本高
- 方法要点：训练任务无关的3D点轨迹条件策略，支持任意物体到任意姿态的零样本操作
- 实验或效果：在仿真和真实机器人上验证零样本部署，优于基线，泛化能力强

## 摘要（原文）

> Learning generalist policies capable of accomplishing a plethora of everyday tasks remains an open challenge in dexterous manipulation. In particular, collecting large-scale manipulation data via real-world teleoperation is expensive and difficult to scale. While learning in simulation provides a feasible alternative, designing multiple task-specific environments and rewards for training is similarly challenging. We propose Dex4D, a framework that instead leverages simulation for learning task-agnostic dexterous skills that can be flexibly recomposed to perform diverse real-world manipulation tasks. Specifically, Dex4D learns a domain-agnostic 3D point track conditioned policy capable of manipulating any object to any desired pose. We train this 'Anypose-to-Anypose' policy in simulation across thousands of objects with diverse pose configurations, covering a broad space of robot-object interactions that can be composed at test time. At deployment, this policy can be zero-shot transferred to real-world tasks without finetuning, simply by prompting it with desired object-centric point tracks extracted from generated videos. During execution, Dex4D uses online point tracking for closed-loop perception and control. Extensive experiments in simulation and on real robots show that our method enables zero-shot deployment for diverse dexterous manipulation tasks and yields consistent improvements over prior baselines. Furthermore, we demonstrate strong generalization to novel objects, scene layouts, backgrounds, and trajectories, highlighting the robustness and scalability of the proposed framework.

