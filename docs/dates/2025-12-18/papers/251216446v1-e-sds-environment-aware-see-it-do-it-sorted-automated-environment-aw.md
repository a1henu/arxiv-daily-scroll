---
layout: default
title: E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
---

# E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
**arXiv**：[2512.16446v1](https://arxiv.org/abs/2512.16446) · [PDF](https://arxiv.org/pdf/2512.16446.pdf)  
**作者**：Enis Yalcin, Joshua O'Hara, Maria Stamatopoulou, Chengxu Zhou, Dimitrios Kanoulas  

**一句话要点**：提出E-SDS框架，通过环境感知自动生成奖励函数，以解决人形机器人复杂地形导航问题。

**关键词**：人形机器人运动, 强化学习, 环境感知, 奖励函数自动生成, 视觉语言模型

## 3 点简述
- 核心问题：现有基于视觉语言模型的奖励设计方法缺乏环境感知，难以处理复杂地形。
- 方法要点：结合视觉语言模型与实时地形传感器分析，自动生成基于示例视频的奖励函数。
- 实验或效果：在四种地形上测试，E-SDS成功实现楼梯下降，并减少速度跟踪误差51.9-82.6%。

## 摘要（原文）

> Vision-language models (VLMs) show promise in automating reward design in humanoid locomotion, which could eliminate the need for tedious manual engineering. However, current VLM-based methods are essentially "blind", as they lack the environmental perception required to navigate complex terrain. We present E-SDS (Environment-aware See it, Do it, Sorted), a framework that closes this perception gap. E-SDS integrates VLMs with real-time terrain sensor analysis to automatically generate reward functions that facilitate training of robust perceptive locomotion policies, grounded by example videos. Evaluated on a Unitree G1 humanoid across four distinct terrains (simple, gaps, obstacles, stairs), E-SDS uniquely enabled successful stair descent, while policies trained with manually-designed rewards or a non-perceptive automated baseline were unable to complete the task. In all terrains, E-SDS also reduced velocity tracking error by 51.9-82.6%. Our framework reduces the human effort of reward design from days to less than two hours while simultaneously producing more robust and capable locomotion policies.

