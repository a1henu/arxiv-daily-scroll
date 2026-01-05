---
layout: default
title: LLM-Based Agentic Exploration for Robot Navigation & Manipulation with Skill Orchestration
---

# LLM-Based Agentic Exploration for Robot Navigation & Manipulation with Skill Orchestration
**arXiv**：[2601.00555v1](https://arxiv.org/abs/2601.00555) · [PDF](https://arxiv.org/pdf/2601.00555.pdf)  
**作者**：Abu Hanif Muhammad Syarubany, Farhan Zaki Rahmani, Trio Widianto  

**一句话要点**：提出基于LLM的智能体探索系统，用于室内购物场景的机器人导航与操作任务。

**关键词**：LLM智能体, 机器人导航, 语义建图, 技能协调, 室内购物任务, 端到端系统

## 3 点简述
- 核心问题：解决室内购物任务中机器人端到端探索与操作问题，需处理自然语言指令、语义建图和多技能协调。
- 方法要点：利用LLM生成离散动作决策，结合轻量级语义地图和模块化运动基元（如避障、AprilTag对齐）执行任务。
- 实验或效果：在Gazebo仿真和真实走廊布局中评估，系统能完成从用户指令到多店铺导航和物体抓取的端到端执行，保持模块化和可调试性。

## 摘要（原文）

> This paper presents an end-to-end LLM-based agentic exploration system for an indoor shopping task, evaluated in both Gazebo simulation and a corresponding real-world corridor layout. The robot incrementally builds a lightweight semantic map by detecting signboards at junctions and storing direction-to-POI relations together with estimated junction poses, while AprilTags provide repeatable anchors for approach and alignment. Given a natural-language shopping request, an LLM produces a constrained discrete action at each junction (direction and whether to enter a store), and a ROS finite-state main controller executes the decision by gating modular motion primitives, including local-costmap-based obstacle avoidance, AprilTag approaching, store entry, and grasping. Qualitative results show that the integrated stack can perform end-to-end task execution from user instruction to multi-store navigation and object retrieval, while remaining modular and debuggable through its text-based map and logged decision history.

