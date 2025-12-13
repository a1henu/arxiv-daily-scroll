---
layout: default
title: How to Brake? Ethical Emergency Braking with Deep Reinforcement Learning
---

# How to Brake? Ethical Emergency Braking with Deep Reinforcement Learning
**arXiv**：[2512.10698v1](https://arxiv.org/abs/2512.10698) · [PDF](https://arxiv.org/pdf/2512.10698.pdf)  
**作者**：Jianbo Wang, Galina Sidorenko, Johan Thunberg  

**一句话要点**：提出混合深度强化学习方法，以在紧急制动场景中实现多车辆伦理决策与整体伤害降低。

**关键词**：深度强化学习, 紧急制动, 多车辆跟随, 伦理决策, 车对车通信, 混合控制

## 3 点简述
- 研究多车辆跟随场景中，如何通过深度强化学习结合车对车通信，实现伦理紧急制动决策。
- 提出混合方法，结合深度强化学习与传统最优恒定减速度分析，提高系统可靠性与性能。
- 实验表明，该方法在整体伤害减少和碰撞避免方面优于单独深度强化学习，增强安全性。

## 摘要（原文）

> Connected and automated vehicles (CAVs) have the potential to enhance driving safety, for example by enabling safe vehicle following and more efficient traffic scheduling. For such future deployments, safety requirements should be addressed, where the primary such are avoidance of vehicle collisions and substantial mitigating of harm when collisions are unavoidable. However, conservative worst-case-based control strategies come at the price of reduced flexibility and may compromise overall performance. In light of this, we investigate how Deep Reinforcement Learning (DRL) can be leveraged to improve safety in multi-vehicle-following scenarios involving emergency braking. Specifically, we investigate how DRL with vehicle-to-vehicle communication can be used to ethically select an emergency breaking profile in scenarios where overall, or collective, three-vehicle harm reduction or collision avoidance shall be obtained instead of single-vehicle such. As an algorithm, we provide a hybrid approach that combines DRL with a previously published method based on analytical expressions for selecting optimal constant deceleration. By combining DRL with the previous method, the proposed hybrid approach increases the reliability compared to standalone DRL, while achieving superior performance in terms of overall harm reduction and collision avoidance.

