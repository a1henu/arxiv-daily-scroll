---
layout: default
title: Information-Theoretic Detection of Bimanual Interactions for Dual-Arm Robot Plan Generation
---

# Information-Theoretic Detection of Bimanual Interactions for Dual-Arm Robot Plan Generation
**arXiv**：[2601.19832v1](https://arxiv.org/abs/2601.19832) · [PDF](https://arxiv.org/pdf/2601.19832.pdf)  
**作者**：Elena Merlo, Marta Lagomarsino, Arash Ajoudani  

**一句话要点**：提出基于信息论的单次RGB视频处理方法，以生成双臂机器人执行计划。

**关键词**：示教编程, 信息论, 场景图, 双臂协调, 行为树, 单次学习

## 3 点简述
- 核心问题：示教编程在双手任务中因手部协调复杂性和数据记录困难而应用受限。
- 方法要点：应用香农信息论分析场景元素间信息流，利用场景图属性检测手部协调策略。
- 实验或效果：通过多主体视频演示和公开数据集验证，在生成集中式双臂协调执行计划方面优于现有方法。

## 摘要（原文）

> Programming by demonstration is a strategy to simplify the robot programming process for non-experts via human demonstrations. However, its adoption for bimanual tasks is an underexplored problem due to the complexity of hand coordination, which also hinders data recording. This paper presents a novel one-shot method for processing a single RGB video of a bimanual task demonstration to generate an execution plan for a dual-arm robotic system. To detect hand coordination policies, we apply Shannon's information theory to analyze the information flow between scene elements and leverage scene graph properties. The generated plan is a modular behavior tree that assumes different structures based on the desired arms coordination. We validated the effectiveness of this framework through multiple subject video demonstrations, which we collected and made open-source, and exploiting data from an external, publicly available dataset. Comparisons with existing methods revealed significant improvements in generating a centralized execution plan for coordinating two-arm systems.

