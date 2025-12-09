---
layout: default
title: Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation
---

# Affordance Field Intervention: Enabling VLAs to Escape Memory Traps in Robotic Manipulation
**arXiv**：[2512.07472v1](https://arxiv.org/abs/2512.07472) · [PDF](https://arxiv.org/pdf/2512.07472.pdf)  
**作者**：Siyu Xu, Zijian Wang, Yunke Wang, Chenghao Xia, Tao Huang, Chang Xu  

**一句话要点**：提出Affordance Field Intervention，通过3D空间可操作场引导VLA模型，以解决机器人操作中的记忆陷阱问题。

**关键词**：视觉-语言-动作模型, 机器人操作, 3D空间可操作场, 分布偏移, 记忆陷阱, 轻量级框架

## 3 点简述
- 核心问题：VLA模型在分布偏移下易陷入记忆陷阱，重复记忆轨迹而非适应新场景。
- 方法要点：使用3D空间可操作场作为轻量级插件，检测记忆陷阱并生成可操作驱动的路径点。
- 实验或效果：在真实机器人平台和LIBERO-Pro基准上，平均性能提升23.5%和20.2%。

## 摘要（原文）

> Vision-Language-Action (VLA) models have shown great performance in robotic manipulation by mapping visual observations and language instructions directly to actions. However, they remain brittle under distribution shifts: when test scenarios change, VLAs often reproduce memorized trajectories instead of adapting to the updated scene, which is a failure mode we refer to as the "Memory Trap". This limitation stems from the end-to-end design, which lacks explicit 3D spatial reasoning and prevents reliable identification of actionable regions in unfamiliar environments. To compensate for this missing spatial understanding, 3D Spatial Affordance Fields (SAFs) can provide a geometric representation that highlights where interactions are physically feasible, offering explicit cues about regions the robot should approach or avoid. We therefore introduce Affordance Field Intervention (AFI), a lightweight hybrid framework that uses SAFs as an on-demand plug-in to guide VLA behavior. Our system detects memory traps through proprioception, repositions the robot to recent high-affordance regions, and proposes affordance-driven waypoints that anchor VLA-generated actions. A SAF-based scorer then selects trajectories with the highest cumulative affordance. Extensive experiments demonstrate that our method achieves an average improvement of 23.5% across different VLA backbones ($π_{0}$ and $π_{0.5}$) under out-of-distribution scenarios on real-world robotic platforms, and 20.2% on the LIBERO-Pro benchmark, validating its effectiveness in enhancing VLA robustness to distribution shifts.

