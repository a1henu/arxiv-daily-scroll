---
layout: default
title: Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching
---

# Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching
**arXiv**：[2602.15827v1](https://arxiv.org/abs/2602.15827) · [PDF](https://arxiv.org/pdf/2602.15827.pdf)  
**作者**：Zhen Wu, Xiaoyu Huang, Lujie Yang, Yuanhang Zhang, Koushil Sreenath, Xi Chen, Pieter Abbeel, Rocky Duan, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, C. Karen Liu  

**一句话要点**：提出Perceptive Humanoid Parkour框架，通过运动匹配和强化学习实现人形机器人自主视觉感知跑酷

**关键词**：人形机器人跑酷, 运动匹配, 强化学习蒸馏, 视觉感知决策, 长时程技能组合, 动态运动控制

## 3 点简述
- 核心问题：人形机器人跑酷需兼顾动态运动表达、长时程技能组合和感知决策，现有方法难以实现。
- 方法要点：利用运动匹配组合人类技能轨迹，训练强化学习专家策略并蒸馏为基于深度的多技能策略。
- 实验或效果：在Unitree G1机器人上验证，能攀爬高达1.25米障碍并适应实时扰动，实现长时程多障碍自主穿越。

## 摘要（原文）

> While recent advances in humanoid locomotion have achieved stable walking on varied terrains, capturing the agility and adaptivity of highly dynamic human motions remains an open challenge. In particular, agile parkour in complex environments demands not only low-level robustness, but also human-like motion expressiveness, long-horizon skill composition, and perception-driven decision-making. In this paper, we present Perceptive Humanoid Parkour (PHP), a modular framework that enables humanoid robots to autonomously perform long-horizon, vision-based parkour across challenging obstacle courses. Our approach first leverages motion matching, formulated as nearest-neighbor search in a feature space, to compose retargeted atomic human skills into long-horizon kinematic trajectories. This framework enables the flexible composition and smooth transition of complex skill chains while preserving the elegance and fluidity of dynamic human motions. Next, we train motion-tracking reinforcement learning (RL) expert policies for these composed motions, and distill them into a single depth-based, multi-skill student policy, using a combination of DAgger and RL. Crucially, the combination of perception and skill composition enables autonomous, context-aware decision-making: using only onboard depth sensing and a discrete 2D velocity command, the robot selects and executes whether to step over, climb onto, vault or roll off obstacles of varying geometries and heights. We validate our framework with extensive real-world experiments on a Unitree G1 humanoid robot, demonstrating highly dynamic parkour skills such as climbing tall obstacles up to 1.25m (96% robot height), as well as long-horizon multi-obstacle traversal with closed-loop adaptation to real-time obstacle perturbations.

