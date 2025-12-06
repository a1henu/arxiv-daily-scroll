---
layout: default
title: Using Machine Learning to Take Stay-or-Go Decisions in Data-driven Drone Missions
---

# Using Machine Learning to Take Stay-or-Go Decisions in Data-driven Drone Missions
**arXiv**：[2512.04773v1](https://arxiv.org/abs/2512.04773) · [PDF](https://arxiv.org/pdf/2512.04773.pdf)  
**作者**：Giorgos Polychronis, Foivos Pournaropoulos, Christos D. Antonopoulos, Spyros Lalis  

**一句话要点**：提出基于分支预测和强化学习的机器学习方法，以优化数据驱动无人机任务中的停留或移动决策。

**关键词**：无人机任务优化, 机器学习决策, 分支预测, 强化学习, 实时数据处理, 事件概率评估

## 3 点简述
- 核心问题：无人机在数据驱动任务中需实时处理数据，决定是否停留执行额外行动，以避免无效等待或返航时间浪费。
- 方法要点：采用分支预测和强化学习等机器学习技术，动态评估事件发生概率，优化决策策略。
- 实验或效果：在事件概率随时间变化的多种场景下，方法显著优于现有回归方法，最坏任务时间提升达4.1倍，中位任务时间接近理想方法。

## 摘要（原文）

> Drones are becoming indispensable in many application domains. In data-driven missions, besides sensing, the drone must process the collected data at runtime to decide whether additional action must be taken on the spot, before moving to the next point of interest. If processing does not reveal an event or situation that requires such an action, the drone has waited in vain instead of moving to the next point. If, however, the drone starts moving to the next point and it turns out that a follow-up action is needed at the previous point, it must spend time to fly-back. To take this decision, we propose different machine-learning methods based on branch prediction and reinforcement learning. We evaluate these methods for a wide range of scenarios where the probability of event occurrence changes with time. Our results show that the proposed methods consistently outperform the regression-based method proposed in the literature and can significantly improve the worst-case mission time by up to 4.1x. Also, the achieved median mission time is very close, merely up to 2.7% higher, to that of a method with perfect knowledge of the current underlying event probability at each point of interest.

