---
layout: default
title: PUMA: Perception-driven Unified Foothold Prior for Mobility Augmented Quadruped Parkour
---

# PUMA: Perception-driven Unified Foothold Prior for Mobility Augmented Quadruped Parkour
**arXiv**：[2601.15995v1](https://arxiv.org/abs/2601.15995) · [PDF](https://arxiv.org/pdf/2601.15995.pdf)  
**作者**：Liang Wang, Kanzhong Yao, Yang Liu, Weikai Qin, Jun Wu, Zhe Sun, Qiuguo Zhu  

**一句话要点**：提出PUMA框架，集成视觉感知与立足点先验，以增强四足机器人在跑酷任务中的敏捷性。

**关键词**：四足机器人, 跑酷任务, 视觉感知, 立足点先验, 端到端学习, 强化学习

## 3 点简述
- 核心问题：现有方法依赖预计算立足点，限制四足机器人在复杂地形中的实时适应性和强化学习探索潜力。
- 方法要点：通过端到端学习框架，利用地形特征估计立足点先验，指导机器人主动调整姿态进行跑酷。
- 实验或效果：在仿真和真实环境中验证，PUMA在离散复杂地形中展现出优异的敏捷性和鲁棒性。

## 摘要（原文）

> Parkour tasks for quadrupeds have emerged as a promising benchmark for agile locomotion. While human athletes can effectively perceive environmental characteristics to select appropriate footholds for obstacle traversal, endowing legged robots with similar perceptual reasoning remains a significant challenge. Existing methods often rely on hierarchical controllers that follow pre-computed footholds, thereby constraining the robot's real-time adaptability and the exploratory potential of reinforcement learning. To overcome these challenges, we present PUMA, an end-to-end learning framework that integrates visual perception and foothold priors into a single-stage training process. This approach leverages terrain features to estimate egocentric polar foothold priors, composed of relative distance and heading, guiding the robot in active posture adaptation for parkour tasks. Extensive experiments conducted in simulation and real-world environments across various discrete complex terrains, demonstrate PUMA's exceptional agility and robustness in challenging scenarios.

