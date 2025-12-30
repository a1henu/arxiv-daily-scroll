---
layout: default
title: A Human-Oriented Cooperative Driving Approach: Integrating Driving Intention, State, and Conflict
---

# A Human-Oriented Cooperative Driving Approach: Integrating Driving Intention, State, and Conflict
**arXiv**：[2512.23220v1](https://arxiv.org/abs/2512.23220) · [PDF](https://arxiv.org/pdf/2512.23220.pdf)  
**作者**：Qin Wang, Shanmin Pang, Jianwu Fang, Shengye Dong, Fuhao Liu, Jianru Xue, Chen Lv  

**一句话要点**：提出人机协同驾驶方法，通过意图一致性和状态自适应分配减少冲突

**关键词**：人机协同驾驶, 意图感知规划, 控制权分配, 强化学习, 驾驶冲突缓解

## 3 点简述
- 核心问题：人机协同驾驶中意图与状态不匹配导致冲突，影响驾驶灵活性和信任
- 方法要点：战术层基于意图一致性成本规划轨迹，操作层用强化学习优化控制权分配策略
- 实验或效果：仿真和人在环实验显示方法提升驾驶性能，显著缓解人机冲突

## 摘要（原文）

> Human-vehicle cooperative driving serves as a vital bridge to fully autonomous driving by improving driving flexibility and gradually building driver trust and acceptance of autonomous technology. To establish more natural and effective human-vehicle interaction, we propose a Human-Oriented Cooperative Driving (HOCD) approach that primarily minimizes human-machine conflict by prioritizing driver intention and state. In implementation, we take both tactical and operational levels into account to ensure seamless human-vehicle cooperation. At the tactical level, we design an intention-aware trajectory planning method, using intention consistency cost as the core metric to evaluate the trajectory and align it with driver intention. At the operational level, we develop a control authority allocation strategy based on reinforcement learning, optimizing the policy through a designed reward function to achieve consistency between driver state and authority allocation. The results of simulation and human-in-the-loop experiments demonstrate that our proposed approach not only aligns with driver intention in trajectory planning but also ensures a reasonable authority allocation. Compared to other cooperative driving approaches, the proposed HOCD approach significantly enhances driving performance and mitigates human-machine conflict.The code is available at https://github.com/i-Qin/HOCD.

