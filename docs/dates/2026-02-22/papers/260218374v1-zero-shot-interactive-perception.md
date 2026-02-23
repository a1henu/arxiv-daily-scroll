---
layout: default
title: Zero-shot Interactive Perception
---

# Zero-shot Interactive Perception
**arXiv**：[2602.18374v1](https://arxiv.org/abs/2602.18374) · [PDF](https://arxiv.org/pdf/2602.18374.pdf)  
**作者**：Venkatesh Sripada, Frank Guerin, Amir Ghalamzan  

**一句话要点**：提出零样本交互感知框架，结合多策略操作与视觉语言模型解决机器人复杂场景中的语义查询问题。

**关键词**：零样本学习, 交互感知, 视觉语言模型, 机器人操作, 推动动作, 语义推理

## 3 点简述
- 核心问题：机器人如何在部分可观测场景中通过物理交互提取隐藏信息并执行操作计划。
- 方法要点：集成增强观察模块、记忆引导动作模块和机器人控制器，引入pushlines视觉增强提升推动性能。
- 实验或效果：在7-DOF Franka Panda臂上评估，优于被动和基于视点的感知技术，尤其在推动任务中表现突出。

## 摘要（原文）

> Interactive perception (IP) enables robots to extract hidden information in their workspace and execute manipulation plans by physically interacting with objects and altering the state of the environment -- crucial for resolving occlusions and ambiguity in complex, partially observable scenarios. We present Zero-Shot IP (ZS-IP), a novel framework that couples multi-strategy manipulation (pushing and grasping) with a memory-driven Vision Language Model (VLM) to guide robotic interactions and resolve semantic queries. ZS-IP integrates three key components: (1) an Enhanced Observation (EO) module that augments the VLM's visual perception with both conventional keypoints and our proposed pushlines -- a novel 2D visual augmentation tailored to pushing actions, (2) a memory-guided action module that reinforces semantic reasoning through context lookup, and (3) a robotic controller that executes pushing, pulling, or grasping based on VLM output. Unlike grid-based augmentations optimized for pick-and-place, pushlines capture affordances for contact-rich actions, substantially improving pushing performance. We evaluate ZS-IP on a 7-DOF Franka Panda arm across diverse scenes with varying occlusions and task complexities. Our experiments demonstrate that ZS-IP outperforms passive and viewpoint-based perception techniques such as Mark-Based Visual Prompting (MOKA), particularly in pushing tasks, while preserving the integrity of non-target elements.

