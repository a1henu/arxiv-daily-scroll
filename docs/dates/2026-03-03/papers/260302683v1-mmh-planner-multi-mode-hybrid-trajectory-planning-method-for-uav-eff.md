---
layout: default
title: MMH-Planner: Multi-Mode Hybrid Trajectory Planning Method for UAV Efficient Flight Based on Real-Time Spatial Awareness
---

# MMH-Planner: Multi-Mode Hybrid Trajectory Planning Method for UAV Efficient Flight Based on Real-Time Spatial Awareness
**arXiv**：[2603.02683v1](https://arxiv.org/abs/2603.02683) · [PDF](https://arxiv.org/pdf/2603.02683.pdf)  
**作者**：Yinghao Zhao, Chenguang Dai, Liang Lyu, Zhenchao Zhang, Chaozhen Lan, Hong Xie  

**一句话要点**：提出基于实时空间感知的多模式混合轨迹规划方法，以提升无人机高效飞行性能。

**关键词**：无人机轨迹规划, 多模式混合规划, 实时空间感知, 惰性重规划, 高效飞行

## 3 点简述
- 核心问题：现有规划算法因策略不灵活和适应性弱，导致规划效率受限。
- 方法要点：引入目标导向空间感知，动态选择最优规划模型，并设计惰性重规划策略。
- 实验或效果：仿真和真实飞行实验验证，在规划迭代次数和计算成本上优于现有SOTA算法。

## 摘要（原文）

> Motion planning is a critical component of intelligent unmanned systems, enabling their complex autonomous operations. However, current planning algorithms still face limitations in planning efficiency due to inflexible strategies and weak adaptability. To address this, this paper proposes a multi-mode hybrid trajectory planning method for UAVs based on real-time environmental awareness, which dynamically selects the optimal planning model for high-quality trajectory generation in response to environmental changes. First, we introduce a goal-oriented spatial awareness method that rapidly assesses flight safety in the upcoming environments. Second, a multi-mode hybrid trajectory planning mechanism is proposed, which can enhance the planning efficiency by selecting the optimal planning model for trajectory generation based on prior spatial awareness. Finally, we design a lazy replanning strategy that triggers replanning only when necessary to reduce computational resource consumption while maintaining flight quality. To validate the performance of the proposed method, we conducted comprehensive comparative experiments in simulation environments. Results demonstrate that our approach outperforms existing state-of-the-art (SOTA) algorithms across multiple metrics, achieving the best performance particularly in terms of the average number of planning iterations and computational cost per iteration. Furthermore, the effectiveness of our approach is further verified through real-world flight experiments integrated with a self-developed intelligent UAV platform.

