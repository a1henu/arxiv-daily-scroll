---
layout: default
title: ManeuverNet: A Soft Actor-Critic Framework for Precise Maneuvering of Double-Ackermann-Steering Robots with Optimized Reward Functions
---

# ManeuverNet: A Soft Actor-Critic Framework for Precise Maneuvering of Double-Ackermann-Steering Robots with Optimized Reward Functions
**arXiv**：[2602.14726v1](https://arxiv.org/abs/2602.14726) · [PDF](https://arxiv.org/pdf/2602.14726.pdf)  
**作者**：Kohio Deflesselle, Mélodie Daniel, Aly Magassouba, Miguel Aranda, Olivier Ly  

**一句话要点**：提出ManeuverNet框架，结合Soft Actor-Critic与优化奖励函数，以解决双阿克曼转向机器人在农业场景中的精确操控问题。

**关键词**：双阿克曼转向机器人, 深度强化学习, Soft Actor-Critic, 奖励函数优化, 农业机器人, 精确操控

## 3 点简述
- 核心问题：双阿克曼转向机器人在有限空间内执行复杂机动时，传统方法参数敏感，而端到端深度强化学习方法因奖励函数不当导致性能不佳。
- 方法要点：基于Soft Actor-Critic与CrossQ的深度强化学习框架，设计四种专用奖励函数，无需专家数据或手工指导。
- 实验或效果：相比深度强化学习基线提升超40%成功率，降低传统规划器参数敏感性，真实试验中轨迹效率提升达90%。

## 摘要（原文）

> Autonomous control of double-Ackermann-steering robots is essential in agricultural applications, where robots must execute precise and complex maneuvers within a limited space. Classical methods, such as the Timed Elastic Band (TEB) planner, can address this problem, but they rely on parameter tuning, making them highly sensitive to changes in robot configuration or environment and impractical to deploy without constant recalibration. At the same time, end-to-end deep reinforcement learning (DRL) methods often fail due to unsuitable reward functions for non-holonomic constraints, resulting in sub-optimal policies and poor generalization. To address these challenges, this paper presents ManeuverNet, a DRL framework tailored for double-Ackermann systems, combining Soft Actor-Critic with CrossQ. Furthermore, ManeuverNet introduces four specifically designed reward functions to support maneuver learning. Unlike prior work, ManeuverNet does not depend on expert data or handcrafted guidance. We extensively evaluate ManeuverNet against both state-of-the-art DRL baselines and the TEB planner. Experimental results demonstrate that our framework substantially improves maneuverability and success rates, achieving more than a 40% gain over DRL baselines. Moreover, ManeuverNet effectively mitigates the strong parameter sensitivity observed in the TEB planner. In real-world trials, ManeuverNet achieved up to a 90% increase in maneuvering trajectory efficiency, highlighting its robustness and practical applicability.

