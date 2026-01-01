---
layout: default
title: RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dataset for Generalizable Embodied Intelligence
---

# RoboMIND 2.0: A Multimodal, Bimanual Mobile Manipulation Dataset for Generalizable Embodied Intelligence
**arXiv**：[2512.24653v1](https://arxiv.org/abs/2512.24653) · [PDF](https://arxiv.org/pdf/2512.24653.pdf)  
**作者**：Chengkai Hou, Kun Wu, Jiaming Liu, Zhengping Che, Di Wu, Fei Liao, Guangrun Li, Jingyang He, Qiuxuan Feng, Zhao Jin, Chenyang Gu, Zhuoyang Liu, Nuowei Han, Xiangju Mi, Yaoxu Lv, Yankai Fu, Gaole Dai, Langzhe Gu, Tao Li, Yuheng Zhang, Yixue Zhang, Xinhua Wang, Shichao Fan, Meng Li, Zhen Zhao, Ning Liu, Zhiyuan Xu, Pei Ren, Junjie Ji, Haonan Liu, Kuan Cheng, Shanghang Zhang, Jian Tang  

**一句话要点**：提出RoboMIND 2.0数据集和MIND-2系统，以解决机器人操作中数据稀缺和泛化能力不足的问题。

**关键词**：机器人操作数据集, 双手机器人操作, 移动操作, 离线强化学习, 仿真到真实迁移, 触觉增强

## 3 点简述
- 核心问题：当前机器人模仿学习受限于大规模真实世界演示数据稀缺，导致在长时程双手机器人操作和移动操作中泛化能力有限。
- 方法要点：发布RoboMIND 2.0数据集，包含超过310K双手机器人操作轨迹，并构建MIND-2系统，采用分层框架结合离线强化学习优化。
- 实验或效果：数据集涵盖多种机器人本体和复杂任务，包括触觉增强和移动操作轨迹，并提供了模拟数据集以支持仿真到真实的迁移。

## 摘要（原文）

> While data-driven imitation learning has revolutionized robotic manipulation, current approaches remain constrained by the scarcity of large-scale, diverse real-world demonstrations. Consequently, the ability of existing models to generalize across long-horizon bimanual tasks and mobile manipulation in unstructured environments remains limited. To bridge this gap, we present RoboMIND 2.0, a comprehensive real-world dataset comprising over 310K dual-arm manipulation trajectories collected across six distinct robot embodiments and 739 complex tasks. Crucially, to support research in contact-rich and spatially extended tasks, the dataset incorporates 12K tactile-enhanced episodes and 20K mobile manipulation trajectories. Complementing this physical data, we construct high-fidelity digital twins of our real-world environments, releasing an additional 20K-trajectory simulated dataset to facilitate robust sim-to-real transfer. To fully exploit the potential of RoboMIND 2.0, we propose MIND-2 system, a hierarchical dual-system frame-work optimized via offline reinforcement learning. MIND-2 integrates a high-level semantic planner (MIND-2-VLM) to decompose abstract natural language instructions into grounded subgoals, coupled with a low-level Vision-Language-Action executor (MIND-2-VLA), which generates precise, proprioception-aware motor actions.

