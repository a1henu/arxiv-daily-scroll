---
layout: default
title: Deep Whole-body Parkour
---

# Deep Whole-body Parkour
**arXiv**：[2601.07701v1](https://arxiv.org/abs/2601.07701) · [PDF](https://arxiv.org/pdf/2601.07701.pdf)  
**作者**：Ziwen Zhuang, Shaoting Zhu, Mengjie Zhao, Hang Zhao  

**一句话要点**：提出感知全身运动控制框架，实现人形机器人在非结构化地形上执行动态多接触任务。

**关键词**：人形机器人控制, 感知运动集成, 全身运动跟踪, 非结构化地形, 动态多接触任务

## 3 点简述
- 核心问题：现有方法难以兼顾地形感知与复杂全身运动，导致机器人运动能力受限。
- 方法要点：将外感知集成到全身运动跟踪中，训练单一策略执行多种动态任务。
- 实验或效果：在非结构化地形上实现稳健的跳跃和翻滚等动作，显著提升机器人通过性。

## 摘要（原文）

> Current approaches to humanoid control generally fall into two paradigms: perceptive locomotion, which handles terrain well but is limited to pedal gaits, and general motion tracking, which reproduces complex skills but ignores environmental capabilities. This work unites these paradigms to achieve perceptive general motion control. We present a framework where exteroceptive sensing is integrated into whole-body motion tracking, permitting a humanoid to perform highly dynamic, non-locomotion tasks on uneven terrain. By training a single policy to perform multiple distinct motions across varied terrestrial features, we demonstrate the non-trivial benefit of integrating perception into the control loop. Our results show that this framework enables robust, highly dynamic multi-contact motions, such as vaulting and dive-rolling, on unstructured terrain, significantly expanding the robot's traversability beyond simple walking or running. https://project-instinct.github.io/deep-whole-body-parkour

