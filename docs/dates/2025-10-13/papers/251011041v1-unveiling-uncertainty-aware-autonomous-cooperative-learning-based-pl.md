---
layout: default
title: Unveiling Uncertainty-Aware Autonomous Cooperative Learning Based Planning Strategy
---

# Unveiling Uncertainty-Aware Autonomous Cooperative Learning Based Planning Strategy
**arXiv**：[2510.11041v1](https://arxiv.org/abs/2510.11041) · [PDF](https://arxiv.org/pdf/2510.11041.pdf)  
**作者**：Shiyao Zhang, Liwei Deng, Shuyu Zhang, Weijie Yuan, Hong Zhang  

**一句话要点**：提出基于深度强化学习的自主协同规划框架以解决多车辆交互中的不确定性

**关键词**：自主协同规划, 深度强化学习, 不确定性处理, 软演员-评论者算法, 门控循环单元, CARLA仿真

## 3 点简述
- 核心问题：现有自主协同规划策略无法充分处理感知、规划和通信中的多种不确定性
- 方法要点：采用软演员-评论者算法结合门控循环单元学习时变动作，应对不完美状态信息
- 实验或效果：在CARLA仿真平台验证，优于基线方法，有效提升协同规划性能

## 摘要（原文）

> In future intelligent transportation systems, autonomous cooperative planning
> (ACP), becomes a promising technique to increase the effectiveness and security
> of multi-vehicle interactions. However, multiple uncertainties cannot be fully
> addressed for existing ACP strategies, e.g. perception, planning, and
> communication uncertainties. To address these, a novel deep reinforcement
> learning-based autonomous cooperative planning (DRLACP) framework is proposed
> to tackle various uncertainties on cooperative motion planning schemes.
> Specifically, the soft actor-critic (SAC) with the implementation of gate
> recurrent units (GRUs) is adopted to learn the deterministic optimal
> time-varying actions with imperfect state information occurred by planning,
> communication, and perception uncertainties. In addition, the real-time actions
> of autonomous vehicles (AVs) are demonstrated via the Car Learning to Act
> (CARLA) simulation platform. Evaluation results show that the proposed DRLACP
> learns and performs cooperative planning effectively, which outperforms other
> baseline methods under different scenarios with imperfect AV state information.

