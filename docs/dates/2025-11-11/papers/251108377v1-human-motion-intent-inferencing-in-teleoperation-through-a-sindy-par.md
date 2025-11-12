---
layout: default
title: Human Motion Intent Inferencing in Teleoperation Through a SINDy Paradigm
---

# Human Motion Intent Inferencing in Teleoperation Through a SINDy Paradigm
**arXiv**：[2511.08377v1](https://arxiv.org/abs/2511.08377) · [PDF](https://arxiv.org/pdf/2511.08377.pdf)  
**作者**：Michael Bowman, Xiaoli Zhang  

**一句话要点**：提出Psychic框架，通过SINDy范式推断遥操作中的人类运动意图。

**关键词**：意图推断, 遥操作, SINDy模型, 随机微分方程, 运动分析, 目标检测

## 3 点简述
- 核心问题：现有意图推断方法忽略细微运动，难以检测意图突变。
- 方法要点：使用跳跃-漂移-扩散SDE建模运动，结合KM系数和异常检测识别目标转换。
- 实验或效果：在600条轨迹上验证，支持离线和在线学习，生成概率可达集。

## 摘要（原文）

> Intent inferencing in teleoperation has been instrumental in aligning operator goals and coordinating actions with robotic partners. However, current intent inference methods often ignore subtle motion that can be strong indicators for a sudden change in intent. Specifically, we aim to tackle 1) if we can detect sudden jumps in operator trajectories, 2) how we appropriately use these sudden jump motions to infer an operator's goal state, and 3) how to incorporate these discontinuous and continuous dynamics to infer operator motion. Our framework, called Psychic, models these small indicative motions through a jump-drift-diffusion stochastic differential equation to cover discontinuous and continuous dynamics. Kramers-Moyal (KM) coefficients allow us to detect jumps with a trajectory which we pair with a statistical outlier detection algorithm to nominate goal transitions. Through identifying jumps, we can perform early detection of existing goals and discover undefined goals in unstructured scenarios. Our framework then applies a Sparse Identification of Nonlinear Dynamics (SINDy) model using KM coefficients with the goal transitions as a control input to infer an operator's motion behavior in unstructured scenarios. We demonstrate Psychic can produce probabilistic reachability sets and compare our strategy to a negative log-likelihood model fit. We perform a retrospective study on 600 operator trajectories in a hands-free teleoperation task to evaluate the efficacy of our opensource package, Psychic, in both offline and online learning.

