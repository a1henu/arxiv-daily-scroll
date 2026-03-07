---
layout: default
title: Competitive Multi-Operator Reinforcement Learning for Joint Pricing and Fleet Rebalancing in AMoD Systems
---

# Competitive Multi-Operator Reinforcement Learning for Joint Pricing and Fleet Rebalancing in AMoD Systems
**arXiv**：[2603.05000v1](https://arxiv.org/abs/2603.05000) · [PDF](https://arxiv.org/pdf/2603.05000.pdf)  
**作者**：Emil Kragh Toft, Carolin Schmidt, Daniele Gammelli, Filipe Rodrigues  

**一句话要点**：提出多运营商强化学习框架，以解决竞争性AMoD系统中联合定价与车队再平衡问题。

**关键词**：自主按需出行系统, 多智能体强化学习, 竞争性定价, 车队再平衡, 离散选择理论, 市场动态

## 3 点简述
- 研究竞争性AMoD市场中多运营商通过定价和车队部署争夺乘客的核心问题。
- 集成离散选择理论，使乘客分配和需求竞争从效用最大化决策中内生涌现。
- 基于多城市真实数据实验，显示竞争降低价格并改变车队定位模式，学习策略稳健。

## 摘要（原文）

> Autonomous Mobility-on-Demand (AMoD) systems promise to revolutionize urban transportation by providing affordable on-demand services to meet growing travel demand. However, realistic AMoD markets will be competitive, with multiple operators competing for passengers through strategic pricing and fleet deployment. While reinforcement learning has shown promise in optimizing single-operator AMoD control, existing work fails to capture competitive market dynamics. We investigate the impact of competition on policy learning by introducing a multi-operator reinforcement learning framework where two operators simultaneously learn pricing and fleet rebalancing policies. By integrating discrete choice theory, we enable passenger allocation and demand competition to emerge endogenously from utility-maximizing decisions. Experiments using real-world data from multiple cities demonstrate that competition fundamentally alters learned behaviors, leading to lower prices and distinct fleet positioning patterns compared to monopolistic settings. Notably, we demonstrate that learning-based approaches are robust to the additional stochasticity of competition, with competitive agents successfully converging to effective policies while accounting for partially unobserved competitor strategies.

