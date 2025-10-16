---
layout: default
title: Tactile-Conditioned Diffusion Policy for Force-Aware Robotic Manipulation
---

# Tactile-Conditioned Diffusion Policy for Force-Aware Robotic Manipulation
**arXiv**：[2510.13324v1](https://arxiv.org/abs/2510.13324) · [PDF](https://arxiv.org/pdf/2510.13324.pdf)  
**作者**：Erik Helmut, Niklas Funk, Tim Schneider, Cristiana de Farias, Jan Peters  

**一句话要点**：提出FARM框架，通过触觉条件扩散策略解决接触丰富操作中的力控制问题。

**关键词**：触觉反馈, 扩散策略, 力控制, 模仿学习, 机器人操作, 触觉传感器

## 3 点简述
- 核心问题：现有模仿学习常忽略触觉反馈对力的控制，导致操作中力应用不当。
- 方法要点：集成高维触觉数据，预测力信号并定义基于力的动作空间。
- 实验效果：在高中低力任务中优于基线，验证触觉观测和力控制空间的优势。

## 摘要（原文）

> Contact-rich manipulation depends on applying the correct grasp forces
> throughout the manipulation task, especially when handling fragile or
> deformable objects. Most existing imitation learning approaches often treat
> visuotactile feedback only as an additional observation, leaving applied forces
> as an uncontrolled consequence of gripper commands. In this work, we present
> Force-Aware Robotic Manipulation (FARM), an imitation learning framework that
> integrates high-dimensional tactile data to infer tactile-conditioned force
> signals, which in turn define a matching force-based action space. We collect
> human demonstrations using a modified version of the handheld Universal
> Manipulation Interface (UMI) gripper that integrates a GelSight Mini visual
> tactile sensor. For deploying the learned policies, we developed an actuated
> variant of the UMI gripper with geometry matching our handheld version. During
> policy rollouts, the proposed FARM diffusion policy jointly predicts robot
> pose, grip width, and grip force. FARM outperforms several baselines across
> three tasks with distinct force requirements -- high-force, low-force, and
> dynamic force adaptation -- demonstrating the advantages of its two key
> components: leveraging force-grounded, high-dimensional tactile observations
> and a force-based control space. The codebase and design files are open-sourced
> and available at https://tactile-farm.github.io .

