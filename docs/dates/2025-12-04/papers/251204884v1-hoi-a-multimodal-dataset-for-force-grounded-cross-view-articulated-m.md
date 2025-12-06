---
layout: default
title: Hoi! -- A Multimodal Dataset for Force-Grounded, Cross-View Articulated Manipulation
---

# Hoi! -- A Multimodal Dataset for Force-Grounded, Cross-View Articulated Manipulation
**arXiv**：[2512.04884v1](https://arxiv.org/abs/2512.04884) · [PDF](https://arxiv.org/pdf/2512.04884.pdf)  
**作者**：Tim Engelbracht, René Zurbrügg, Matteo Wohlrapp, Martin Büchner, Abhinav Valada, Marc Pollefeys, Hermann Blum, Zuria Bauer  

**一句话要点**：提出Hoi!数据集以支持基于力感知的多视角关节操作研究

**关键词**：多模态数据集, 关节操作, 力感知, 跨视角学习, 交互理解

## 3 点简述
- 核心问题：缺乏耦合视觉、动作与力感知的多模态数据集，限制交互理解方法评估。
- 方法要点：收集3048个序列，涵盖381个关节物体，提供四种操作视角，包括同步末端力与触觉数据。
- 实验或效果：支持跨人类与机器人视角的方法迁移评估，并探索力感知等未充分研究模态。

## 摘要（原文）

> We present a dataset for force-grounded, cross-view articulated manipulation that couples what is seen with what is done and what is felt during real human interaction. The dataset contains 3048 sequences across 381 articulated objects in 38 environments. Each object is operated under four embodiments - (i) human hand, (ii) human hand with a wrist-mounted camera, (iii) handheld UMI gripper, and (iv) a custom Hoi! gripper - where the tool embodiment provides synchronized end-effector forces and tactile sensing. Our dataset offers a holistic view of interaction understanding from video, enabling researchers to evaluate how well methods transfer between human and robotic viewpoints, but also investigate underexplored modalities such as force sensing and prediction.

