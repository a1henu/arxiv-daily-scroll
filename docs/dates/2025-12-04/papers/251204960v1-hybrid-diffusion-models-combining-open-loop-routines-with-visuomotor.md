---
layout: default
title: Hybrid-Diffusion Models: Combining Open-loop Routines with Visuomotor Diffusion Policies
---

# Hybrid-Diffusion Models: Combining Open-loop Routines with Visuomotor Diffusion Policies
**arXiv**：[2512.04960v1](https://arxiv.org/abs/2512.04960) · [PDF](https://arxiv.org/pdf/2512.04960.pdf)  
**作者**：Jonne Van Haastregt, Bastian Orthmann, Michael C. Welle, Yuchong Zhang, Danica Kragic  

**一句话要点**：提出混合扩散模型，结合开环例程与视觉运动扩散策略以提升机器人操作精度与速度。

**关键词**：混合扩散模型, 视觉运动策略, 远程操作增强原语, 机器人操作, 模仿学习, 开环控制

## 3 点简述
- 问题：基于模仿学习的视觉运动策略在复杂操作任务中精度和速度不及传统控制方法。
- 方法：开发远程操作增强原语，允许在演示中无缝执行预定义例程，混合扩散模型学习在推理时触发这些原语。
- 实验：在真实世界任务如吸液、开容器液体转移和容器拧开中验证方法有效性。

## 摘要（原文）

> Despite the fact that visuomotor-based policies obtained via imitation learning demonstrate good performances in complex manipulation tasks, they usually struggle to achieve the same accuracy and speed as traditional control based methods. In this work, we introduce Hybrid-Diffusion models that combine open-loop routines with visuomotor diffusion policies. We develop Teleoperation Augmentation Primitives (TAPs) that allow the operator to perform predefined routines, such as locking specific axes, moving to perching waypoints, or triggering task-specific routines seamlessly during demonstrations. Our Hybrid-Diffusion method learns to trigger such TAPs during inference. We validate the method on challenging real-world tasks: Vial Aspiration, Open-Container Liquid Transfer, and container unscrewing. All experimental videos are available on the project's website: https://hybriddiffusion.github.io/

