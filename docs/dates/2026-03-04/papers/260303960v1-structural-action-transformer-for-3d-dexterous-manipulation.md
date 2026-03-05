---
layout: default
title: Structural Action Transformer for 3D Dexterous Manipulation
---

# Structural Action Transformer for 3D Dexterous Manipulation
**arXiv**：[2603.03960v1](https://arxiv.org/abs/2603.03960) · [PDF](https://arxiv.org/pdf/2603.03960.pdf)  
**作者**：Xiaohan Lei, Min Wang, Bohong Weng, Wengang Zhou, Houqiang Li  

**一句话要点**：提出结构动作Transformer以解决异构机器人3D灵巧操作中的跨具身技能迁移问题

**关键词**：3D灵巧操作, 跨具身技能迁移, 结构动作Transformer, 异构机器人, 连续时间流匹配, 具身关节码本

## 3 点简述
- 核心问题：异构数据集下高自由度机器人手的跨具身技能迁移困难，现有方法难以处理3D空间关系和具身异构性
- 方法要点：将动作块重构为无序的关节轨迹序列，引入具身关节码本编码功能角色和运动属性，通过连续时间流匹配从3D点云生成轨迹
- 实验或效果：在大规模异构数据集上预训练并在仿真与真实任务中微调，性能超越基线，样本效率高且跨具身迁移有效

## 摘要（原文）

> Achieving human-level dexterity in robots via imitation learning from heterogeneous datasets is hindered by the challenge of cross-embodiment skill transfer, particularly for high-DoF robotic hands. Existing methods, often relying on 2D observations and temporal-centric action representation, struggle to capture 3D spatial relations and fail to handle embodiment heterogeneity. This paper proposes the Structural Action Transformer (SAT), a new 3D dexterous manipulation policy that challenges this paradigm by introducing a structural-centric perspective. We reframe each action chunk not as a temporal sequence, but as a variable-length, unordered sequence of joint-wise trajectories. This structural formulation allows a Transformer to natively handle heterogeneous embodiments, treating the joint count as a variable sequence length. To encode structural priors and resolve ambiguity, we introduce an Embodied Joint Codebook that embeds each joint's functional role and kinematic properties. Our model learns to generate these trajectories from 3D point clouds via a continuous-time flow matching objective. We validate our approach by pre-training on large-scale heterogeneous datasets and fine-tuning on simulation and real-world dexterous manipulation tasks. Our method consistently outperforms all baselines, demonstrating superior sample efficiency and effective cross-embodiment skill transfer. This structural-centric representation offers a new path toward scaling policies for high-DoF, heterogeneous manipulators.

