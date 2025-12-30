---
layout: default
title: Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation
---

# Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation
**arXiv**：[2512.23703v1](https://arxiv.org/abs/2512.23703) · [PDF](https://arxiv.org/pdf/2512.23703.pdf)  
**作者**：Huajie Tan, Sixiang Chen, Yijie Xu, Zixiao Wang, Yuheng Ji, Cheng Chi, Yaoxu Lyu, Zhongxia Zhao, Xiansheng Chen, Peterson Co, Shaoxuan Xie, Guocai Yao, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang  

**一句话要点**：提出Dopamine-Reward方法，通过多视角感知和理论可靠奖励塑造解决机器人精细操作中的奖励建模难题

**关键词**：机器人操作, 过程奖励建模, 多视角感知, 奖励塑造, 强化学习, 通用奖励模型

## 3 点简述
- 核心问题：传统过程奖励模型缺乏步骤感知能力和单视角限制，导致精细操作评估不可靠
- 方法要点：引入通用奖励模型，采用步骤奖励离散化和多视角奖励融合技术
- 实验效果：在3400+小时数据上训练，单次适应新任务后仅需150次在线交互达到95%成功率

## 摘要（原文）

> The primary obstacle for applying reinforcement learning (RL) to real-world robotics is the design of effective reward functions. While recently learning-based Process Reward Models (PRMs) are a promising direction, they are often hindered by two fundamental limitations: their reward models lack step-aware understanding and rely on single-view perception, leading to unreliable assessments of fine-grained manipulation progress; and their reward shaping procedures are theoretically unsound, often inducing a semantic trap that misguides policy optimization. To address these, we introduce Dopamine-Reward, a novel reward modeling method for learning a general-purpose, step-aware process reward model from multi-view inputs. At its core is our General Reward Model (GRM), trained on a vast 3,400+ hour dataset, which leverages Step-wise Reward Discretization for structural understanding and Multi-Perspective Reward Fusion to overcome perceptual limitations. Building upon Dopamine-Reward, we propose Dopamine-RL, a robust policy learning framework that employs a theoretically-sound Policy-Invariant Reward Shaping method, which enables the agent to leverage dense rewards for efficient self-improvement without altering the optimal policy, thereby fundamentally avoiding the semantic trap. Extensive experiments across diverse simulated and real-world tasks validate our approach. GRM achieves state-of-the-art accuracy in reward assessment, and Dopamine-RL built on GRM significantly improves policy learning efficiency. For instance, after GRM is adapted to a new task in a one-shot manner from a single expert trajectory, the resulting reward model enables Dopamine-RL to improve the policy from near-zero to 95% success with only 150 online rollouts (approximately 1 hour of real robot interaction), while retaining strong generalization across tasks. Project website: https://robo-dopamine.github.io

