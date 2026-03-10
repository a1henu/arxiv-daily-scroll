---
layout: default
title: See and Switch: Vision-Based Branching for Interactive Robot-Skill Programming
---

# See and Switch: Vision-Based Branching for Interactive Robot-Skill Programming
**arXiv**：[2603.08057v1](https://arxiv.org/abs/2603.08057) · [PDF](https://arxiv.org/pdf/2603.08057.pdf)  
**作者**：Petr Vanc, Jan Kristof Behrens, Václav Hlaváč, Karla Stepanova  

**一句话要点**：提出See & Switch框架，基于视觉分支选择解决机器人示教编程中的条件任务图执行问题。

**关键词**：机器人示教编程, 条件任务图, 视觉分支选择, 眼在手视觉, 异常检测, 灵巧操作

## 3 点简述
- 核心问题：示教编程难以处理现实世界变化，条件任务图需可靠感知分支选择。
- 方法要点：使用眼在手机器人视觉切换器，基于高维图像选择技能分支并检测异常。
- 实验或效果：在三个灵巧操作任务中验证，分支选择和异常检测准确率分别达90.7%和87.9%。

## 摘要（原文）

> Programming robots by demonstration (PbD) is an intuitive concept, but scaling it to real-world variability remains a challenge for most current teaching frameworks. Conditional task graphs are very expressive and can be defined incrementally, which fits very well with the PbD idea. However, acting using conditional task graphs requires reliable perception-grounded online branch selection. In this paper, we present See & Switch, an interactive teaching-and-execution framework that represents tasks as user-extendable graphs of skill parts connected via decision states (DS), enabling conditional branching during replay. Unlike prior approaches that rely on manual branching or low-dimensional signals (e.g., proprioception), our vision-based Switcher uses eye-in-hand images (high-dimensional) to select among competing successor skill parts and to detect out-of-distribution contexts that require new demonstrations. We integrate kinesthetic teaching, joystick control, and hand gestures via an input-modality-abstraction layer and demonstrate that our proposed method is teaching modality-independent, enabling efficient in-situ recovery demonstrations. The system is validated in experiments on three challenging dexterous manipulation tasks. We evaluate our method under diverse conditions and furthermore conduct user studies with 8 participants. We show that the proposed method reliably performs branch selection and anomaly detection for novice users, achieving 90.7 % and 87.9 % accuracy, respectively, across 576 real-robot rollouts. We provide all code and data required to reproduce our experiments at http://imitrob.ciirc.cvut.cz/publications/seeandswitch.

