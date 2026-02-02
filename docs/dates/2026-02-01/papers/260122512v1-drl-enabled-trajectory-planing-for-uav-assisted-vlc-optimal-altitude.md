---
layout: default
title: DRL-Enabled Trajectory Planing for UAV-Assisted VLC: Optimal Altitude and Reward Design
---

# DRL-Enabled Trajectory Planing for UAV-Assisted VLC: Optimal Altitude and Reward Design
**arXiv**：[2601.22512v1](https://arxiv.org/abs/2601.22512) · [PDF](https://arxiv.org/pdf/2601.22512.pdf)  
**作者**：Tian-Tian Lin, Yi Liu, Xiao-Wei Tang, Yunmei Shi, Yi Huang, Zhongxiang Wei, Qingqing Wu, Yuhan Dong  

**一句话要点**：提出基于DRL的UAV辅助VLC轨迹规划框架，优化飞行高度与奖励机制以提升数据收集效率。

**关键词**：无人机轨迹规划, 可见光通信, 深度强化学习, 优化算法, 数据收集

## 3 点简述
- 研究UAV辅助VLC系统中三维轨迹规划问题，目标是最小化飞行距离以最大化数据收集效率。
- 推导特定VLC信道增益阈值下的最优飞行高度闭式解，并设计信息素驱动奖励机制结合TD3算法优化水平轨迹。
- 仿真验证最优高度可减少飞行距离达35%，奖励机制缩短收敛步数约50%，显著提升效率。

## 摘要（原文）

> Recently, the integration of unmanned aerial vehicle (UAV) and visible light communication (VLC) technologies has emerged as a promising solution to offer flexible communication and efficient lighting. This letter investigates the three-dimensional trajectory planning in a UAV-assisted VLC system, where a UAV is dispatched to collect data from ground users (GUs). The core objective is to develop a trajectory planning framework that minimizes UAV flight distance, which is equivalent to maximizing the data collection efficiency. This issue is formulated as a challenging mixed-integer non-convex optimization problem. To tackle it, we first derive a closed-form optimal flight altitude under specific VLC channel gain threshold. Subsequently, we optimize the UAV horizontal trajectory by integrating a novel pheromone-driven reward mechanism with the twin delayed deep deterministic policy gradient algorithm, which enables adaptive UAV motion strategy in complex environments. Simulation results validate that the derived optimal altitude effectively reduces the flight distance by up to 35% compared to baseline methods. Additionally, the proposed reward mechanism significantly shortens the convergence steps by approximately 50%, demonstrating notable efficiency gains in the context of UAV-assisted VLC data collection.

