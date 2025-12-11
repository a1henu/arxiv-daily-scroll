---
layout: default
title: Scene-agnostic Hierarchical Bimanual Task Planning via Visual Affordance Reasoning
---

# Scene-agnostic Hierarchical Bimanual Task Planning via Visual Affordance Reasoning
**arXiv**：[2512.09310v1](https://arxiv.org/abs/2512.09310) · [PDF](https://arxiv.org/pdf/2512.09310.pdf)  
**作者**：Kwang Bin Lee, Jiho Kang, Sung-Hee Lee  

**一句话要点**：提出场景无关的双臂任务规划框架，通过视觉可供性推理实现协调操作

**关键词**：双臂任务规划, 视觉可供性推理, 场景无关操作, 子目标规划, 协调动作

## 3 点简述
- 核心问题：现有机器人任务规划器多为单臂，难以处理场景无关双臂操作的空间、几何和协调挑战
- 方法要点：集成视觉点定位、双臂子目标规划和交互点驱动提示模块，实现语义推理与3D执行桥接
- 实验或效果：在杂乱未知场景中生成紧凑可行双臂计划，无需重训练，展示稳健场景泛化能力

## 摘要（原文）

> Embodied agents operating in open environments must translate high-level instructions into grounded, executable behaviors, often requiring coordinated use of both hands. While recent foundation models offer strong semantic reasoning, existing robotic task planners remain predominantly unimanual and fail to address the spatial, geometric, and coordination challenges inherent to bimanual manipulation in scene-agnostic settings. We present a unified framework for scene-agnostic bimanual task planning that bridges high-level reasoning with 3D-grounded two-handed execution. Our approach integrates three key modules. Visual Point Grounding (VPG) analyzes a single scene image to detect relevant objects and generate world-aligned interaction points. Bimanual Subgoal Planner (BSP) reasons over spatial adjacency and cross-object accessibility to produce compact, motion-neutralized subgoals that exploit opportunities for coordinated two-handed actions. Interaction-Point-Driven Bimanual Prompting (IPBP) binds these subgoals to a structured skill library, instantiating synchronized unimanual or bimanual action sequences that satisfy hand-state and affordance constraints. Together, these modules enable agents to plan semantically meaningful, physically feasible, and parallelizable two-handed behaviors in cluttered, previously unseen scenes. Experiments show that it produces coherent, feasible, and compact two-handed plans, and generalizes to cluttered scenes without retraining, demonstrating robust scene-agnostic affordance reasoning for bimanual tasks.

