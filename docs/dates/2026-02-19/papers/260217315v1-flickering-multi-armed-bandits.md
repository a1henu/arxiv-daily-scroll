---
layout: default
title: Flickering Multi-Armed Bandits
---

# Flickering Multi-Armed Bandits
**arXiv**：[2602.17315v1](https://arxiv.org/abs/2602.17315) · [PDF](https://arxiv.org/pdf/2602.17315.pdf)  
**作者**：Sourav Chakraborty, Amit Kiran Rege, Claire Monteleoni, Lijun Chen  

**一句话要点**：提出闪烁多臂老虎机框架，解决局部移动约束下最优臂识别问题。

**关键词**：多臂老虎机, 随机图过程, 局部移动约束, 亚线性遗憾, 机器人侦察

## 3 点简述
- 核心问题：可用臂集随时间变化且依赖历史选择，建模为随机图过程。
- 方法要点：采用两阶段算法，结合懒惰随机游走探索与导航利用。
- 实验或效果：理论证明亚线性遗憾界，数值模拟验证机器人侦察场景。

## 摘要（原文）

> We introduce Flickering Multi-Armed Bandits (FMAB), a new MAB framework where the set of available arms (or actions) can change at each round, and the available set at any time may depend on the agent's previously selected arm. We model this constrained, evolving availability using random graph processes, where arms are nodes and the agent's movement is restricted to its local neighborhood. We analyze this problem under two random graph models: an i.i.d. Erdős--Rényi (ER) process and an Edge-Markovian process. We propose and analyze a two-phase algorithm that employs a lazy random walk for exploration to efficiently identify the optimal arm, followed by a navigation and commitment phase for exploitation. We establish high-probability and expected sublinear regret bounds for both graph settings. We show that the exploration cost of our algorithm is near-optimal by establishing a matching information-theoretic lower bound for this problem class, highlighting the fundamental cost of exploration under local-move constraints. We complement our theoretical guarantees with numerical simulations, including a scenario of a robotic ground vehicle scouting a disaster-affected region.

