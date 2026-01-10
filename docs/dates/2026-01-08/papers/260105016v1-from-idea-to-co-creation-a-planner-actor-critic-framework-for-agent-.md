---
layout: default
title: From Idea to Co-Creation: A Planner-Actor-Critic Framework for Agent Augmented 3D Modeling
---

# From Idea to Co-Creation: A Planner-Actor-Critic Framework for Agent Augmented 3D Modeling
**arXiv**：[2601.05016v1](https://arxiv.org/abs/2601.05016) · [PDF](https://arxiv.org/pdf/2601.05016.pdf)  
**作者**：Jin Gao, Saichandu Juluri  

**一句话要点**：提出Planner-Actor-Critic框架，通过多智能体自反思与人类监督提升3D建模质量与效率。

**关键词**：3D建模, 多智能体系统, 自反思学习, 人类在环监督, Planner-Actor-Critic架构, Blender集成

## 3 点简述
- 核心问题：现有单提示智能体在3D建模中易导致几何精度低、美学质量差和任务完成率不足。
- 方法要点：引入Planner协调步骤、Actor执行命令、Critic提供迭代反馈，结合人类监督与实时Blender同步。
- 实验或效果：相比单提示方法，在几何精度、美学质量和任务完成率上均有提升，减少建模错误并增加结果复杂度。

## 摘要（原文）

> We present a framework that extends the Actor-Critic architecture to creative 3D modeling through multi-agent self-reflection and human-in-the-loop supervision. While existing approaches rely on single-prompt agents that directly execute modeling commands via tools like Blender MCP, our approach introduces a Planner-Actor-Critic architecture. In this design, the Planner coordinates modeling steps, the Actor executes them, and the Critic provides iterative feedback, while human users act as supervisors and advisors throughout the process. Through systematic comparison between single-prompt modeling and our reflective multi-agent approach, we demonstrate improvements in geometric accuracy, aesthetic quality, and task completion rates across diverse 3D modeling scenarios. Our evaluation reveals that critic-guided reflection, combined with human supervisory input, reduces modeling errors and increases complexity and quality of the result compared to direct single-prompt execution. This work establishes that structured agent self-reflection, when augmented by human oversight and advisory guidance, produces higher-quality 3D models while maintaining efficient workflow integration through real-time Blender synchronization.

