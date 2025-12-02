---
layout: default
title: End-to-end Deep Reinforcement Learning for Stochastic Multi-objective Optimization in C-VRPTW
---

# End-to-end Deep Reinforcement Learning for Stochastic Multi-objective Optimization in C-VRPTW
**arXiv**：[2512.01518v1](https://arxiv.org/abs/2512.01518) · [PDF](https://arxiv.org/pdf/2512.01518.pdf)  
**作者**：Abdo Abouelrous, Laurens Bliek, Yaoxin Wu, Yingqian Zhang  

**一句话要点**：提出端到端深度强化学习模型，解决带时间窗的随机多目标车辆路径问题

**关键词**：车辆路径问题, 深度强化学习, 多目标优化, 随机优化, 注意力机制, 帕累托前沿

## 3 点简述
- 核心问题：车辆路径问题中旅行时间不确定性与多目标（总旅行时间和路线完工时间）冲突的联合优化。
- 方法要点：基于注意力机制和端到端深度强化学习，通过场景聚类训练机制处理随机性和多目标性。
- 实验或效果：模型能在可接受运行时间内构建高质量帕累托前沿，优于三个基线方法。

## 摘要（原文）

> In this work, we consider learning-based applications in routing to solve a Vehicle Routing variant characterized by stochasticity and multiple objectives. Such problems are representative of practical settings where decision-makers have to deal with uncertainty in the operational environment as well as multiple conflicting objectives due to different stakeholders. We specifically consider travel time uncertainty. We also consider two objectives, total travel time and route makespan, that jointly target operational efficiency and labor regulations on shift length, although different objectives could be incorporated. Learning-based methods offer earnest computational advantages as they can repeatedly solve problems with limited interference from the decision-maker. We specifically focus on end-to-end deep learning models that leverage the attention mechanism and multiple solution trajectories. These models have seen several successful applications in routing problems. However, since travel times are not a direct input to these models due to the large dimensions of the travel time matrix, accounting for uncertainty is a challenge, especially in the presence of multiple objectives. In turn, we propose a model that simultaneously addresses stochasticity and multi-objectivity and provide a refined training mechanism for this model through scenario clustering to reduce training time. Our results show that our model is capable of constructing a Pareto Front of good quality within acceptable run times compared to three baselines.

