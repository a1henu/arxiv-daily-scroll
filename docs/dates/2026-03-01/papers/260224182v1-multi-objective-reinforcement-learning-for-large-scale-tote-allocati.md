---
layout: default
title: Multi-Objective Reinforcement Learning for Large-Scale Tote Allocation in Human-Robot Collaborative Fulfillment Centers
---

# Multi-Objective Reinforcement Learning for Large-Scale Tote Allocation in Human-Robot Collaborative Fulfillment Centers
**arXiv**：[2602.24182v1](https://arxiv.org/abs/2602.24182) · [PDF](https://arxiv.org/pdf/2602.24182.pdf)  
**作者**：Sikata Sengupta, Guangyi Liu, Omer Gottesman, Joseph W Durham, Michael Kearns, Aaron Roth, Michael Caldara  

**一句话要点**：提出基于零和博弈的多目标强化学习方法，以优化人机协作履行中心的容器分配问题。

**关键词**：多目标强化学习, 人机协作, 履行中心优化, 零和博弈, 约束强化学习, 最小最大策略

## 3 点简述
- 核心问题：在履行中心中平衡处理速度、资源使用和空间利用等多目标，同时满足现实操作约束。
- 方法要点：利用零和博弈中的最优响应和无悔动态，学习最小最大策略以处理高维状态和动态行为。
- 实验或效果：在模拟仓库中评估策略，有效权衡目标并满足所有约束，理论框架处理误差抵消问题。

## 摘要（原文）

> Optimizing the consolidation process in container-based fulfillment centers requires trading off competing objectives such as processing speed, resource usage, and space utilization while adhering to a range of real-world operational constraints. This process involves moving items between containers via a combination of human and robotic workstations to free up space for inbound inventory and increase container utilization. We formulate this problem as a large-scale Multi-Objective Reinforcement Learning (MORL) task with high-dimensional state spaces and dynamic system behavior. Our method builds on recent theoretical advances in solving constrained RL problems via best-response and no-regret dynamics in zero-sum games, enabling principled minimax policy learning. Policy evaluation on realistic warehouse simulations shows that our approach effectively trades off objectives, and we empirically observe that it learns a single policy that simultaneously satisfies all constraints, even if this is not theoretically guaranteed. We further introduce a theoretical framework to handle the problem of error cancellation, where time-averaged solutions display oscillatory behavior. This method returns a single iterate whose Lagrangian value is close to the minimax value of the game. These results demonstrate the promise of MORL in solving complex, high-impact decision-making problems in large-scale industrial systems.

