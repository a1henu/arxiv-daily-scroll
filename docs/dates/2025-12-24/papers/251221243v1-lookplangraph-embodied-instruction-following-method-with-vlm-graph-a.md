---
layout: default
title: LookPlanGraph: Embodied Instruction Following Method with VLM Graph Augmentation
---

# LookPlanGraph: Embodied Instruction Following Method with VLM Graph Augmentation
**arXiv**：[2512.21243v1](https://arxiv.org/abs/2512.21243) · [PDF](https://arxiv.org/pdf/2512.21243.pdf)  
**作者**：Anatoly O. Onishchenko, Alexey K. Kovalev, Aleksandr I. Panov  

**一句话要点**：提出LookPlanGraph方法，通过VLM增强场景图以解决具身指令跟随中环境动态变化问题。

**关键词**：具身指令跟随, 场景图增强, 视觉语言模型, 动态环境处理, 机器人规划

## 3 点简述
- 核心问题：现有方法依赖预建静态场景图，无法处理环境在规划与执行间的变化。
- 方法要点：结合静态资产和对象先验构建场景图，执行时用VLM处理视角持续更新图，验证或发现对象。
- 实验或效果：在VirtualHome和OmniGibson模拟环境中测试，优于静态图方法，并展示真实世界应用。

## 摘要（原文）

> Methods that use Large Language Models (LLM) as planners for embodied instruction following tasks have become widespread. To successfully complete tasks, the LLM must be grounded in the environment in which the robot operates. One solution is to use a scene graph that contains all the necessary information. Modern methods rely on prebuilt scene graphs and assume that all task-relevant information is available at the start of planning. However, these approaches do not account for changes in the environment that may occur between the graph construction and the task execution. We propose LookPlanGraph - a method that leverages a scene graph composed of static assets and object priors. During plan execution, LookPlanGraph continuously updates the graph with relevant objects, either by verifying existing priors or discovering new entities. This is achieved by processing the agents egocentric camera view using a Vision Language Model. We conducted experiments with changed object positions VirtualHome and OmniGibson simulated environments, demonstrating that LookPlanGraph outperforms methods based on predefined static scene graphs. To demonstrate the practical applicability of our approach, we also conducted experiments in a real-world setting. Additionally, we introduce the GraSIF (Graph Scenes for Instruction Following) dataset with automated validation framework, comprising 514 tasks drawn from SayPlan Office, BEHAVIOR-1K, and VirtualHome RobotHow. Project page available at https://lookplangraph.github.io .

