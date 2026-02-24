---
layout: default
title: To Move or Not to Move: Constraint-based Planning Enables Zero-Shot Generalization for Interactive Navigation
---

# To Move or Not to Move: Constraint-based Planning Enables Zero-Shot Generalization for Interactive Navigation
**arXiv**：[2602.20055v1](https://arxiv.org/abs/2602.20055) · [PDF](https://arxiv.org/pdf/2602.20055.pdf)  
**作者**：Apoorva Vashisth, Manav Kulshrestha, Pranav Bakshi, Damon Conover, Guillaume Sartoretti, Aniket Bera  

**一句话要点**：提出基于约束规划与主动感知的LLM框架，以解决机器人交互导航中路径被杂物阻塞的问题。

**关键词**：交互导航, 约束规划, 主动感知, 场景图推理, 机器人操作, 零样本泛化

## 3 点简述
- 核心问题：真实环境中杂物可能阻塞所有路径，需机器人移动杂物以完成顺序物体放置任务。
- 方法要点：利用LLM在结构化场景图上推理，结合主动感知决定移动对象、放置位置和探索区域。
- 实验或效果：在ProcTHOR-10k模拟器中优于基线，并在真实硬件上进行了定性演示。

## 摘要（原文）

> Visual navigation typically assumes the existence of at least one obstacle-free path between start and goal, which must be discovered/planned by the robot. However, in real-world scenarios, such as home environments and warehouses, clutter can block all routes. Targeted at such cases, we introduce the Lifelong Interactive Navigation problem, where a mobile robot with manipulation abilities can move clutter to forge its own path to complete sequential object- placement tasks - each involving placing an given object (eg. Alarm clock, Pillow) onto a target object (eg. Dining table, Desk, Bed). To address this lifelong setting - where effects of environment changes accumulate and have long-term effects - we propose an LLM-driven, constraint-based planning framework with active perception. Our framework allows the LLM to reason over a structured scene graph of discovered objects and obstacles, deciding which object to move, where to place it, and where to look next to discover task-relevant information. This coupling of reasoning and active perception allows the agent to explore the regions expected to contribute to task completion rather than exhaustively mapping the environment. A standard motion planner then executes the corresponding navigate-pick-place, or detour sequence, ensuring reliable low-level control. Evaluated in physics-enabled ProcTHOR-10k simulator, our approach outperforms non-learning and learning-based baselines. We further demonstrate our approach qualitatively on real-world hardware.

