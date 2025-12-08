---
layout: default
title: Correspondence-Oriented Imitation Learning: Flexible Visuomotor Control with 3D Conditioning
---

# Correspondence-Oriented Imitation Learning: Flexible Visuomotor Control with 3D Conditioning
**arXiv**：[2512.05953v1](https://arxiv.org/abs/2512.05953) · [PDF](https://arxiv.org/pdf/2512.05953.pdf)  
**作者**：Yunhao Cao, Zubin Bhaumik, Jessie Jia, Xingyi He, Kuan Fang  

**一句话要点**：提出对应导向模仿学习框架，通过3D关键点运动表示实现灵活视觉运动控制。

**关键词**：视觉运动控制, 模仿学习, 3D关键点, 时空注意力, 自监督训练, 任务泛化

## 3 点简述
- 核心问题：视觉运动控制中任务表示缺乏灵活性，难以适应可变空间和时间粒度。
- 方法要点：基于3D关键点运动定义任务，采用时空注意力机制融合多模态信息，通过自监督训练学习条件策略。
- 实验或效果：在真实世界操作任务中，优于先前方法，泛化能力强，支持稀疏和密集任务规范。

## 摘要（原文）

> We introduce Correspondence-Oriented Imitation Learning (COIL), a conditional policy learning framework for visuomotor control with a flexible task representation in 3D. At the core of our approach, each task is defined by the intended motion of keypoints selected on objects in the scene. Instead of assuming a fixed number of keypoints or uniformly spaced time intervals, COIL supports task specifications with variable spatial and temporal granularity, adapting to different user intents and task requirements. To robustly ground this correspondence-oriented task representation into actions, we design a conditional policy with a spatio-temporal attention mechanism that effectively fuses information across multiple input modalities. The policy is trained via a scalable self-supervised pipeline using demonstrations collected in simulation, with correspondence labels automatically generated in hindsight. COIL generalizes across tasks, objects, and motion patterns, achieving superior performance compared to prior methods on real-world manipulation tasks under both sparse and dense specifications.

