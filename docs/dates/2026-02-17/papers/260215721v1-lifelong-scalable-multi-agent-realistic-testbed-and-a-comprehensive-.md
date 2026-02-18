---
layout: default
title: Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems
---

# Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems
**arXiv**：[2602.15721v1](https://arxiv.org/abs/2602.15721) · [PDF](https://arxiv.org/pdf/2602.15721.pdf)  
**作者**：Jingtian Yan, Yulun Zhang, Zhenting Liu, Han Zhang, He Jiang, Jingkai Chen, Stephen F. Smith, Jiaoyang Li  

**一句话要点**：提出LSMART开源模拟器，用于评估多智能体路径规划算法在终身AGV车队管理系统中的性能。

**关键词**：多智能体路径规划, 终身规划, AGV车队管理, 开源模拟器, 规划与执行并行

## 3 点简述
- 核心问题：终身MAPF在AGV车队管理系统中需处理规划与执行并行、规划器选择及故障恢复等设计挑战。
- 方法要点：扩展SMART模拟器，集成规划时机、规划方式和恢复机制，支持评估任何MAPF算法。
- 实验或效果：基于先进方法提供实验指导，帮助设计有效的终身AGV车队管理系统。

## 摘要（原文）

> We present Lifelong Scalable Multi-Agent Realistic Testbed (LSMART), an open-source simulator to evaluate any Multi-Agent Path Finding (MAPF) algorithm in a Fleet Management System (FMS) with Automated Guided Vehicles (AGVs). MAPF aims to move a group of agents from their corresponding starting locations to their goals. Lifelong MAPF (LMAPF) is a variant of MAPF that continuously assigns new goals for agents to reach. LMAPF applications, such as autonomous warehouses, often require a centralized, lifelong system to coordinate the movement of a fleet of robots, typically AGVs. However, existing works on MAPF and LMAPF often assume simplified kinodynamic models, such as pebble motion, as well as perfect execution and communication for AGVs. Prior work has presented SMART, a software capable of evaluating any MAPF algorithms while considering agent kinodynamics, communication delays, and execution uncertainties. However, SMART is designed for MAPF, not LMAPF. Generalizing SMART to an FMS requires many more design choices. First, an FMS parallelizes planning and execution, raising the question of when to plan. Second, given planners with varying optimality and differing agent-model assumptions, one must decide how to plan. Third, when the planner fails to return valid solutions, the system must determine how to recover. In this paper, we first present LSMART, an open-source simulator that incorporates all these considerations to evaluate any MAPF algorithms in an FMS. We then provide experiment results based on state-of-the-art methods for each design choice, offering guidance on how to effectively design centralized lifelong AGV Fleet Management Systems. LSMART is available at https://smart-mapf.github.io/lifelong-smart.

