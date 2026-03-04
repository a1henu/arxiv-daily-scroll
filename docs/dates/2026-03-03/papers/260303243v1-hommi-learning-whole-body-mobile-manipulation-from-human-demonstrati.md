---
layout: default
title: HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations
---

# HoMMI: Learning Whole-Body Mobile Manipulation from Human Demonstrations
**arXiv**：[2603.03243v1](https://arxiv.org/abs/2603.03243) · [PDF](https://arxiv.org/pdf/2603.03243.pdf)  
**作者**：Xiaomeng Xu, Jisang Park, Han Zhang, Eric Cousineau, Aditya Bhat, Jose Barreiros, Dian Wang, Shuran Song  

**一句话要点**：提出HoMMI框架，通过无机器人人类演示学习全身移动操作，解决跨具身策略转移难题。

**关键词**：全身移动操作, 人类演示学习, 跨具身策略, 手眼协调, 主动感知

## 3 点简述
- 核心问题：无机器人演示引入观察与动作空间的跨具身鸿沟，阻碍策略迁移。
- 方法要点：采用跨具身手眼策略设计，包括具身无关视觉表示、松弛头部动作表示和全身控制器。
- 实验或效果：实现长时程移动操作任务，支持双手协调、导航和主动感知，效果见项目网站。

## 摘要（原文）

> We present Whole-Body Mobile Manipulation Interface (HoMMI), a data collection and policy learning framework that learns whole-body mobile manipulation directly from robot-free human demonstrations. We augment UMI interfaces with egocentric sensing to capture the global context required for mobile manipulation, enabling portable, robot-free, and scalable data collection. However, naively incorporating egocentric sensing introduces a larger human-to-robot embodiment gap in both observation and action spaces, making policy transfer difficult. We explicitly bridge this gap with a cross-embodiment hand-eye policy design, including an embodiment agnostic visual representation; a relaxed head action representation; and a whole-body controller that realizes hand-eye trajectories through coordinated whole-body motion under robot-specific physical constraints. Together, these enable long-horizon mobile manipulation tasks requiring bimanual and whole-body coordination, navigation, and active perception. Results are best viewed on: https://hommi-robot.github.io

