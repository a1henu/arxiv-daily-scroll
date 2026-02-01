---
layout: default
title: Towards Space-Based Environmentally-Adaptive Grasping
---

# Towards Space-Based Environmentally-Adaptive Grasping
**arXiv**：[2601.21394v1](https://arxiv.org/abs/2601.21394) · [PDF](https://arxiv.org/pdf/2601.21394.pdf)  
**作者**：Leonidas Askianakis, Aleksandr Artemov  

**一句话要点**：提出基于潜在流形的多模态融合方法，以提升空间环境下机器人抓取的适应性和样本效率。

**关键词**：机器人抓取, 潜在流形, 多模态融合, 强化学习, 空间环境, 样本效率

## 3 点简述
- 核心问题：非结构化环境中机器人抓取面临高维动作空间、稀疏奖励和泛化慢的挑战。
- 方法要点：在学习的潜在流形中融合多模态信息，使用SAC强化学习直接学习控制策略。
- 实验或效果：在GPU加速物理仿真中，单次抓取任务成功率超95%，收敛速度优于视觉基线。

## 摘要（原文）

> Robotic manipulation in unstructured environments requires reliable execution under diverse conditions, yet many state-of-the-art systems still struggle with high-dimensional action spaces, sparse rewards, and slow generalization beyond carefully curated training scenarios. We study these limitations through the example of grasping in space environments. We learn control policies directly in a learned latent manifold that fuses (grammarizes) multiple modalities into a structured representation for policy decision-making. Building on GPU-accelerated physics simulation, we instantiate a set of single-shot manipulation tasks and achieve over 95% task success with Soft Actor-Critic (SAC)-based reinforcement learning in less than 1M environment steps, under continuously varying grasping conditions from step 1. This empirically shows faster convergence than representative state-of-the-art visual baselines under the same open-loop single-shot conditions. Our analysis indicates that explicitly reasoning in latent space yields more sample-efficient learning and improved robustness to novel object and gripper geometries, environmental clutter, and sensor configurations compared to standard baselines. We identify remaining limitations and outline directions toward fully adaptive and generalizable grasping in the extreme conditions of space.

