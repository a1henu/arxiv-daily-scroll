---
layout: default
title: Retrieval-Augmented Robots via Retrieve-Reason-Act
---

# Retrieval-Augmented Robots via Retrieve-Reason-Act
**arXiv**：[2603.02688v1](https://arxiv.org/abs/2603.02688) · [PDF](https://arxiv.org/pdf/2603.02688.pdf)  
**作者**：Izat Temiraliev, Diji Yang, Yi Zhang  

**一句话要点**：提出检索增强机器人范式，通过检索-推理-执行循环解决零样本任务中的信息缺失问题。

**关键词**：检索增强机器人, 零样本任务执行, 跨模态对齐, 长视野组装, 非结构化文档检索

## 3 点简述
- 核心问题：机器人在零样本设置下缺乏外部程序知识，无法完成复杂任务。
- 方法要点：引入检索增强机器人范式，从非结构化文档中检索视觉手册并跨模态对齐以生成可执行计划。
- 实验或效果：在长视野组装基准上验证，性能优于零样本推理或少量示例检索基线。

## 摘要（原文）

> To achieve general-purpose utility, we argue that robots must evolve from passive executors into active Information Retrieval users. In strictly zero-shot settings where no prior demonstrations exist, robots face a critical information gap, such as the exact sequence required to assemble a complex furniture kit, that cannot be satisfied by internal parametric knowledge (common sense) or past internal memory. While recent robotic works attempt to use search before action, they primarily focus on retrieving past kinematic trajectories (analogous to searching internal memory) or text-based safety rules (searching for constraints). These approaches fail to address the core information need of active task construction: acquiring unseen procedural knowledge from external, unstructured documentation. In this paper, we define the paradigm as Retrieval-Augmented Robotics (RAR), empowering the robot with the information-seeking capability that bridges the gap between visual documentation and physical actuation. We formulate the task execution as an iterative Retrieve-Reason-Act loop: the robot or embodied agent actively retrieves relevant visual procedural manuals from an unstructured corpus, grounds the abstract 2D diagrams to 3D physical parts via cross-modal alignment, and synthesizes executable plans. We validate this paradigm on a challenging long-horizon assembly benchmark. Our experiments demonstrate that grounding robotic planning in retrieved visual documents significantly outperforms baselines relying on zero-shot reasoning or few-shot example retrieval. This work establishes the basis of RAR, extending the scope of Information Retrieval from answering user queries to driving embodied physical actions.

