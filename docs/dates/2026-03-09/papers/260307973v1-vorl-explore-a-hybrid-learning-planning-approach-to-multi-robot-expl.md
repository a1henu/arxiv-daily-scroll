---
layout: default
title: VORL-EXPLORE: A Hybrid Learning Planning Approach to Multi-Robot Exploration in Dynamic Environments
---

# VORL-EXPLORE: A Hybrid Learning Planning Approach to Multi-Robot Exploration in Dynamic Environments
**arXiv**：[2603.07973v1](https://arxiv.org/abs/2603.07973) · [PDF](https://arxiv.org/pdf/2603.07973.pdf)  
**作者**：Ning Liu, Sen Shen, Zheng Li, Sheng Liu, Dongkun Han, Shangke Lyu, Thomas Braunl  

**一句话要点**：提出VORL-EXPLORE混合学习规划框架，以解决动态环境中多机器人探索的瓶颈拥堵与冗余覆盖问题。

**关键词**：多机器人探索, 混合学习规划, 执行保真度, 动态环境, 自适应仲裁, 自监督校准

## 3 点简述
- 核心问题：传统分层探索在动态密集环境中因分配器缺乏执行难度感知，导致机器人拥堵、振荡重规划和冗余覆盖。
- 方法要点：通过执行保真度耦合任务分配与运动执行，结合Voronoi目标与自适应仲裁机制，平衡全局效率与局部安全。
- 实验或效果：在随机网格和Gazebo工厂场景中实现高成功率、短路径、低重叠和鲁棒避撞，支持在线自监督适应。

## 摘要（原文）

> Hierarchical multi-robot exploration commonly decouples frontier allocation from local navigation, which can make the system brittle in dense and dynamic environments. Because the allocator lacks direct awareness of execution difficulty, robots may cluster at bottlenecks, trigger oscillatory replanning, and generate redundant coverage. We propose VORL-EXPLORE, a hybrid learning and planning framework that addresses this limitation through execution fidelity, a shared estimate of local navigability that couples task allocation with motion execution. This fidelity signal is incorporated into a fidelity-coupled Voronoi objective with inter-robot repulsion to reduce contention before it emerges. It also drives a risk-aware adaptive arbitration mechanism between global A* guidance and a reactive reinforcement learning policy, balancing long-range efficiency with safe interaction in confined spaces. The framework further supports online self-supervised recalibration of the fidelity model using pseudo-labels derived from recent progress and safety outcomes, enabling adaptation to non-stationary obstacles without manual risk tuning. We evaluate this capability separately in a dedicated severe-traffic ablation. Extensive experiments in randomized grids and a Gazebo factory scenario show high success rates, shorter path length, lower overlap, and robust collision avoidance. The source code will be made publicly available upon acceptance.

