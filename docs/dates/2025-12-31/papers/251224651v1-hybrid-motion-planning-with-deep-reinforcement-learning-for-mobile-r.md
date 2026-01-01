---
layout: default
title: Hybrid Motion Planning with Deep Reinforcement Learning for Mobile Robot Navigation
---

# Hybrid Motion Planning with Deep Reinforcement Learning for Mobile Robot Navigation
**arXiv**：[2512.24651v1](https://arxiv.org/abs/2512.24651) · [PDF](https://arxiv.org/pdf/2512.24651.pdf)  
**作者**：Yury Kolomeytsev, Dmitry Golembiovsky  

**一句话要点**：提出HMP-DRL混合框架，以增强移动机器人在复杂动态环境中的导航安全与可靠性。

**关键词**：混合运动规划, 深度强化学习, 移动机器人导航, 实体感知奖励, 全局路径规划, 动态环境

## 3 点简述
- 核心问题：传统图规划器缺乏反应性，而DRL方法缺少全局上下文，导致导航在动态环境中效果受限。
- 方法要点：结合图规划器生成全局路径，通过检查点编码到DRL策略中，并采用基于语义的实体感知奖励结构。
- 实验或效果：在真实地图模拟环境中验证，HMP-DRL在成功率、碰撞率和到达时间上优于其他方法。

## 摘要（原文）

> Autonomous mobile robots operating in complex, dynamic environments face the dual challenge of navigating large-scale, structurally diverse spaces with static obstacles while safely interacting with various moving agents. Traditional graph-based planners excel at long-range pathfinding but lack reactivity, while Deep Reinforcement Learning (DRL) methods demonstrate strong collision avoidance but often fail to reach distant goals due to a lack of global context. We propose Hybrid Motion Planning with Deep Reinforcement Learning (HMP-DRL), a hybrid framework that bridges this gap. Our approach utilizes a graph-based global planner to generate a path, which is integrated into a local DRL policy via a sequence of checkpoints encoded in both the state space and reward function. To ensure social compliance, the local planner employs an entity-aware reward structure that dynamically adjusts safety margins and penalties based on the semantic type of surrounding agents. We validate the proposed method through extensive testing in a realistic simulation environment derived from real-world map data. Comprehensive experiments demonstrate that HMP-DRL consistently outperforms other methods, including state-of-the-art approaches, in terms of key metrics of robot navigation: success rate, collision rate, and time to reach the goal. Overall, these findings confirm that integrating long-term path guidance with semantically-aware local control significantly enhances both the safety and reliability of autonomous navigation in complex human-centric settings.

