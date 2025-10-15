---
layout: default
title: Controlling Intent Expressiveness in Robot Motion with Diffusion Models
---

# Controlling Intent Expressiveness in Robot Motion with Diffusion Models
**arXiv**：[2510.12370v1](https://arxiv.org/abs/2510.12370) · [PDF](https://arxiv.org/pdf/2510.12370.pdf)  
**作者**：Wenli Shi, Clemence Grislain, Olivier Sigaud, Mohamed Chetouani  

**一句话要点**：提出基于扩散模型的机器人运动生成框架，实现意图表达可控性

**关键词**：机器人运动生成, 意图可读性, 扩散模型, 信息势场, 人机交互

## 3 点简述
- 核心问题：传统机器人运动方法效率优先，但意图可读性不足，且现有方法仅生成单一最可读轨迹
- 方法要点：使用信息势场模型评估轨迹可读性，结合两阶段扩散框架生成不同可读性水平的路径和动作
- 实验或效果：在2D和3D到达任务中验证，生成多样可控运动，性能接近SOTA

## 摘要（原文）

> Legibility of robot motion is critical in human-robot interaction, as it
> allows humans to quickly infer a robot's intended goal. Although traditional
> trajectory generation methods typically prioritize efficiency, they often fail
> to make the robot's intentions clear to humans. Meanwhile, existing approaches
> to legible motion usually produce only a single "most legible" trajectory,
> overlooking the need to modulate intent expressiveness in different contexts.
> In this work, we propose a novel motion generation framework that enables
> controllable legibility across the full spectrum, from highly legible to highly
> ambiguous motions. We introduce a modeling approach based on an Information
> Potential Field to assign continuous legibility scores to trajectories, and
> build upon it with a two-stage diffusion framework that first generates paths
> at specified legibility levels and then translates them into executable robot
> actions. Experiments in both 2D and 3D reaching tasks demonstrate that our
> approach produces diverse and controllable motions with varying degrees of
> legibility, while achieving performance comparable to SOTA. Code and project
> page: https://legibility-modulator.github.io.

