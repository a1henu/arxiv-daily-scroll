---
layout: default
title: Walking on Rough Terrain with Any Number of Legs
---

# Walking on Rough Terrain with Any Number of Legs
**arXiv**：[2603.09147v1](https://arxiv.org/abs/2603.09147) · [PDF](https://arxiv.org/pdf/2603.09147.pdf)  
**作者**：Zhuoyang Chen, Xinyuan Wang, Shai Revzen  

**一句话要点**：提出多足机器人粗糙地形控制架构，结合事件级联与CPG控制器，实现轻量自适应行走。

**关键词**：多足机器人控制, 粗糙地形行走, 事件级联控制器, 中央模式发生器, 分段机器人, 轻量自适应控制

## 3 点简述
- 核心问题：多足机器人（≥6腿）在复杂地形控制策略存在黑盒模型、CPG网络或开环控制等局限性。
- 方法要点：采用分段机器人设计，每段有相同状态机，通过前段输入实现事件级联与CPG耦合，支持接触时紧耦合地面、无接触时虚拟运动。
- 实验或效果：在仿真中验证了6至16腿机器人的有效性，作为轻量自适应控制器或机器学习基线。

## 摘要（原文）

> Robotics would gain by replicating the remarkable agility of arthropods in navigating complex environments. Here we consider the control of multi-legged systems which have 6 or more legs. Current multi-legged control strategies in robots include large black-box machine learning models, Central Pattern Generator (CPG) networks, and open-loop feed-forward control with stability arising from mechanics. Here we present a multi-legged control architecture for rough terrain using a segmental robot with 3 actuators for every 2 legs, which we validated in simulation for robots with 6 to 16 legs. Segments have identical state machines, and each segment also receives input from the segment in front of it. Our design bridges the gap between WalkNet-like event cascade controllers and CPG-based controllers: it tightly couples to the ground when contact is present, but produces fictive locomotion when ground contact is missing. The approach may be useful as an adaptive and computationally lightweight controller for multi-legged robots, and as a baseline capability for scaffolding the learning of machine learning controllers.

