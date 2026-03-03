---
layout: default
title: Bimanual XR Specification of Relative and Absolute Assembly Hierarchies for Teleoperation
---

# Bimanual XR Specification of Relative and Absolute Assembly Hierarchies for Teleoperation
**arXiv**：[2603.01495v1](https://arxiv.org/abs/2603.01495) · [PDF](https://arxiv.org/pdf/2603.01495.pdf)  
**作者**：Benjamin Yang, Xichen He, Charlie Zou, Jen-Shuo Liu, Barbara Tversky, Steven Feiner  

**一句话要点**：提出双手XR交互方法，通过相对与绝对约束层次指定远程装配任务，以支持机器人高级遥操作目标。

**关键词**：双手交互, 扩展现实, 远程装配, 约束层次, 机器人遥操作

## 3 点简述
- 核心问题：如何高效指定远程装配任务，允许机器人软件灵活选择子装配位置以提高效率。
- 方法要点：使用双手抓取对象创建约束组，支持相对和绝对6DoF姿态，并可嵌套成层次结构。
- 实验或效果：未知，但方法旨在通过可视化外壳和层次化约束简化用户指定过程。

## 摘要（原文）

> We present a bimanual XR interaction approach for specifying remote assembly tasks as hierarchies of relative and absolute object constraints that specify high-level teleoperation goals for robots. Grabbing one object in each hand creates a constraint group (visualized as a hull) and groups can be nested into hierarchies. Each group can be relative (with a robot-specifiable 6DoF pose) or absolute (with an author-specified fixed 6DoF pose) in relation to its parent. A relative group specifies a subassembly that can be constructed at a location chosen by the robot software for efficiency rather than mandated by the user.

