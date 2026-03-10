---
layout: default
title: EquiBim: Learning Symmetry-Equivariant Policy for Bimanual Manipulation
---

# EquiBim: Learning Symmetry-Equivariant Policy for Bimanual Manipulation
**arXiv**：[2603.08541v1](https://arxiv.org/abs/2603.08541) · [PDF](https://arxiv.org/pdf/2603.08541.pdf)  
**作者**：Zhiyuan Zhang, Aditya Mohan, Seungho Han, Wan Shou, Dongyi Wang, Yu She  

**一句话要点**：提出EquiBim框架，通过对称等变性策略学习解决双手机器人操作中的行为不对称问题。

**关键词**：双手机器人操作, 对称等变性学习, 模仿学习, 机器人控制, 物理对称性, 策略学习

## 3 点简述
- 核心问题：现有机器人模仿学习方法未显式处理物理对称性，导致双手机器人在对称观察下行为不一致。
- 方法要点：将物理对称性建模为群作用，在训练中对策略预测施加等变性约束，框架模型无关且兼容多种观察和动作表示。
- 实验或效果：在仿真和真实双手机器人平台上验证，提升性能和鲁棒性，尤其在分布偏移下表现更优。

## 摘要（原文）

> Robotic imitation learning has achieved impressive success in learning complex manipulation behaviors from demonstrations. However, many existing robot learning methods do not explicitly account for the physical symmetries of robotic systems, often resulting in asymmetric or inconsistent behaviors under symmetric observations. This limitation is particularly pronounced in dual-arm manipulation, where bilateral symmetry is inherent to both the robot morphology and the structure of many tasks. In this paper, we introduce EquiBim, a symmetry-equivariant policy learning framework for bimanual manipulation that enforces bilateral equivariance between observations and actions during training. Our approach formulates physical symmetry as a group action on both observation and action spaces, and imposes an equivariance constraint on policy predictions under symmetric transformations. The framework is model-agnostic and can be seamlessly integrated into a wide range of imitation learning pipelines with diverse observation modalities and action representations, including point cloud-based and image-based policies, as well as both end-effector-space and joint-space parameterizations. We evaluate EquiBim on RoboTwin, a dual-arm robotic platform with symmetric kinematics, and evaluate it across diverse observation and action configurations in simulation. We further validate the approach on a real-world dual-arm system. Across both simulation and physical experiments, our method consistently improves performance and robustness under distribution shifts. These results suggest that explicitly enforcing physical symmetry provides a simple yet effective inductive bias for bimanual robot learning.

