---
layout: default
title: Interaction-Aware Whole-Body Control for Compliant Object Transport
---

# Interaction-Aware Whole-Body Control for Compliant Object Transport
**arXiv**：[2603.03751v1](https://arxiv.org/abs/2603.03751) · [PDF](https://arxiv.org/pdf/2603.03751.pdf)  
**作者**：Hao Zhang, Yves Tseng, Ding Zhao, H. Eric Tseng  

**一句话要点**：提出交互导向全身控制以解决非结构化环境中协作物体运输的稳定性问题

**关键词**：全身控制, 交互导向控制, 强化学习, 物体运输, 非结构化环境, 教师-学生蒸馏

## 3 点简述
- 核心问题：强时变交互力使跟踪式全身控制在紧密接触任务中不可靠
- 方法要点：结构分离上下身控制，结合轨迹优化参考生成器和强化学习策略
- 实验或效果：仿真训练后部署，在多种场景下保持稳定全身行为和物理交互

## 摘要（原文）

> Cooperative object transport in unstructured environments remains challenging for assistive humanoids because strong, time-varying interaction forces can make tracking-centric whole-body control unreliable, especially in close-contact support tasks. This paper proposes a bio-inspired, interaction-oriented whole-body control (IO-WBC) that functions as an artificial cerebellum - an adaptive motor agent that translates upstream (skill-level) commands into stable, physically consistent whole-body behavior under contact. This work structurally separates upper-body interaction execution from lower-body support control, enabling the robot to maintain balance while shaping force exchange in a tightly coupled robot-object system. A trajectory-optimized reference generator (RG) provides a kinematic prior, while a reinforcement learning (RL) policy governs body responses under heavy-load interactions and disturbances. The policy is trained in simulation with randomized payload mass/inertia and external perturbations, and deployed via asymmetric teacher-student distillation so that the student relies only on proprioceptive histories at runtime. Extensive experiments demonstrate that IO-WBC maintains stable whole-body behavior and physical interaction even when precise velocity tracking becomes infeasible, enabling compliant object transport across a wide range of scenarios.

