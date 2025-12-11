---
layout: default
title: Analyzing Planner Design Trade-offs for MAPF under Realistic Simulation
---

# Analyzing Planner Design Trade-offs for MAPF under Realistic Simulation
**arXiv**：[2512.09736v1](https://arxiv.org/abs/2512.09736) · [PDF](https://arxiv.org/pdf/2512.09736.pdf)  
**作者**：Jingtian Yan, Zhifei Li, William Kang, Stephen F. Smith, Jiaoyang Li  

**一句话要点**：分析现实仿真下MAPF规划器设计权衡，指导实际部署

**关键词**：多智能体路径规划, 现实仿真, 规划器设计, 运动学建模, 性能评估

## 3 点简述
- 核心问题：现有MAPF评估框架基于简化机器人模型，与实际性能存在差距
- 方法要点：利用SMART等框架，系统研究规划器设计选择对现实执行性能的影响
- 实验或效果：实证分析解最优性、运动学建模精度及其交互作用，揭示设计权衡

## 摘要（原文）

> Multi-Agent Path Finding (MAPF) algorithms are increasingly deployed in industrial warehouses and automated manufacturing facilities, where robots must operate reliably under real-world physical constraints. However, existing MAPF evaluation frameworks typically rely on simplified robot models, leaving a substantial gap between algorithmic benchmarks and practical performance. Recent frameworks such as SMART, incorporate kinodynamic modeling and offer the MAPF community a platform for large-scale, realistic evaluation. Building on this capability, this work investigates how key planner design choices influence performance under realistic execution settings. We systematically study three fundamental factors: (1) the relationship between solution optimality and execution performance, (2) the sensitivity of system performance to inaccuracies in kinodynamic modeling, and (3) the interaction between model accuracy and plan optimality. Empirically, we examine these factors to understand how these design choices affect performance in realistic scenarios. We highlight open challenges and research directions to steer the community toward practical, real-world deployment.

