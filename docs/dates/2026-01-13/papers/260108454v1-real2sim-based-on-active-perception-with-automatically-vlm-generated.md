---
layout: default
title: Real2Sim based on Active Perception with automatically VLM-generated Behavior Trees
---

# Real2Sim based on Active Perception with automatically VLM-generated Behavior Trees
**arXiv**：[2601.08454v1](https://arxiv.org/abs/2601.08454) · [PDF](https://arxiv.org/pdf/2601.08454.pdf)  
**作者**：Alessandro Adami, Sebastian Zudaire, Ruggero Carli, Pietro Falco  

**一句话要点**：提出基于主动感知的Real2Sim框架，利用VLM自动生成行为树以估计物理参数。

**关键词**：真实到仿真, 行为树生成, 视觉语言模型, 物理参数估计, 机器人交互, 主动感知

## 3 点简述
- 传统Real2Sim依赖手动测量或固定探索，难以适应任务变化和用户意图。
- 方法使用视觉语言模型推理生成行为树，指导机器人执行任务特定交互以估计参数。
- 实验在真实机械臂上验证了质量、高度和摩擦等参数的估计能力，包括遮挡场景。

## 摘要（原文）

> Constructing an accurate simulation model of real-world environments requires reliable estimation of physical parameters such as mass, geometry, friction, and contact surfaces. Traditional real-to-simulation (Real2Sim) pipelines rely on manual measurements or fixed, pre-programmed exploration routines, which limit their adaptability to varying tasks and user intents. This paper presents a Real2Sim framework that autonomously generates and executes Behavior Trees for task-specific physical interactions to acquire only the parameters required for a given simulation objective, without relying on pre-defined task templates or expert-designed exploration routines. Given a high-level user request, an incomplete simulation description, and an RGB observation of the scene, a vision-language model performs multi-modal reasoning to identify relevant objects, infer required physical parameters, and generate a structured Behavior Tree composed of elementary robotic actions. The resulting behavior is executed on a torque-controlled Franka Emika Panda, enabling compliant, contact-rich interactions for parameter estimation. The acquired measurements are used to automatically construct a physics-aware simulation. Experimental results on the real manipulator demonstrate estimation of object mass, surface height, and friction-related quantities across multiple scenarios, including occluded objects and incomplete prior models. The proposed approach enables interpretable, intent-driven, and autonomously Real2Sim pipelines, bridging high-level reasoning with physically-grounded robotic interaction.

