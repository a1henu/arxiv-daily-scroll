---
layout: default
title: AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding
---

# AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding
**arXiv**：[2601.08485v1](https://arxiv.org/abs/2601.08485) · [PDF](https://arxiv.org/pdf/2601.08485.pdf)  
**作者**：Chong Zhang, Victor Klemm, Fan Yang, Marco Hutter  

**一句话要点**：提出AME-2框架，通过注意力地图编码实现敏捷通用腿式运动

**关键词**：腿式机器人, 强化学习, 注意力机制, 地图编码, 不确定性感知, 敏捷运动

## 3 点简述
- 核心问题：现有方法在敏捷性与通用性间存在权衡，且难以处理视觉遮挡和稀疏立足点
- 方法要点：引入注意力地图编码器提取局部全局特征，结合基于学习的快速不确定性感知地图生成
- 实验或效果：在四足和双足机器人上验证，控制器在仿真和真实环境中展现强敏捷性和泛化能力

## 摘要（原文）

> Achieving agile and generalized legged locomotion across terrains requires tight integration of perception and control, especially under occlusions and sparse footholds. Existing methods have demonstrated agility on parkour courses but often rely on end-to-end sensorimotor models with limited generalization and interpretability. By contrast, methods targeting generalized locomotion typically exhibit limited agility and struggle with visual occlusions. We introduce AME-2, a unified reinforcement learning (RL) framework for agile and generalized locomotion that incorporates a novel attention-based map encoder in the control policy. This encoder extracts local and global mapping features and uses attention mechanisms to focus on salient regions, producing an interpretable and generalized embedding for RL-based control. We further propose a learning-based mapping pipeline that provides fast, uncertainty-aware terrain representations robust to noise and occlusions, serving as policy inputs. It uses neural networks to convert depth observations into local elevations with uncertainties, and fuses them with odometry. The pipeline also integrates with parallel simulation so that we can train controllers with online mapping, aiding sim-to-real transfer. We validate AME-2 with the proposed mapping pipeline on a quadruped and a biped robot, and the resulting controllers demonstrate strong agility and generalization to unseen terrains in simulation and in real-world experiments.

